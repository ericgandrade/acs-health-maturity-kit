# Contributing

Thank you for helping improve the ACS Health Maturity Kit.

## Ways to contribute
- **Report how you used the kit** with the Adoption report issue form.
- **Suggest a question or correction** with the Feedback issue form, citing the framework or source.
- **Propose a change** with a pull request.

## Rules for changes
1. Questions live only in `data/questionnaire.csv`. Each new question needs a unique ID, a target state, evidence, a recommended action and at least one framework reference.
2. Licensing statements in `data/license_security_map.csv` must cite current Microsoft documentation in the pull request description.
3. Rebuild the workbook with `python tools/build_workbook.py` and include it in the pull request.
4. Never include protected health information, credentials or details of any organization's environment.
5. Update `CHANGELOG.md`.

By contributing, you agree that your contribution is licensed under the same terms as the repository (CC BY 4.0 for content, MIT for code).
