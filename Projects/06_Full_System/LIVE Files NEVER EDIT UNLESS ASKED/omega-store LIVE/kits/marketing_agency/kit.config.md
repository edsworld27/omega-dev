# KIT CONFIG — Marketing Agency (Meta-Kit)

**Kit:** Marketing Agency
**Version:** 1.0
**Activates when:** PROJECT.md → Project Type = Marketing Agency (or similar)

---

## Meta-Kit Authority
- **Primary:** Marketing Agency Kit
- **Hosted Kit:** Website Kit
- **Logic:** This kit stacks on top of the Website Kit. When activated, both kits load. Agency tasks take priority in the lifecycle.

---

## Authority Hierarchy
```
1. constitution/SECURITY.xml
2. constitution/QUALITY.xml
3. This Kit's PROMPTER.md
4. Website Kit (ALL Laws)
5. This Kit's MARKETING_AGENCY.md
```

---

## Kit Contents
| File | Purpose |
|:-----|:--------|
| `PROMPTER.md` | Agency discovery (Google Maps, Apple Connect, Citations) |
| `MARKETING_AGENCY.md` | Agency checklists and service standards |
| `04_publication/MARKETING_PUBLISH.task.md` | Maps, Profiles, and Citations |

---

## Activation Flow
```
1. User requests "Marketing Agency" project.
2. AI detects type.
3. AI Loads Marketing Agency Kit.
4. AI Auto-Loads Website Kit (Hosted).
5. AI merges lifecycles.
```
