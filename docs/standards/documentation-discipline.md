# Documentation Discipline

Standards for maintaining thesis documents in this repository.

## Rules

1. Every document must have a clear purpose stated in its first heading or opening line.
2. Use consistent heading hierarchy: `#` for title, `##` for major sections, `###` for subsections. Never skip levels.
3. Version-sensitive documents (System Specification, PRD, Model Design) must include a version number and date in the frontmatter or first heading. Thesis documents use a JSON `## Metadata` block (`document-type`, `version`, `date`, `authors`).
4. When moving a file, update all documents that reference its old path. Check `INDEX.md`, `AGENTS.md`, and any cross-referencing documents.
5. Mark outdated documents clearly with `(OLD)` or `(OUTDATED)` in the filename and a notice at the top of the file body. Do not delete them outright — they may contain historical context. Current preserved `(OLD)` copies live in `docs/thesis/system/`.
6. Keep `INDEX.md` as the authoritative navigation index. When adding, moving, or removing files, update `INDEX.md` in the same commit.
7. AI-generated content (summaries, compilations, analyses) must be distinguishable from human-authored content. Use clear file naming (`_summarized.json`, `_Compilation.md`) and avoid mixing generated and hand-written prose in the same file.
8. Binary assets (PDFs, XLSX, CSV, ZIP) should be tracked via Git LFS. Do not commit large binaries directly to git history.
9. The authoritative versions of the thesis documents live in the Google Drive folder. Repo copies are working mirrors — never assume they are current; verify against the Drive source before citing.

## Cross-References

When one document references another, use relative paths:

```markdown
See [System Specification](docs/thesis/specifications/system-spec.md) for details.
```

Verify the path exists before committing. Broken cross-references degrade agent navigation.
