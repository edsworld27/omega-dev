# DEPENDENCIES — TaskFlow

**Status:** Pending approval at CP-5  
**Policy:** DEPENDENCY_POLICY.md (Install Gate)

---

## Runtime Dependencies

| Package | Version | Rationale | Usage | Risk |
| :--- | :--- | :--- | :--- | :--- |
| next | 14.2.x | Core framework | Entire app | Low — maintained by Vercel |
| react | 18.3.x | UI library | Entire app | Low — industry standard |
| react-dom | 18.3.x | React DOM renderer | Entire app | Low — paired with React |
| @supabase/supabase-js | 2.x | Database + auth client | API routes, auth | Low — official Supabase SDK |
| @prisma/client | 5.x | Type-safe database queries | API routes | Low — widely used ORM |

## Development Dependencies

| Package | Version | Rationale | Usage | Risk |
| :--- | :--- | :--- | :--- | :--- |
| typescript | 5.x | Type safety | Entire codebase | Low |
| tailwindcss | 3.x | Styling | All components | Low |
| prisma | 5.x | Schema management, migrations | Dev workflow | Low |
| vitest | 1.x | Unit/integration testing | Test suite | Low |
| @testing-library/react | 14.x | Component testing | Test suite | Low |
| eslint | 8.x | Code quality | CI/CD | Low |
| prettier | 3.x | Code formatting | CI/CD | Low |

## Rejected Packages

| Package | Why Rejected |
| :--- | :--- |
| zustand | React Context is sufficient for this app's state complexity |
| framer-motion | Animation library — deferred to v2 polish phase |
| @tanstack/query | Supabase client handles caching already |

## Total: 5 runtime, 7 dev dependencies
