# Contributing Guidelines

## Workflow
1. Fork or clone the repository.  
2. Create a new branch: `git checkout -b feat/my-feature`.  
3. Write code, tests, and documentation.  
4. Commit with clear, descriptive messages.  
5. Push your branch and open a Pull Request (PR).  
6. Request at least one teammate review before merging.  

## Branch Naming
- `feat/<function>` — New feature or functionality  
- `fix/<bug>` — Bug fix or patch  
- `docs/<file>` — Documentation-only updates  
- `chore/<task>` — Cleanup, configuration, or maintenance  

## Pull Request (PR) Process
- Each PR must **close or reference** a related issue.  
- Complete the PR template checklist before submitting.  
- Do **not** merge your own PR without review.  
- Use **Squash & Merge** once approved to maintain a clean commit history.  

## Contribution Minimums
- Each member must contribute **3–5 functions**.  
- Each member must review **at least 2 PRs** from other teammates.  
- Update `docs/function_reference.md` whenever new functions are added.  

## Tests
- Each function must include **doctest examples**.  
- Run the following command before pushing:  
  ```bash
  python -m doctest -v src/irlib.py
