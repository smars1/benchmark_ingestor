# GIT_BEST_PRACTICES.md

## Branching Model

- main: stable and protected
- dev: integration
- feature/*: development

## Setup Commands

```bash
git checkout main
git pull
git checkout -b dev
git push -u origin dev
git checkout -b feature/your-feature
```

## Rules

- Never commit directly to main
- One feature per branch
- Keep commits atomic

## Merge Flow

feature/* -> dev -> main

## Tagging

Use semantic versions:

v0.1.0
v0.2.0
