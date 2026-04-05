# ⚫ Deploying on GitHub Pages

GitHub Pages is perfect for simple projects, documentation, and portfolios hosted directly from your repository.

## Step 1: Prepare Your Repository

Make sure your project is ready:
- Code pushed to a GitHub repository
- Static HTML/CSS/JS or built framework output
- Repository can be public or private (with Pro)

## Step 2: Enable GitHub Pages

### Option A: From Root Directory

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in left sidebar)
3. Under "Source", select branch:
   - **Branch**: `main` or `master`
   - **Folder**: `/ (root)`
4. Click **Save**
5. Wait for deployment (usually 1-2 minutes)

### Option B: From /docs Folder

1. Create a `docs` folder in your repository
2. Put your HTML files in the `docs` folder
3. Go to Settings → Pages
4. Select:
   - **Branch**: `main` or `master`
   - **Folder**: `/docs`
5. Click **Save**

### Option C: Using GitHub Actions (For Build Processes)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build
      
      - name: Setup Pages
        uses: actions/configure-pages@v3
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: './dist'
      
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

## Step 3: Get Your GitHub Pages URL

Your site will be available at:
```
username.github.io
```
or
```
username.github.io/repository-name
```

You can find this in:
- Settings → Pages → Your site is live at...

**Test it:** Visit your GitHub Pages URL to ensure it's working.

## Step 4: Configure Custom Domain (After PR Approval)

Once your PR is approved and DNS is configured:

### Method 1: Via Repository Settings

1. Go to your repository Settings → Pages
2. Under "Custom domain", enter: `yourname.iths.online`
3. Click **Save**
4. GitHub will create a `CNAME` file in your repository
5. Check "Enforce HTTPS" (wait for SSL certificate)

### Method 2: Via CNAME File

1. Create a file named `CNAME` in your repository root (or docs folder)
2. Add your domain:
   ```
   yourname.iths.online
   ```
3. Commit the file
4. Go to Settings → Pages
5. Verify the custom domain appears
6. Enable "Enforce HTTPS"

## Step 5: Create Your Domain Configuration

Create a JSON file for your PR:

```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "username.github.io",
  "owner": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "github": "your-github-username"
  },
  "project": {
    "name": "My Portfolio",
    "description": "Personal portfolio hosted on GitHub Pages",
    "url": "https://github.com/username/repo"
  }
}
```

**Note:** If your site is at `username.github.io/repo-name`, you may need to use an `A` record instead. Contact us for assistance.

## 🎯 GitHub Pages-Specific Tips

### For Jekyll Sites
GitHub Pages has native Jekyll support:
- Add `_config.yml` to your repository
- Use Jekyll themes
- Automatic builds on push

### Base Path Issues
If your site is in a subdirectory (`username.github.io/repo`):
- Set base URL in your framework config
- Use relative paths for assets
- Or use a custom domain to avoid this issue

### Custom 404 Page
Create a `404.html` file in your root:
```html
<!DOCTYPE html>
<html>
<head>
  <title>404 - Page Not Found</title>
</head>
<body>
  <h1>Page not found</h1>
  <a href="/">Go home</a>
</body>
</html>
```

### Repository Structure Examples

**Simple HTML Site:**
```
repo/
├── index.html
├── style.css
├── script.js
└── images/
```

**Jekyll Site:**
```
repo/
├── _config.yml
├── _posts/
├── index.md
└── about.md
```

**Built Framework (React, Vue, etc.):**
```
repo/
├── src/
├── package.json
├── dist/ (or build/)
└── .github/workflows/deploy.yml
```

## ⚠️ Common Issues

### Issue: 404 Errors
**Solution:** 
- Check file paths are correct
- Ensure `index.html` exists in root
- Verify deployment completed successfully

### Issue: Assets Not Loading
**Solution:**
- Use relative paths for CSS/JS/images
- Check browser console for errors
- Ensure files are committed to repository

### Issue: Custom Domain Not Working
**Solution:**
- Verify CNAME file exists and is correct
- Check DNS propagation
- Ensure "Enforce HTTPS" is enabled
- Wait up to 24 hours for SSL certificate

### Issue: Build Fails (for Jekyll)
**Solution:**
- Check `_config.yml` syntax
- Verify gem dependencies
- Review build logs in Actions tab

## ✅ Checklist Before Submitting PR

- [ ] GitHub Pages enabled in repository settings
- [ ] Site is accessible at username.github.io
- [ ] Website loads without errors
- [ ] All assets (images, CSS, JS) load correctly
- [ ] No console errors in browser
- [ ] CNAME file added (if using custom domain)
- [ ] HTTPS enabled
- [ ] Content is appropriate and complete

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Jekyll on GitHub Pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)
- [GitHub Actions for Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## 🆘 Need Help?

- Check GitHub's [Pages documentation](https://docs.github.com/en/pages)
- Visit [GitHub Community](https://github.community)
- Open an issue in this repository

---

Ready to submit? Follow the [Getting Started Guide](getting-started.md) to create your PR!
