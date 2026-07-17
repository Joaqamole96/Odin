# Documentation Discipline

Standards for maintaining thesis documents in this repository.

## Rules

1. Every document must have a clear purpose stated in its first heading or opening line.
2. Use consistent heading hierarchy: `#` for title, `##` for major sections, `###` for subsections. Never skip levels.
3. Version-sensitive documents (Specification, PRD, Model Design) must include a version number and date in the frontmatter or first heading.
4. When moving a file, update all documents that reference its old path. Check `INDEX.md`, `AGENTS.md`, and any cross-referencing documents.
5. Mark outdated documents clearly with `(OUTDATED)` in the filename and a notice at the top of the file body. Do not delete them outright — they may contain historical context.
6. Keep `INDEX.md` as the authoritative navigation index. When adding, moving, or removing files, update `INDEX.md` in the same commit.
7. AI-generated content (summaries, compilations, analyses) must be distinguishable from human-authored content. Use clear file naming (`_summarized.md`, `_Compilation.md`) and avoid mixing generated and hand-written prose in the same file.
8. Binary assets (PDFs, XLSX, CSV, ZIP) should be tracked via Git LFS. Do not commit large binaries directly to git history.

## Cross-References

When one document references another, use relative paths:

```markdown
See [Specification](Documents/Thesis/System/Specification.md) for details.
```

Verify the path exists before committing. Broken cross-references degrade agent navigation.
