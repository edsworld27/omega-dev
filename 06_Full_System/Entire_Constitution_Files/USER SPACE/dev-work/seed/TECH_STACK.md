# TECH STACK — TECHNOLOGY SEED

**Purpose:** Plug-and-play technology decisions. Centralises all tech choices so the agent knows exactly what to build with. Swap this between projects.

**If blank:** The agent proposes a stack at CP-1 based on your CONTEXT.md constraints.

---

## 1. Paradigm
- [ ] **Path A: Application** (Logic First) — Function = Backend/Schema/API
- [ ] **Path B: Website** (Content First) — Function = Content/Sitemap/SEO

## 2. Frontend
- **Framework:** (e.g., Next.js 14 / React / Vue / Astro / None)
- **Styling:** (e.g., Tailwind CSS / CSS Modules / Styled Components)
- **Component Library:** (e.g., shadcn/ui / Radix / None)
- **State Management:** (e.g., Zustand / Redux / Context API / None)

## 3. Backend
- **Runtime:** (e.g., Node.js 20 / Python 3.12 / Go)
- **Framework:** (e.g., Express / FastAPI / Hono / None)
- **ORM:** (e.g., Prisma / Drizzle / SQLAlchemy / None)

## 4. Database
- **Primary:** (e.g., PostgreSQL / Supabase / Firebase / MongoDB)
- **Cache:** (e.g., Redis / None)
- **File Storage:** (e.g., S3 / Supabase Storage / Cloudflare R2 / None)

## 5. Authentication
- **Provider:** (e.g., Supabase Auth / NextAuth / Clerk / Custom)
- **Methods:** (e.g., Email/Password, OAuth, Magic Link)

## 6. Hosting & Deployment
- **Frontend:** (e.g., Vercel / Netlify / VPS)
- **Backend:** (e.g., Railway / VPS / AWS Lambda)
- **CI/CD:** (e.g., GitHub Actions / GitLab CI / None yet)

## 7. Third-Party Services
| Service | Purpose | Auth Method |
| :--- | :--- | :--- |
| (e.g., Stripe) | (Payments) | (API Key in .env) |
| (e.g., Resend) | (Email) | (API Key in .env) |

## 8. AI / Automation (If applicable)
- **AI Provider:** (e.g., Anthropic / OpenAI / Local models)
- **Orchestration:** (e.g., n8n / LangChain / Custom)
- **MCP Servers:** (See `store/mcps/MCP_CONFIG.md` or your `USER SPACE/dev-work/plug-and-play/mcps/`)

## 9. Development Tools
- **Package Manager:** (e.g., pnpm / npm / yarn)
- **Linting:** (e.g., ESLint + Prettier / Ruff)
- **Testing:** (e.g., Vitest / Jest / Pytest)
- **Version Control:** (e.g., Git + GitHub / GitLab)
