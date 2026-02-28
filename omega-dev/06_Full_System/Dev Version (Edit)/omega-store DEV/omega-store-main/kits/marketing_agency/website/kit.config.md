# KIT CONFIG — Website

**Kit:** Website
**Version:** 1.0
**Activates when:** PROJECT.md → Project Type = Website (or similar)

---

## Authority Hierarchy

```
1. constitution/SECURITY.xml     ← Supreme (never override)
2. constitution/QUALITY.xml      ← Quality standards
3. constitution/PROMPTING.xml    ← Communication methods
4. constitution/*.xml            ← Other laws
5. This Kit's BEST_PRACTICES.xml      ← Specialized laws (Aesthetics/ACC)
6. This Kit's PROMPTER.md            ← Discovery + requirements
7. This Kit's kit.config.md          ← Activation rules (this file)
8. This Kit's WEBSITE_KIT.md         ← Patterns + checklists
9. user-input/seed/*.md              ← User's project context
```

**Rule:** Higher number never overrides lower number.

---

## Kit Contents

| File | Purpose |
|:-----|:--------|
| `PROMPTER.md` | How to discover requirements, what questions to ask |
| `WEBSITE_KIT.md` | Sitemap templates, SEO checklist, performance budgets, patterns |
| `kit.config.md` | This file — activation rules |
| `preproduction/` | Market Audit, SEO Intent, Wireframes/UX, Copywriting Structure |
| `production/` | Tasks during build (SEO, accessibility, performance) |
| `testing/` | Tasks before launch (browser, mobile, lighthouse) |
| `publication/` | Tasks for launch (SSL, DNS, Handoff, Cleanup) |
| `TRACKER.md` | Progress tracking for this kit |
| `README.md` | Quick reference for this kit |

---

## Activation Flow

```
1. User runs RUN.md or ignition prompt
2. AI loads constitution (mandatory)
3. AI reads user-input/seed/PROJECT.md
4. AI detects: Project Type = Website
5. AI loads this kit:
   └── First: PROMPTER.md (discovery)
   └── Then: BEST_PRACTICES.xml (technical laws)
   └── Then: 4-Phase Specialized Lifecycle:
       ├── 01_preproduction/ (Market Audit -> SEO -> UX -> Copy)
       ├── 02_production/
       ├── 03_testing/
       └── 04_publication/
6. PROMPTER.md drives the conversation
7. Build begins only when requirements table is complete
```

---

## Override Rules

| If this says... | But this says... | Winner |
|:----------------|:-----------------|:-------|
| WEBSITE_KIT.md: LCP <2.5s | CONSTRAINTS.md: LCP <1.5s | CONSTRAINTS.md |
| WEBSITE_KIT.md: breakpoint 640px | BRAND.md: breakpoint 768px | BRAND.md |
| Anything in this kit | SECURITY.xml | SECURITY.xml (always) |
| PROMPTER.md: ask 4 questions | User: "Just build it" | PROMPTER.md (requirements must be filled) |

---

## When NOT to Use This Kit

- Project type = Web Application (SaaS) → Use `saas/` kit
- Project type = API only → Use `api/` kit
- Project type = Mobile app → Use `mobile/` kit (when created)

---

*This config is read-only during build. Modify only between projects.*
