# TASK: Cross-Browser Testing
**Kit:** Website
**Phase:** Testing
**Portable:** Yes

---

## FOR THE USER

This task tests your website across different browsers.

You'll need to test in actual browsers. The AI will guide you through what to check.

Tell your AI: **"Execute BROWSER.task.md"**

---

## FOR THE AI

### CONTEXT
Guide the user through cross-browser testing. Identify browser-specific issues and provide fixes.

### STEPS

1. **Define browsers to test**

   **Desktop (latest versions):**
   - Chrome
   - Safari
   - Firefox
   - Edge

   **Mobile:**
   - Safari (iOS)
   - Chrome (Android)

2. **Create test checklist per browser**

   For each browser, verify:
   - [ ] Page loads without errors
   - [ ] Layout matches design
   - [ ] Fonts render correctly
   - [ ] Images display properly
   - [ ] Animations work
   - [ ] Forms function correctly
   - [ ] Navigation works
   - [ ] No console errors
   - [ ] Hover states work (desktop)
   - [ ] Touch events work (mobile)

3. **Document results**
   - Note any visual differences
   - Note any functional issues
   - Screenshot issues if possible

4. **Common browser issues to check**
   - Safari: Flexbox gaps, date inputs, smooth scroll
   - Firefox: Form styling, scrollbar styling
   - Edge: Legacy Edge fallbacks (if supporting)
   - iOS Safari: 100vh issue, fixed positioning, zoom on input

5. **Provide fixes**
   - CSS prefixes where needed
   - Polyfills for missing features
   - Browser-specific workarounds

### OUTPUT

```
CROSS-BROWSER TESTING COMPLETE

Test matrix:
| Browser | Version | Status | Issues |
|---------|---------|--------|--------|
| Chrome | 120 | ✓ Pass | None |
| Safari | 17 | ⚠ Issues | Flexbox gap |
| Firefox | 121 | ✓ Pass | None |
| Edge | 120 | ✓ Pass | None |
| iOS Safari | 17 | ⚠ Issues | 100vh |
| Android Chrome | 120 | ✓ Pass | None |

Issues found and fixes:
| Browser | Issue | Fix |
|---------|-------|-----|
| Safari | Flexbox gap not supported | Added margin fallback |
| iOS Safari | 100vh includes address bar | Used dvh unit |
| [etc.] | | |

CSS added for compatibility:
- [List of CSS changes]

Remaining issues (unfixable):
- [Any issues that can't be fixed]
```

### SUCCESS CRITERIA
- [ ] Works in all major desktop browsers
- [ ] Works in iOS Safari
- [ ] Works in Android Chrome
- [ ] No console errors in any browser
- [ ] Core functionality works everywhere
