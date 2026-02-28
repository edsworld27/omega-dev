# TASK: Accessibility Implementation
**Kit:** Website
**Phase:** Production
**Portable:** Yes

---

## FOR THE USER

This task ensures your website is accessible to all users.

Target: WCAG 2.1 Level AA compliance, Lighthouse Accessibility score 90+.

Tell your AI: **"Execute ACCESSIBILITY.task.md"**

---

## FOR THE AI

### CONTEXT
Implement accessibility best practices throughout the website. This is a functional requirement, not optional polish.

### STEPS

1. **Audit current state**
   - Run Lighthouse accessibility audit
   - Check for axe DevTools issues (if available)
   - Note current score and issues

2. **Semantic HTML**
   - Ensure one `<h1>` per page
   - Heading hierarchy is logical (h1 → h2 → h3)
   - Use semantic elements: `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`
   - Use `<button>` for actions, `<a>` for navigation
   - Lists use `<ul>`, `<ol>`, `<li>`

3. **Keyboard navigation**
   - All interactive elements focusable
   - Tab order is logical
   - Focus states are visible
   - Skip-to-content link at top
   - No keyboard traps
   - Escape closes modals

4. **Screen reader support**
   - Alt text on meaningful images
   - `alt=""` on decorative images
   - `aria-label` where needed
   - Form inputs have `<label>` elements
   - Error messages are announced
   - Live regions for dynamic content

5. **Visual accessibility**
   - Color contrast 4.5:1 for normal text
   - Color contrast 3:1 for large text
   - Don't rely on color alone
   - Text resizable to 200%
   - No horizontal scroll at 320px width

6. **Motion and media**
   - Respect `prefers-reduced-motion`
   - No auto-playing media with sound
   - Video has captions (if applicable)
   - Animations can be paused

### OUTPUT

```
ACCESSIBILITY IMPLEMENTATION COMPLETE

Before:
- Lighthouse Accessibility: [X/100]
- Issues found: [X]

After:
- Lighthouse Accessibility: [X/100]
- Issues remaining: [X]

Fixes applied:
- [x] Semantic HTML corrected
- [x] Keyboard navigation working
- [x] Alt text added to images
- [x] Color contrast fixed
- [x] Focus states visible
- [etc.]

Manual testing needed:
- [ ] Screen reader walkthrough
- [ ] Keyboard-only navigation test
- [ ] Zoom to 200% test

Files modified:
- [List of files]
```

### SUCCESS CRITERIA
- [ ] Lighthouse Accessibility score 90+
- [ ] All images have appropriate alt text
- [ ] Keyboard navigation works throughout
- [ ] Color contrast passes
- [ ] Forms are properly labeled
- [ ] Skip link present
