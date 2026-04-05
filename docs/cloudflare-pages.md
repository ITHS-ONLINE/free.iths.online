# 🔶 Deploying on Cloudflare Pages

Cloudflare Pages offers fast global CDN, automatic SSL, and excellent performance.

## Step 1: Prepare Your Project

Ensure your project is ready:
- Static site or built framework output
- Code pushed to GitHub/GitLab
- Build command configured (if needed)

## Step 2: Deploy to Cloudflare Pages

### Via Cloudflare Dashboard

1. Go to [pages.cloudflare.com](https://pages.cloudflare.com)
2. Sign up/login with your Cloudflare account
3. Click "Create a project" → "Connect to Git"
4. Authorize Cloudflare to access your Git provider
5. Select your repository
6. Configure build settings:
   - **Project name**: Your project name
   - **Production branch**: `main` or `master`
   - **Build command**: e.g., `npm run build`
   - **Build output directory**: e.g., `dist`, `build`, `public`
7. Click "Save and Deploy"
8. Wait for deployment to complete

### Via Wrangler CLI

```bash
# Install Wrangler
npm install wrangler --save-dev

# Login to Cloudflare
npx wrangler login

# Deploy your project
npx wrangler pages deploy ./dist --project-name=your-project
```

## Step 3: Get Your Cloudflare Pages URL

After deployment, you'll get a URL like:
```
your-project.pages.dev
```

You can find this in:
- Cloudflare Pages Dashboard → Your Project

**Test it:** Visit `https://your-project.pages.dev` to ensure it's working.

## Step 4: Configure Custom Domain (After PR Approval)

Once your PR is approved and DNS is configured:

1. Go to Cloudflare Pages Dashboard
2. Select your project
3. Go to **Custom domains**
4. Click "Set up a custom domain"
5. Enter: `yourname.iths.online`
6. Click "Continue"
7. Cloudflare will automatically configure DNS
8. SSL certificate is provisioned automatically
9. Wait for activation (usually within minutes)

## Step 5: Create Your Domain Configuration

Create a JSON file for your PR:

```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.pages.dev",
  "owner": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "github": "your-github-username"
  },
  "project": {
    "name": "My Portfolio",
    "description": "Personal portfolio with fast CDN",
    "url": "https://github.com/username/repo"
  }
}
```

## 🎯 Cloudflare Pages-Specific Tips

### Environment Variables
1. Go to Project Settings → Environment variables
2. Add production variables
3. Add preview variables (optional)
4. Redeploy to apply changes

### Build Configurations
For advanced setups, create `wrangler.toml`:

```toml
name = "your-project"
compatibility_date = "2024-01-01"

[build]
  command = "npm run build"
  cwd = ""
  watch_dir = "src"
```

### Functions (Serverless)
Create serverless functions in `/functions` directory:

```
project/
├── functions/
│   └── api/
│       └── hello.js
```

Example function:
```javascript
export async function onRequest(context) {
  return new Response("Hello World!");
}
```

### Preview Deployments
- Every pull request gets a unique preview URL
- Great for testing before merging
- Automatically cleaned up after merge

## ⚠️ Common Issues

### Issue: Build Fails
**Solution:** 
- Check build logs in dashboard
- Verify build command is correct
- Ensure all dependencies are in package.json
- Test build locally first

### Issue: Custom Domain Not Activating
**Solution:**
- Verify domain is added in Cloudflare dashboard
- Check DNS propagation
- Clear browser cache
- Wait up to 24 hours

### Issue: Functions Not Working
**Solution:**
- Ensure functions are in correct directory
- Check function syntax
- Review function logs in dashboard

## ✅ Checklist Before Submitting PR

- [ ] Project deployed successfully on Cloudflare Pages
- [ ] Pages URL is accessible (`your-project.pages.dev`)
- [ ] Website loads without errors
- [ ] All assets load correctly
- [ ] No console errors
- [ ] Responsive design works
- [ ] Content is appropriate

## 📚 Additional Resources

- [Cloudflare Pages Documentation](https://developers.cloudflare.com/pages/)
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/)
- [Functions](https://developers.cloudflare.com/pages/functions/)
- [Custom Domains](https://developers.cloudflare.com/pages/platform/custom-domains/)

---

Ready to submit? Follow the [Getting Started Guide](getting-started.md) to create your PR!
