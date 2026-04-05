# 🚀 Getting Started Guide

This guide will walk you through the entire process of getting your free subdomain.

## Step-by-Step Process

### 1️⃣ Deploy Your Website

First, you need to deploy your website on a hosting platform. Choose one:

- [Vercel](vercel.md) - Best for Next.js, React, and modern frameworks
- [Netlify](netlify.md) - Great for static sites and JAMstack
- [GitHub Pages](github-pages.md) - Perfect for simple projects
- [Cloudflare Pages](cloudflare-pages.md) - Fast global CDN
- [Render](render.md) - Good for full-stack applications
- [Other Platforms](other-platforms.md) - Any other hosting service

### 2️⃣ Get Your Deployment URL

After deploying, you'll get a URL like:
- Vercel: `your-project.vercel.app`
- Netlify: `your-project.netlify.app`
- GitHub Pages: `username.github.io`
- Cloudflare Pages: `your-project.pages.dev`

**Important:** Make sure your site is live and accessible!

### 3️⃣ Fork This Repository

1. Click the "Fork" button at the top right
2. Clone your forked repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/free.iths.online.git
   cd free.iths.online
   ```

### 4️⃣ Create Your Domain Configuration

Create a new JSON file in the `domains/` directory:

```bash
# Example: domains/john.json
```

Add this content (replace with your details):

```json
{
  "subdomain": "john",
  "type": "CNAME",
  "value": "john-portfolio.vercel.app",
  "owner": {
    "name": "John Doe",
    "email": "john@example.com",
    "github": "johndoe"
  },
  "project": {
    "name": "John's Portfolio",
    "description": "My personal portfolio showcasing my projects",
    "url": "https://github.com/johndoe/portfolio"
  }
}
```

### 5️⃣ Validate Your Configuration

Run our validation script to check your configuration:

```bash
python scripts/validate.py domains/john.json
```

Fix any errors before submitting.

### 6️⃣ Submit a Pull Request

1. Commit your changes:
   ```bash
   git add domains/john.json
   git commit -m "Add domain: john.iths.online"
   git push origin main
   ```

2. Go to the original repository and click "New Pull Request"
3. Use our PR template (it will load automatically)
4. Fill in all required information
5. Submit your PR

### 7️⃣ Wait for Review

Our team will review your submission:
- ✅ Check format and validation
- ✅ Verify your deployment is live
- ✅ Review content appropriateness
- ✅ Add DNS records manually

You'll receive feedback within 24-48 hours.

### 8️⃣ Configure Your Deployment Platform

Once approved, you need to configure your deployment platform to accept your custom domain.

**For Vercel:**
1. Go to your project settings
2. Navigate to "Domains"
3. Add `john.iths.online`
4. Follow verification steps

**For Netlify:**
1. Go to Site settings → Domain management
2. Click "Add custom domain"
3. Enter `john.iths.online`
4. Verify ownership

**For GitHub Pages:**
1. Go to repository Settings → Pages
2. Add custom domain: `john.iths.online`
3. Enable HTTPS

### 9️⃣ Test Your Domain

After DNS propagation (can take up to 24 hours):
- Visit `https://john.iths.online`
- Ensure it loads correctly
- Check that HTTPS is working

## 🎉 Congratulations!

Your free subdomain is now active!

## 📝 Important Notes

- **DNS Propagation**: Can take up to 24-48 hours globally
- **HTTPS**: Most platforms provide automatic SSL certificates
- **Updates**: To change your domain config, submit a new PR
- **Renewal**: Domains are free indefinitely for active projects

## 🆘 Need Help?

- Check the specific platform documentation
- Review example configurations in `domains/examples/`
- Open an issue if you're stuck
- Join our community discussions

## ⚠️ Common Mistakes to Avoid

1. ❌ Submitting before your site is deployed
2. ❌ Using invalid or unreachable URLs
3. ❌ Incorrect JSON format
4. ❌ Not filling out the PR template completely
5. ❌ Requesting inappropriate subdomain names

## ✅ Best Practices

1. ✅ Test your deployment URL before submitting
2. ✅ Use descriptive subdomain names
3. ✅ Provide accurate contact information
4. ✅ Keep your project repository public
5. ✅ Respond promptly to review comments

---

Ready? Start by choosing your [deployment platform](./) and follow the specific guide!
