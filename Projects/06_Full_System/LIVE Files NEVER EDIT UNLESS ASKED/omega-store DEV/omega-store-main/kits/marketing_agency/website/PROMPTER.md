# WEBSITE KIT — PROMPTER

**Purpose:** This file tells the AI how to gather requirements and ensure nothing is missed when building a website project.

**Authority:** Constitution > This Prompter > kit.config.md > WEBSITE_KIT.md patterns

---

## 1. ACTIVATION GATE

Before using this kit, verify:
- [ ] Constitution loaded (SECURITY.xml, QUALITY.xml, PROMPTING.xml, etc.)
- [ ] PROJECT.md read (user-input/seed/)
- [ ] Project type = Website confirmed
- [ ] plug-and-play/ scanned for existing assets

If any constitution file is missing → HALT. Load constitution first.

---

## 2. REQUIREMENTS TABLE

**Every row must have a value before build begins. If blank, AI must ask.**

| Requirement | Source | Status | Notes |
|:------------|:-------|:-------|:------|
| Project name | PROJECT.md | [ ] | |
| North star (singular goal) | PROJECT.md | [ ] | |
| Target audience | PROJECT.md or PERSONAS.md | [ ] | |
| Site type (Marketing / Blog / E-commerce / Portfolio) | PROJECT.md | [ ] | |
| Page count estimate | CONTENT.md or ask | [ ] | |
| Content ready? | Ask or plug-and-play/ | [ ] | Yes/No/Partial |
| Brand guidelines exist? | BRAND.md or plug-and-play/ | [ ] | |
| Tech stack decision | TECH_STACK.md or ask | [ ] | |
| Hosting preference | PROJECT.md or ask | [ ] | |
| Domain name | Ask | [ ] | |
| Analytics tool | Ask (default: GA4) | [ ] | |
| Cookie consent needed? | Ask (default: Yes if EU) | [ ] | |
| Launch deadline | CONSTRAINTS.md or ask | [ ] | |
| Budget tier | CONSTRAINTS.md or ask | [ ] | £0 / £500 / £5k+ |

---

## 3. DISCOVERY SEQUENCE

Use PROMPTING.xml methods. Ask in batches of 2-4 questions max.

### Batch 1: Core Identity
```
I've loaded your project seeds. Let me confirm a few things:

1. **Site type:** Is this primarily:
   - Marketing/Landing page
   - Blog/Content site
   - E-commerce/Shop
   - Portfolio/Showcase
   - Other (describe)

2. **Scale:** How many pages do you expect?
   - Small (1-5 pages)
   - Medium (6-15 pages)
   - Large (15+ pages)
```

### Batch 2: Content Status
```
About your content:

1. **Do you have existing content** (copy, images, brand assets)?
   - Yes, it's ready → Drop into plug-and-play/ or tell me the path
   - Partial — I have some
   - No — starting from scratch

2. **Brand guidelines?**
   - Yes (colors, fonts, logo defined)
   - No — need to establish
```

### Batch 3: Technical Preferences
```
### 4. Tech Stack, Integrations & Routing ⚙️
1. **Framework Preferences:** Are we using a specific framework (Next.js, Vite, HTML/CSS) or do I have autonomy to choose the best fit?
2. **CMS/CRM Needs:** Will this site require a backend CMS (Sanity, WordPress headless) or Webhooks for a CRM (HubSpot, GoHighLevel)?
3. **Integrations & Plugins:** Are there any specific third-party integrations required (e.g., Stripe, Calendly, Mailchimp, Live Chat)?
4. **Fulfillment Routing:** Shall I generate the code locally in the IDE, or do you want me to generate prompts for an external AI Native Builder (e.g., Lovable, v0) and then audit the result?ext
```

### Batch 4: Launch Context
```
Final context:

1. **Launch deadline?** (date or "no rush")

2. **Any specific integrations needed?**
   - Contact form → where do submissions go?
   - Newsletter signup → which provider?
   - E-commerce → Stripe? Shopify?
   - CMS for content editing?
```

---

### Batch 5: 3D & Animation (Optional)
```
If we are activating 3D Scrollytelling Mode:

1. **Do you have your 120-frame sequence ready?**
   - Yes, in /public/sequence/
   - I need to generate it based on a Start/End frame blueprint
   - No, let's use a placeholder

2. **Start/End Specifications:**
   - Have you defined the 'Assembled' vs 'Exploded' components?
   - Is your background locked to #050505 for the seamless void?
```

---

### Batch 6: UI/UX Pro Max Dimensions (Visual DNA)
```
Before we build the UI, we must define its 5 Core Dimensions:

1. **SKELETON (Pattern/Layout):** Which pattern fits your goal? 
   - SaaS (Feature-heavy) / Portfolio (Story-telling) / E-comm (Luxury) / Crypto (Trust & Data)
2. **SKIN (Style/Aesthetic):** What is the visual 'feel'?
   - Glassmorphism / Aurora UI / Linear / Brutalist / Liquid Glass
3. **PALETTE (Color):** What is the emotional mood?
   - Trust (Navy/Slate) / Vibrant (Indigo/Emerald) / luxury (Gold/Stone) / Dark Mode
4. **VOICE (Typography):** Select a brand voice:
   - Modern Tech / Elegant Luxury / Friendly / Brutalist Bold
5. **SOUL (Interaction):** Any specific animation preferences? 
   - 3D Scrollytelling / Micro-interactions / Fade-Stagger / Scroll Reveal
```

---

## 4. EVALUATION MATRIX

After discovery, score the project against WEBSITE_KIT.md requirements:

| Category | Required Items | Status |
|:---------|:---------------|:-------|
| **Pages** | Home, About, Contact minimum | [ ] |
| **SEO** | Title, meta, H1, alt text, sitemap, robots.txt | [ ] |
| **Performance** | LCP <2.5s, FID <100ms, CLS <0.1 | [ ] |
| **Accessibility** | Lighthouse ≥90 | [ ] |
| **Mobile** | Responsive breakpoints defined | [ ] |
| **Legal** | Privacy policy, Terms, Cookie consent | [ ] |
| **Analytics** | Tracking code, events, goals | [ ] |
| **Security** | SSL, headers, form validation | [ ] |

---

## 5. BUILD HANDOFF

Next Steps:
Based on the answers above, the AI will:
1. **Generate sitemap** from WEBSITE_KIT.md template + user input
2. **Create component list** for tech stack
3. **Output PRD** using constitution/blueprints/PRD.md
4.- **"Begin Architect's Sequence"**: Start from Pre-Production Document 1 and work sequentially. No code generation until Pre-Production is fully approved.
- **"Maestro Mode (Skip to Design)"**: Bypass the market audit and instantly generate the `TREEMAP.md`, `project/database/cms/site.config`, and `CP_STRUCTURE.md` to begin immediate structural coding. (Subject to Mobile-First and Container Laws).
- **"Maintenance Mode"**: Re-open a completed project to execute Phase 5 protocols (Blogs, Text Edits, Plugin Integrations via the Hot Swap CMS file).
- **"Demo Mode (UI Showcase)"**: Bypass all SEO, Schema, and heavy backend discovery. Generate only the Aesthetic Layer (Hot Swap Colors/Fonts) and immediately jump to scaffolding a pure frontend layout (HTML/React) for rapid structural approval.

---

## 6. NOTHING LEFT BEHIND

Before ANY code is written, this prompter ensures:
- Every seed gap is filled by asking
- Every kit requirement is evaluated
- Every constitution rule is respected
- Every deliverable is tracked

**If a requirement is unclear → ASK. Never assume.**

---

## 7. KIT-SPECIFIC PROMPTING RULES

From PROMPTING.xml, apply to website context:

1. **Visual proposals:** Describe layouts before building (Hero: full-width image, centered headline...)
2. **Chunked delivery:** Build page-by-page, not all at once
3. **Checkpoint after each page:** "Home page complete. Review before I continue?"
4. **No placeholder content:** Real copy or clear [PLACEHOLDER: describe what goes here]
5. **Mobile-first always:** Start with mobile layout in all component descriptions

---

*This prompter auto-activates when kit.config.md conditions are met.*
