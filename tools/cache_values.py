#!/usr/bin/env python3
"""Store calculated formula values in the assessment workbook, so results also display in viewers that do not recalculate.

openpyxl writes formulas without their results. This script evaluates the workbook with the `formulas` package
(pip install formulas) and writes each result next to its formula. The workbook still recalculates when opened in Excel
or LibreOffice (fullCalcOnLoad stays on), so the stored values never override a live calculation.

Usage:  python tools/cache_values.py [workbook.xlsx]     (default: toolkit/ACS-Health-Maturity-Assessment.xlsx)
Run it after tools/build_workbook.py. It takes about a minute.
"""
import re, shutil, sys, tempfile, zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
TARGET = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'toolkit' / 'ACS-Health-Maturity-Assessment.xlsx'
CELL = re.compile(r'<c r="([A-Z]+[0-9]+)"((?: [a-z]+="[^"]*")*)><f>(.*?)</f><v ?/>(?:</v>)?</c>|'
                  r'<c r="([A-Z]+[0-9]+)"((?: [a-z]+="[^"]*")*)><f>(.*?)</f><v></v></c>', re.S)


def calculate(path):
    try:
        import formulas
    except ImportError:
        sys.exit('This step needs the "formulas" package: pip install formulas')
    from openpyxl import load_workbook
    names = load_workbook(path, read_only=True).sheetnames
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / 'wb.xlsx'
        shutil.copy(path, src)
        solution = formulas.ExcelModel().loads(str(src)).finish().calculate()
    values = {}
    upper = {n.upper(): n for n in names}
    for key, rng in solution.items():
        m = re.match(r"^'\[[^\]]+\](.+)'!([A-Z]+[0-9]+)$", key)
        if not m or m.group(1).upper() not in upper:
            continue
        try:
            v = rng.value[0][0]
        except (AttributeError, IndexError, TypeError):
            continue
        values[(upper[m.group(1).upper()], m.group(2))] = v
    return names, values


def render(v):
    """Return (type attribute, text) for a calculated value, or None to leave the cell uncached."""
    if isinstance(v, bool):
        return ' t="b"', '1' if v else '0'
    if isinstance(v, (int, float)):
        return '', repr(float(v)) if isinstance(v, float) and not float(v).is_integer() else str(int(v))
    if isinstance(v, str):
        return ' t="str"', escape(v)
    if v is None or type(v).__name__ == 'XlEmpty' or 'empty' in type(v).__name__.lower():
        return ' t="str"', ''
    return None  # errors and anything unusual stay uncached


def main():
    names, values = calculate(TARGET)
    tmp = TARGET.with_suffix('.tmp.xlsx')
    stored = skipped = 0
    with zipfile.ZipFile(TARGET) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            m = re.match(r'xl/worksheets/sheet(\d+)\.xml$', item.filename)
            if m:
                sheet = names[int(m.group(1)) - 1]
                xml = data.decode('utf-8')

                def fix(mm):
                    nonlocal stored, skipped
                    ref, attrs, f = (mm.group(1), mm.group(2), mm.group(3)) if mm.group(1) else (mm.group(4), mm.group(5), mm.group(6))
                    r = render(values.get((sheet, ref))) if (sheet, ref) in values else None
                    if r is None:
                        skipped += 1
                        return mm.group(0)
                    stored += 1
                    attrs = re.sub(r' t="[^"]*"', '', attrs)
                    return f'<c r="{ref}"{attrs}{r[0]}><f>{f}</f><v>{r[1]}</v></c>'

                data = CELL.sub(fix, xml).encode('utf-8')
            zout.writestr(item, data)
    tmp.replace(TARGET)
    print(f'Stored {stored} calculated values in {TARGET.name} ({skipped} formula cells left uncached)')


if __name__ == '__main__':
    main()
