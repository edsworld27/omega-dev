# TASK: SEO Setup
**Kit:** Website
**Phase:** Production
**Portable:** Yes

---

## FOR THE USER

This task configures SEO for your website.

Prerequisites:
- Pages exist (at least in draft form)
- You have target keywords (or want AI to suggest them)

Tell your AI: **"Execute SEO.task.md"**

---

## FOR THE AI

### CONTEXT
Set up comprehensive SEO for the website. This includes meta tags, technical SEO, and content optimization.

### STEPS

1. **Audit current state**
   - Check which pages exist
   - Check current meta tags (if any)
   - Check for sitemap.xml and robots.txt

2. **Generate meta tags per page**
   For each page, create:
   - Title tag (50-60 characters, keyword + brand)
   - Meta description (150-160 characters, compelling + keyword)
   - Open Graph tags (og:title, og:description, og:image)
   - Twitter card tags

3. **Technical SEO**
   - Generate sitemap.xml with all pages
   - Create robots.txt (allow all, reference sitemap)
   - Set up canonical URLs
   - Check for proper heading hierarchy (one H1 per page)

4. **Content recommendations**
   - Suggest internal linking opportunities
   - Flag thin content pages
   - Suggest alt text for images

### OUTPUT

```
SEO SETUP COMPLETE

Meta tags created for:
- Homepage: "Title here" | "Description here"
- About: "Title here" | "Description here"
- [etc.]

Technical SEO:
- [x] sitemap.xml created at /sitemap.xml
- [x] robots.txt created
- [x] Canonical URLs set

Recommendations:
- [Content improvements]
- [Internal linking opportunities]
- [Missing elements]

Files created/modified:
- [List of files]
```

### SUCCESS CRITERIA
- [ ] Every page has unique title and description
- [ ] Open Graph tags present for social sharing
- [ ] sitemap.xml exists and is valid
- [ ] robots.txt exists
- [ ] No duplicate titles or descriptions
