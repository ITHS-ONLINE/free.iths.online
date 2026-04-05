# 🟢 Deploying on Netlify

Netlify is excellent for static sites, JAMstack applications, and modern web projects.

## Step 1: Prepare Your Project

Ensure your project is ready:
- Static HTML/CSS/JS or built framework output
- Code pushed to GitHub/GitLab/Bitbucket
- Build command configured (if needed)

## Step 2: Deploy to Netlify

### Option A: Deploy via Netlify Dashboard

1. Go to [netlify.com](https://netlify.com) and sign up/login
2. Click "Add new site" → "Import an existing project"
3. Connect to your Git provider (GitHub/GitLab/Bitbucket)
4. Select your repository
5. Configure build settings:
   - **Build command**: e.g., `npm run build`, `yarn build`, or leave blank for static sites
   - **Publish directory**: e.g., `dist`, `build`, `public`, or `_site`
6. Click "Deploy site"
7. Wait for deployment to complete

### Option B: Deploy via Drag & Drop

1. Build your project locally
2. Go to Netlify Dashboard
3. Drag and drop your build folder
4. Site deploys instantly

### Option C: Deploy via CLI

```bash
# Install Netlify CLI
npm install netlify-cli -g

# Login to Netlify
netlify login

# Initialize your project
netlify init

# Deploy your site
netlify deploy --prod
```

## Step 3: Get Your Netlify URL

After deployment, you'll get a URL like:
```
your-project.netlify.app
```

Or initially:
```
random-name-12345.netlify.app
```

You can customize the subdomain in:
- Site Settings → Site Details → Change site name

**Test it:** Visit `https://your-project.netlify.app` to ensure it's working.

## Step 4: Configure Custom Domain (After PR Approval)

Once your PR is approved and DNS is configured:

1. Go to Netlify Dashboard
2. Select your site
3. Go to **Site configuration** → **Domain management**
4. Click "Add custom domain"
5. Enter: `yourname.iths.online`
6. Click "Verify"
7. Netlify will automatically provision SSL certificate
8. Wait for verification (usually within minutes)

## Step 5: Create Your Domain Configuration

Create a JSON file for your PR:

```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.netlify.app",
  "owner": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "github": "your-github-username"
  },
  "project": {
    "name": "My Portfolio",
    "description": "Personal portfolio built with React",
    "url": "https://github.com/username/repo"
  }
}
```

## 🎯 Netlify-Specific Tips

### Environment Variables
If your project needs environment variables:
1. Go to Site Settings → Environment variables
2. Add your variables
3. Trigger a new deploy

### Build Settings
For advanced configurations, create `netlify.toml`:

```toml
[build]
  publish = "dist"
  command = "npm run build"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.environment]
  NODE_VERSION = "18"
```

### Form Handling
Netlify has built-in form handling:
```html
<form name="contact" method="POST" data-netlify="true">
  <!-- Your form fields -->
</form>
```

### Serverless Functions
Create serverless functions easily:
```
project-root/
├── netlify/
│   └── functions/
│       └── my-function.js
```

## ⚠️ Common Issues

### Issue: Custom Domain Not Working
**Solution:** 
- Ensure domain is added in Netlify dashboard
- Check DNS propagation status
- Clear browser cache and DNS cache

### Issue: Build Fails
**Solution:**
- Check deploy logs in Netlify dashboard
- Verify build command is correct
- Ensure all dependencies are installed
- Test build locally first

### Issue: 404 Errors on Routes
**Solution:**
- Add redirects in `netlify.toml` or `_redirects` file
- For SPAs, redirect all routes to index.html

### Issue: Environment Variables Not Working
**Solution:**
- Add them in Netlify dashboard
- Redeploy after adding variables
- Check variable names match your code

## ✅ Checklist Before Submitting PR

- [ ] Project deployed successfully on Netlify
- [ ] Netlify URL is accessible (`your-project.netlify.app`)
- [ ] Website loads without errors
- [ ] All assets (images, CSS, JS) load correctly
- [ ] No console errors in browser
- [ ] Forms work (if applicable)
- [ ] Responsive design works on mobile
- [ ] Content is appropriate and complete

## 📚 Additional Resources

- [Netlify Documentation](https://docs.netlify.com)
- [Netlify CLI](https://docs.netlify.com/cli/get-started)
- [Custom Domains](https://docs.netlify.com/domains-https/custom-domains)
- [Environment Variables](https://docs.netlify.com/environment-variables/overview)
- [Serverless Functions](https://docs.netlify.com/functions/overview)

## 🆘 Need Help?

- Check Netlify's [support documentation](https://answers.netlify.com)
- Join the [Netlify Community Forum](https://answers.netlify.com)
- Open an issue in this repository

---

Ready to submit? Follow the [Getting Started Guide](getting-started.md) to create your PR!
