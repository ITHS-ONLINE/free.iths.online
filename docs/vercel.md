# 🔵 Deploying on Vercel

Vercel is perfect for Next.js, React, Vue, and other modern frameworks.

## Step 1: Prepare Your Project

Make sure your project is ready to deploy:
- Has a valid `package.json` (for Node.js projects)
- Has a build script if needed
- Code is pushed to GitHub/GitLab/Bitbucket

## Step 2: Deploy to Vercel

### Option A: Deploy via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com) and sign up/login
2. Click "Add New Project"
3. Import your Git repository
4. Configure your project settings:
   - **Framework Preset**: Auto-detected or select manually
   - **Build Command**: Usually auto-detected
   - **Output Directory**: Usually auto-detected
5. Click "Deploy"
6. Wait for deployment to complete

### Option B: Deploy via CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy your project
vercel
```

Follow the prompts to configure your deployment.

## Step 3: Get Your Vercel URL

After deployment, you'll get a URL like:
```
your-project.vercel.app
```

You can find this in:
- Vercel Dashboard → Your Project → Domains
- Deployment logs

**Test it:** Visit `https://your-project.vercel.app` to ensure it's working.

## Step 4: Configure Custom Domain (After PR Approval)

Once your PR is approved and DNS is configured:

1. Go to Vercel Dashboard
2. Select your project
3. Go to **Settings** → **Domains**
4. Add your domain: `yourname.iths.online`
5. Vercel will automatically configure SSL
6. Wait for verification (usually instant)

## Step 5: Create Your Domain Configuration

Create a JSON file for your PR:

```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.vercel.app",
  "owner": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "github": "your-github-username"
  },
  "project": {
    "name": "My Portfolio",
    "description": "Personal portfolio built with Next.js",
    "url": "https://github.com/username/repo"
  }
}
```

## 🎯 Vercel-Specific Tips

### For Next.js Projects
- Vercel has native Next.js support
- Automatic image optimization
- API routes work out of the box
- Incremental Static Regeneration (ISR) supported

### Environment Variables
If your project needs environment variables:
1. Go to Project Settings → Environment Variables
2. Add your variables
3. Redeploy your project

### Custom Build Settings
For advanced configurations, create `vercel.json`:

```json
{
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/next"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
```

## ⚠️ Common Issues

### Issue: Domain Not Working After Setup
**Solution:** 
- Ensure you've added the domain in Vercel dashboard
- Check that DNS propagation is complete
- Clear browser cache

### Issue: Build Fails
**Solution:**
- Check build logs in Vercel dashboard
- Ensure all dependencies are in `package.json`
- Test build locally: `npm run build`

### Issue: Environment Variables Missing
**Solution:**
- Add them in Vercel dashboard
- Redeploy after adding variables
- Use different values for Production/Preview

## ✅ Checklist Before Submitting PR

- [ ] Project deployed successfully on Vercel
- [ ] Vercel URL is accessible (`your-project.vercel.app`)
- [ ] Website loads without errors
- [ ] All assets (images, CSS, JS) load correctly
- [ ] No console errors in browser
- [ ] Responsive design works on mobile
- [ ] Content is appropriate and complete

## 📚 Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Next.js on Vercel](https://vercel.com/docs/frameworks/nextjs)
- [Vercel CLI](https://vercel.com/docs/cli)
- [Custom Domains on Vercel](https://vercel.com/docs/concepts/projects/domains)

## 🆘 Need Help?

- Check Vercel's [support documentation](https://vercel.com/support)
- Join the [Vercel Community](https://github.com/vercel/vercel/discussions)
- Open an issue in this repository

---

Ready to submit? Follow the [Getting Started Guide](getting-started.md) to create your PR!
