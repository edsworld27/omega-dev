# OMEGA STORE: WEBSITE KIT TREEMAP

This is the localized Treemap and Phase Table for the **Website Kit**. This map guides the AI through the strict architectural lifecycle of a web project.

## Website Kit Lifecycle Phases

| Phase | Purpose | Mandatory Tasks | Output |
| :--- | :--- | :--- | :--- |
| **01 Pre-Production** | Discovery, UX Architecture, & Routing | `01_MARKET_AUDIT`, `01_GLOBAL_VARIABLES_CMS`, `03.5_SITEMAP`, `03.8_AI_BUILDER_ROUTING` (If requested) | Approved UI Architecture & Config |
| **02 Production** | Functional Development & Component Weaving | `INDEX.html`, `main.jsx`, `Layout` | Fully responsive frontend |
| **03 Verification** | Audits, Cleanups, & Security Gates | `01_SEO_PAGE_SPEED`, `02_SECURITY_AUDIT` (The Guardian Gate) | 100/100 Lighthouse, Security Passed |
| **04 Publication** | Deployment & Global Indexing | `01_VERCEL_DEPLOY`, `02_WEBMASTER_SETUP`, `02.5_TRACKING_AND_SCHEMA` | Live URL, Analytics Installed |
| **05 Maintenance** | Post-Launch Edits & Integrations | `01_BLOG_OR_EDIT` | Updated CMS config, localized plugins |

## Fractal Structure
```
website/
├── WEBSITE_KIT.md                      # Core Kit Rulebook
├── PROMPTER.md                         # Discovery variables (Budget, Tech Stack, Router)
├── TREEMAP.md                          # (This File) Localized Kit Index
├── preproduction/                      # Architecture Phase
│   ├── 01_MARKET_AUDIT.task.md         # Brand & Competitors
│   ├── 01_GLOBAL_VARIABLES_CMS.task.md # Hot Swap Data (NAPO, Colors, Fonts)
│   ├── 02_SEO_INTENT.task.md           # Keywords & States
│   ├── 03_WIREFRAME_UX.task.md         # Component Layout
│   ├── LANDING_PAGE_SECTIONS.md        # Modular Visual Dictionary
│   ├── 03.5_SITEMAP_ARCHITECTURE.task.md # Page Tree rules
│   ├── 03.8_AI_BUILDER_ROUTING.task.md # Handoff to Lovable/v0
│   └── 04_COPY_STRUCTURE.task.md       # Content Mapping
├── production/                         # Execution Phase (Standard)
│   └── 02.5_TRACKING_AND_SCHEMA.task.md# GTM, Pixels, & JSON-LD
├── testing/                            # Verification Phase
│   ├── 01_SEO_PAGE_SPEED.task.md       # Mandatory Audit Loop
│   └── 02_SECURITY_AUDIT.task.md       # The Guardian Gate
├── publication/                        # Launch Phase
│   ├── 01_VERCEL_DEPLOY.task.md        # Git connection
│   └── 02_WEBMASTER_SETUP.task.md      # Console indexing
└── 05_maintenance/                     # Post-Launch Phase
    └── 01_BLOG_OR_EDIT.task.md         # Hot Swap Edits & Plugins
```
