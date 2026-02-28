# TASK: Mobile Responsiveness Testing
**Kit:** Website
**Phase:** Testing
**Portable:** Yes

---

## FOR THE USER

This task tests your website across mobile and tablet devices.

Tell your AI: **"Execute MOBILE.task.md"**

If you can share screenshots at different breakpoints, that helps.

---

## FOR THE AI

### CONTEXT
Test the website's responsiveness across common device sizes. Identify and fix layout issues.

### STEPS

1. **Define test breakpoints**
   - 320px (small mobile)
   - 375px (iPhone SE/Mini)
   - 390px (iPhone 14)
   - 428px (iPhone 14 Pro Max)
   - 768px (iPad)
   - 1024px (iPad Pro)
   - 1280px (laptop)
   - 1440px+ (desktop)

2. **Test each page at each breakpoint**
   Check for:
   - Text overflow or truncation
   - Images breaking layout
   - Horizontal scrolling (should not happen)
   - Touch targets too small (<44px)
   - Overlapping elements
   - Hidden content that should be visible
   - Navigation accessibility

3. **Test mobile-specific features**
   - Mobile menu opens/closes
   - Mobile menu is scrollable if long
   - Tap actions work (no hover-only)
   - Forms are usable (inputs not too small)
   - Buttons are tappable

4. **Test orientation**
   - Portrait mode works
   - Landscape mode works
   - Rotation doesn't break layout

5. **Fix issues found**
   - Adjust CSS breakpoints
   - Fix overflow issues
   - Resize touch targets
   - Fix navigation

### OUTPUT

```
MOBILE TESTING COMPLETE

Pages tested:
- Homepage
- About
- Contact
- [etc.]

Breakpoints tested:
- 320px: [Pass/Issues]
- 375px: [Pass/Issues]
- 768px: [Pass/Issues]
- [etc.]

Issues found and fixed:
| Page | Breakpoint | Issue | Fix |
|------|------------|-------|-----|
| Homepage | 320px | Hero text overflow | Reduced font size |
| Contact | 375px | Form too wide | Added padding |
| [etc.] | | | |

Mobile features:
- [x] Mobile menu works
- [x] Touch targets adequate
- [x] Forms usable
- [x] No horizontal scroll

Remaining issues:
- [Any issues that need manual fix]
```

### SUCCESS CRITERIA
- [ ] No horizontal scrolling at any breakpoint
- [ ] All touch targets 44px or larger
- [ ] Mobile navigation works
- [ ] All text readable without zooming
- [ ] Forms usable on mobile
