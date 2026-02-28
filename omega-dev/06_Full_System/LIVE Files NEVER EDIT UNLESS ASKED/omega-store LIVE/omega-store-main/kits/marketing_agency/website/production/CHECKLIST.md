# WEBSITE PRODUCTION CHECKLIST

Build in this order. Function before UX before Form.

---

## PHASE 1: STRUCTURE (Function)
- [ ] Project scaffolded (framework set up)
- [ ] Routing configured
- [ ] Sitemap structure created
- [ ] Base layouts built
- [ ] Data fetching working (if CMS/API)

---

## PHASE 2: CORE PAGES (Function)
- [ ] Homepage — structure and content
- [ ] About page
- [ ] Contact page (form working)
- [ ] [Other core pages]

---

## PHASE 3: COMPONENTS (Function → UX)
- [ ] Navigation — working links, mobile menu
- [ ] Footer — links, legal
- [ ] Forms — validation, submission
- [ ] CTAs — actions work

---

## PHASE 4: SEO & META (Function)
Run: `SEO.task.md`
- [ ] Meta titles per page
- [ ] Meta descriptions per page
- [ ] Open Graph tags
- [ ] Twitter cards
- [ ] Sitemap.xml
- [ ] Robots.txt
- [ ] Canonical URLs

---

## PHASE 5: PERFORMANCE (UX)
Run: `PERFORMANCE.task.md`
- [ ] Images optimized (WebP, lazy loading)
- [ ] Fonts optimized (subset, preload)
- [ ] CSS/JS minified
- [ ] Caching configured
- [ ] Core Web Vitals passing

---

## PHASE 6: ACCESSIBILITY (UX)
Run: `ACCESSIBILITY.task.md`
- [ ] Semantic HTML throughout
- [ ] Keyboard navigation works
- [ ] Screen reader tested
- [ ] Color contrast passing
- [ ] Focus states visible
- [ ] Alt text on images
- [ ] Form labels present

---

## PHASE 7: STYLING (Form)
- [ ] Brand colors applied
- [ ] Typography consistent
- [ ] Spacing system applied
- [ ] Responsive breakpoints
- [ ] Dark mode (if applicable)

---

## WHEN COMPLETE

Move to Testing phase:
```
testing/CHECKLIST.md
```
