# TASK: Lighthouse Audit
**Kit:** Website
**Phase:** Testing
**Portable:** Yes

---

## FOR THE USER

This task runs a Lighthouse audit and addresses any issues.

Target scores: 90+ in all categories.

Tell your AI: **"Execute LIGHTHOUSE.task.md"**

---

## FOR THE AI

### CONTEXT
Run Lighthouse audit on the website and fix issues to achieve 90+ scores in Performance, Accessibility, Best Practices, and SEO.

### STEPS

1. **Run Lighthouse**
   - If you can access browser tools, run Lighthouse
   - Otherwise, instruct user to run and share results
   - Test on mobile and desktop

2. **Document current scores**
   - Performance: X/100
   - Accessibility: X/100
   - Best Practices: X/100
   - SEO: X/100

3. **Analyze issues by category**

   **Performance issues:**
   - LCP (Largest Contentful Paint)
   - CLS (Cumulative Layout Shift)
   - TBT (Total Blocking Time)
   - Image optimization
   - Unused JavaScript/CSS

   **Accessibility issues:**
   - Missing alt text
   - Color contrast
   - Missing form labels
   - Heading order
   - Focus management

   **Best Practices issues:**
   - HTTPS usage
   - Console errors
   - Deprecated APIs
   - Image aspect ratios

   **SEO issues:**
   - Missing meta descriptions
   - Missing titles
   - Crawlability
   - Mobile friendliness

4. **Fix issues**
   - Address each issue
   - Re-run Lighthouse after fixes
   - Document improvements

### OUTPUT

```
LIGHTHOUSE AUDIT COMPLETE

Initial scores:
| Category | Score |
|----------|-------|
| Performance | X |
| Accessibility | X |
| Best Practices | X |
| SEO | X |

Issues found and fixed:
- [Issue 1]: [Fix applied]
- [Issue 2]: [Fix applied]
- [etc.]

Final scores:
| Category | Score |
|----------|-------|
| Performance | X |
| Accessibility | X |
| Best Practices | X |
| SEO | X |

Remaining issues (if any):
- [Issues that couldn't be fixed automatically]

Recommendations:
- [Further improvements]
```

### SUCCESS CRITERIA
- [ ] All categories score 90+
- [ ] No critical accessibility issues
- [ ] No console errors
- [ ] Core Web Vitals passing
