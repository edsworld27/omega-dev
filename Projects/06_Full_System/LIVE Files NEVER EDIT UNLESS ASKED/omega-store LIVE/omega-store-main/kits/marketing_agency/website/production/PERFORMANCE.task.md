# TASK: Performance Optimization
**Kit:** Website
**Phase:** Production
**Portable:** Yes

---

## FOR THE USER

This task optimizes your website's performance.

Prerequisites:
- Site is functional (pages load)
- Content and images are in place

Tell your AI: **"Execute PERFORMANCE.task.md"**

---

## FOR THE AI

### CONTEXT
Optimize the website for Core Web Vitals and fast loading. Target: Lighthouse Performance score 90+.

### STEPS

1. **Audit current performance**
   - Run Lighthouse (or note if user should run it)
   - Identify largest contentful paint (LCP) element
   - Check for layout shifts (CLS)
   - Check interaction delays (INP/FID)

2. **Image optimization**
   - Convert images to WebP/AVIF
   - Add width/height attributes (prevents CLS)
   - Implement lazy loading for below-fold images
   - Use responsive images (srcset)
   - Compress without visible quality loss

3. **Font optimization**
   - Subset fonts to used characters
   - Use font-display: swap
   - Preload critical fonts
   - Consider system font stack for body text

4. **Code optimization**
   - Minify CSS and JavaScript
   - Remove unused CSS
   - Code-split JavaScript (load what's needed)
   - Defer non-critical scripts

5. **Caching and delivery**
   - Set cache headers for static assets
   - Use CDN if available
   - Enable compression (gzip/brotli)
   - Preconnect to external origins

### OUTPUT

```
PERFORMANCE OPTIMIZATION COMPLETE

Before:
- LCP: [X seconds]
- CLS: [X]
- Performance score: [X/100]

After:
- LCP: [X seconds]
- CLS: [X]
- Performance score: [X/100]

Optimizations applied:
- [x] Images converted to WebP
- [x] Lazy loading added
- [x] Fonts optimized
- [x] CSS/JS minified
- [etc.]

Recommendations for further improvement:
- [Additional suggestions]

Files modified:
- [List of files]
```

### SUCCESS CRITERIA
- [ ] Lighthouse Performance score 90+
- [ ] LCP under 2.5 seconds
- [ ] CLS under 0.1
- [ ] All images optimized
- [ ] No render-blocking resources
