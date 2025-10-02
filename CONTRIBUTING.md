```markdown
# Contributing Guidelines


## Workflow
1. Fork/clone the repository.
2. Create a new branch: `git checkout -b feat/my-feature`.
3. Write code + tests + docs.
4. Commit with clear messages.
5. Push branch and open a Pull Request.
6. Request at least one teammate review before merge.


## Branch naming
- `feat/<function>` — new feature
- `fix/<bug>` — bug fix
- `docs/<file>` — documentation only
- `chore/<task>` — cleanup/config


## PR process
- Each PR must close or reference an issue.
- Fill out PR template checklist.
- Do not merge your own PR without review.
- Squash & merge once approved.


## Contribution minimums
- Each member: 3–5 functions.
- Each member: review at least 2 PRs.
- Update `docs/function_reference.md` when adding functions.


## Tests
- Each function must include doctest examples.
- Run `python -m doctest -v src/irlib.py` before pushing.
