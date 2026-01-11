# Git Best Practices for Safe Refactors

Reusable Git workflow focused on safety, clarity, and low-stress development.

## Branch Strategy

- main: stable, production-ready
- dev: integration branch
- feature/*: isolated development

```
main
 └── dev
      └── feature/your-feature-name
```

## Why Set This Up Before Coding

- Architecture refactors are not trivial
- Provides rollback safety
- Keeps history clean
- Reduces cognitive load

## Workflow

1. Always start from main
2. Create dev branch
3. Create feature branch
4. Work only in feature
5. Merge feature -> dev
6. Test
7. Merge dev -> main
8. Tag release

## Commit Guidelines

- Small commits
- One concern per commit
- Clear messages

Examples:

feat(storage): add StorageBackend interface  
refactor(core): inject storage backend  
feat(storage): add s3 adapter  

## Benefits

- Less stress
- Safer refactors
- Easier reviews
- Professional workflow
