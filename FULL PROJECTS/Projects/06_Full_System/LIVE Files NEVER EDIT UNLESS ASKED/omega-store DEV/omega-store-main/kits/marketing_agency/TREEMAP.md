# Marketing Agency: Meta-Kit Architecture

**Version:** V16.30
**Purpose:** The umbrella framework for full-stack agency fulfillment. An agency provides websites, SEO, and ongoing maintenance. Therefore, this Meta-Kit houses those specific operational Sub-Kits.

## Fractal Structure
```text
marketing_agency/
├── website/                            # Sub-Kit: Core Website Design & Execution
│   ├── TREEMAP.md                      # [Website Architecture Map](file:///Users/eds/Documents/Omega%20Constitution%20Pack/Omega%20DEV%20Panel/06_Full_System/omega-store/kits/marketing_agency/website/TREEMAP.md)
│   ├── WEBSITE_KIT.md                  # Project boundaries & laws
│   └── PROMPTER.md                     # Client discovery sequence
└── seo_campaigns/                      # (Future) Local/National SEO scaling
```

## How It Works
When a user begins a "Marketing Agency" project, the AI recognizes this is a *Meta-Kit*. It will then ask what specific fulfillment is needed first (e.g., "Do you need the Website built first, or an SEO campaign?"). It will then route the user into the nested `website/` kit to execute the build.
