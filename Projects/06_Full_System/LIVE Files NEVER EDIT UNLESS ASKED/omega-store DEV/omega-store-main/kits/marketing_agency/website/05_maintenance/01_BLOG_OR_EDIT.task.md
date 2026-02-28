# PROTOCOL 05: POST-LAUNCH MAINTENANCE & INTEGRATIONS (Phase 5)

*This protocol executes when the user initiates a project in "Maintenance Mode" (e.g., returning to a completed site to add a blog or change copy).*

## The "CMS First" Mandate
If the client requests copy, image, color, or structural data changes, the AI MUST **audit and edit the `project/database/cms/` config file FIRST**. 
- Do **NOT** dive straight into the raw frontend components (e.g., `src/components/Hero.tsx`) to change text.
- If the text is hardcoded in the frontend, the AI must refactor it to pull from the `site.config` file, therefore fixing the architecture while fulfilling the edit request.

## Objectives
- [ ] **Audit Request:** Determine if the request is a Content Edit, a Structural Addition (new page), or a Plugin Integration.
- [ ] **Content Edits:** Edit the `project/database/cms/site.config` file to update text, links, or image URLs.
- [ ] **Structural Additions (Blogs/Pages):** 
    - If adding a new page, ensure the new route is added to the Sitemap and the CMS config.
    - If adding a blog architecture, ensure MDX or the chosen CMS is correctly mapped and styled according to the `AESTHETIC_LAYER`.
- [ ] **Plugin Integrations:** If adding a new script (e.g., Calendly, Stripe, Intercom), download or configure the localized script inside `project/database/plugins/` and inject the initializer into the `<head>` or component.

## Evidence Required
- [ ] Exact diff of the `project/database/cms/` file edited.
- [ ] Confirmation that the frontend accurately reflects the CMS update without breaking responsive scaling (Mobile-First verification).
