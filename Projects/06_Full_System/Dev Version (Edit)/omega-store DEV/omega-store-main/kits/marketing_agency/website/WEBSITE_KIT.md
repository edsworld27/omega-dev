# WEBSITE KIT — Starter Pattern

## Specialized Laws
- **Legal Authority:** See [BEST_PRACTICES.xml](file:///Users/eds/Documents/Omega%20Constitution%20Pack/Omega%20DEV%20Panel/06_Full_System/omega-store/kits/website/BEST_PRACTICES.xml) for Accessibility and Aesthetic mandates.
- **Asset Layer:** See [AESTHETIC_LAYER.xml](file:///Users/eds/Documents/Omega%20Constitution%20Pack/Omega%20DEV%20Panel/06_Full_System/omega-store/kits/website/assets/AESTHETIC_LAYER.xml) for CSS presets.
- **Design Intelligence:** Every project MUST adhere to the [UI_UX_PRO_MAX_TEMPLATE.md](file:///Volumes/Internal/Projects/Omega%20System/Omega%20System%20DEV%20MODE/Projects/06_Full_System/Dev%20Version%20(Edit)/omega-store%20DEV/omega-store-main/kits/marketing_agency/website/UI_UX_PRO_MAX_TEMPLATE.md) philosophy.

## The 5 Core Dimensions (Pro Max)
All builds must be architected across these non-negotiable dimensions:
1. **SKELETON (Pattern & Layout):** SaaS, Micro-SaaS, E-comm, or Bento.
2. **SKIN (Style & Aesthetic):** Glass, Aurora, Linear, or Liquid.
3. **PALETTE (Color & Theme):** 60-30-10 rule, verified WCAG contrast.
4. **VOICE (Typography):** Strategic font pairings (Modern/Tech, Luxury, etc.).
5. **SOUL (Interaction):** Micro-interactions, spring animations, and page transitions.

## Specialized Lifecycle
| Phase | Folder | Focus | Goal |
| :--- | :--- | :--- | :--- |
| **I. Pre-Production** | `01_preproduction/` | Market Audit -> SEO Intent -> UX -> Copy | Approved PRD & Assets |
| **II. Production** | `02_production/` | Rapid Build | Iterative Fulfill (IRONCORE) |
| **III. Verification** | `03_testing/` | Audit -> Perfect -> Security | High-Resolution Evidence |
| **IV. Publication** | `04_publication/` | Deployment & Handoff | Live Asset & Secure Handoff |

## Maestro Modes
- **Full Discovery (Default):** Market Audit -> SEO Intent -> UX Journey -> Fulfillment.
- **Skip to Design:** Bypasses Phase I research. AI immediately generates **TREEMAP.md** and **CP_STRUCTURE.md** for approval before any code.
- **3D Scrollytelling Mode:** Focuses on scroll-linked canvas animations using image sequences (120+ frames). Includes loading UI, sticky canvas, and transformative text overlays. Optimized for background `#050505`.
- **Premium UI Styles (UI/UX Pro Max):**
    - **Linear Aesthetic:** 1px borders, high-contrast, developer-centric.
    - **Aurora UI:** Mesh gradients and organic movement.
    - **Bento Grid:** Information-dense, structured card layouts.
    - **Glassmorphism v2:** High blur, saturated backgrounds, tactile borders.

## Structural Integrity
- **TREEMAP.md:** Non-negotiable hierarchical map of the dev environment.
- **CP_STRUCTURE.md:** Non-negotiable gate between prep and build.
- **Law:** FUNCTION OVER EVERYTHING. Style follows structure.

## Sitemap Template
| Page | Path | Template | Priority |
| :--- | :--- | :--- | :--- |
| Home | / | Hero + Features + CTA | Critical |
| About | /about | Story + Team + Values | High |
| Services | /services | Service cards + CTAs | High |
| Contact | /contact | Form + Map + Details | Medium |
| Blog | /blog | Post list + Categories | Medium |
| Privacy | /privacy | Legal text | Required |
| Terms | /terms | Legal text | Required |

## SEO Checklist
- [ ] Unique title tag per page (<60 chars)
- [ ] Meta description per page (<155 chars)
- [ ] H1 on every page (one per page)
- [ ] Alt text on all images
- [ ] sitemap.xml generated
- [ ] robots.txt configured
- [ ] Schema markup (Organization, LocalBusiness, BreadcrumbList)
- [ ] Open Graph tags for social sharing
- [ ] Canonical URLs set

## Performance Budget
| Metric | Target | Tool |
| :--- | :--- | :--- |
| Largest Contentful Paint | <2.5s | Lighthouse |
| First Input Delay | <100ms | Lighthouse |
| Cumulative Layout Shift | <0.1 | Lighthouse |
| Total page weight | <500KB | DevTools |
| Image formats | WebP/AVIF | Build tool |

## Analytics Setup
- [ ] Google Analytics 4 (or privacy-friendly alternative)
- [ ] Google Search Console
- [ ] Event tracking for CTAs
- [ ] Conversion goals defined
- [ ] 404 error tracking

## Content Hierarchy Pattern
Each page should follow this hierarchy:
1. **Hero Section** — Primary message + CTA (above the fold)
2. **Social Proof** — Logos, testimonials, or stats
3. **Value Proposition** — 3–4 cards/columns explaining benefits
4. **Deep Content** — Detailed descriptions, case studies, features
5. **Secondary CTA** — Repeat the primary CTA or introduce a softer one
6. **FAQ** — Address objections before they leave
7. **Footer** — Navigation, legal links, contact, social

## Responsive Breakpoints
| Breakpoint | Width | Target |
| :--- | :--- | :--- |
| Mobile | <640px | Single column, stacked layout |
| Tablet | 640px–1024px | Two column, simplified nav |
| Desktop | 1024px–1440px | Full layout |
| Large Desktop | >1440px | Max-width container, centred |

**Mobile-first rule:** Start with mobile layout, progressively enhance for larger screens.

## Image Strategy
- **Hero images:** WebP, max 200KB, lazy-load below fold
- **Thumbnails:** WebP, max 30KB, eager-load if above fold
- **Icons:** SVG inline or sprite sheet
- **Responsive images:** Use `<picture>` element with `srcset` for 1x/2x/3x
- **No layout shift:** Always set `width` and `height` attributes

## Cookie Consent (GDPR/PECR)
- [ ] Cookie consent banner implemented (prior blocking)
- [ ] Analytics only fires after consent
- [ ] Categories: Necessary / Analytics / Marketing
- [ ] Consent stored and retrievable
- [ ] Reject button equally prominent as Accept
- [ ] Cookie policy page linked from banner

## 1. Project Initialization & Architecture Rules

### 1.1 The "Clean Handoff" Protocol
When requested to build a new Website, the AI MUST explicitly establish a sterile boundary:
- All new code goes into a pristine `project/` directory.
- This directory must contain NO Dev Panel or Instructional files. It must be a mathematically pure web skeleton, ready to be handed directly to a client or hosted.

### 1.3 Execution Paths & Modes
The exact trajectory of the project is defined by the Execution Mode selected by the user in `PROMPTER.md`:
- **Architect's Sequence:** The full, heavy-weight 5-Phase lifecycle from Market Audit to Post-Launch Maintenance.
- **Maestro Mode (Skip to Design):** Bypasses Market Audits but strictly adheres to all Structural, Database, and Verification gates.
- **Maintenance Mode:** Bypasses Pre-Production entirely. Operates exclusively via modifying the `project/database/cms/` file (The "CMS-First Mandate") and localization of plugins.
- **Demo Mode (UI Showcase):** A pure frontend rapid-prototyping pathway. The AI MUST skip `02_SEO_INTENT`, `01_SEO_PAGE_SPEED`, and `02.5_TRACKING_AND_SCHEMA`. It generates only the `project/database/cms/` (for colors/fonts), and immediately scaffolds the raw React/HTML/CSS for rapid visual approval.

## Pre-Launch Checklist
- [ ] All pages render correctly on mobile, tablet, desktop
- [ ] All links work (no 404s)
- [ ] All forms submit correctly
- [ ] Favicon and touch icons set
- [ ] 404 page designed
- [ ] SSL certificate active
- [ ] Redirects configured (www → non-www or vice versa)
- [ ] Page speed ≥90 on Lighthouse
- [ ] Accessibility ≥90 on Lighthouse
- [ ] Social sharing preview (OG tags) tested
- [ ] **Guardian Gate:** Full `SECURITY.xml` audit passed with 0 critical issues.
