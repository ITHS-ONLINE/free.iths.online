# 🟠 Deploying on Render

Render is great for full-stack applications, static sites, and backend services.

## Step 1: Prepare Your Project

Ensure your project is ready:
- Code pushed to GitHub/GitLab
- Static site or web service
- Build command configured (if needed)

## Step 2: Deploy to Render

### For Static Sites

1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" → "Static Site"
3. Connect your Git repository
4. Configure settings:
   - **Name**: Your site name
   - **Branch**: `main` or `master`
   - **Root Directory**: Leave blank or specify subdirectory
   - **Build Command**: e.g., `npm run build`
   - **Publish Directory**: e.g., `dist`, `build`, `public`
5. Click "Create Static Site"
6. Wait for deployment

### For Web Services

1. Click "New +" → "Web Service"
2. Connect your repository
3. Configure settings:
   - **Name**: Service name
   - **Environment**: Node, Python, Docker, etc.
   - **Region**: Choose closest to your users
   - **Branch**: `main` or `master`
   - **Build Command**: e.g., `npm install && npm run build`
   - **Start Command**: e.g., `npm start`
4. Click "Create Web Service"

## Step 3: Get Your Render URL

After deployment, you'll get a URL like:
```
your-project.onrender.com
```

You can find this in:
- Render Dashboard → Your Service → Settings

**Test it:** Visit `https://your-project.onrender.com` to ensure it's working.

**Note:** Free tier services may sleep after 15 minutes of inactivity and take ~30 seconds to wake up.

## Step 4: Configure Custom Domain (After PR Approval)

Once your PR is approved and DNS is configured:

1. Go to Render Dashboard
2. Select your service
3. Go to **Settings** → **Custom Domains**
4. Click "Add Custom Domain"
5. Enter: `yourname.iths.online`
6. Click "Save"
7. Render will provide DNS configuration instructions
8. SSL certificate is automatically provisioned
9. Wait for verification

## Step 5: Create Your Domain Configuration

Create a JSON file for your PR:

```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.onrender.com",
  "owner": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "github": "your-github-username"
  },
  "project": {
    "name": "My Portfolio",
    "description": "Full-stack portfolio application",
    "url": "https://github.com/username/repo"
  }
}
```

## 🎯 Render-Specific Tips

### Environment Variables
1. Go to Service → Environment tab
2. Add your environment variables
3. Click "Save Changes"
4. Service will automatically redeploy

### Auto-Deploy
- Render automatically deploys on every push to connected branch
- Can be disabled in settings if needed

### Build Logs
- View real-time build logs in dashboard
- Helpful for debugging deployment issues

### Health Checks
Render performs automatic health checks:
- Endpoint: `/` by default
- Can be customized in settings
- Failed checks trigger alerts

## ⚠️ Common Issues

### Issue: Service Sleeping (Free Tier)
**Solution:** 
- This is normal for free tier
- Service wakes up on first request (~30 seconds)
- Consider upgrading to paid plan for always-on

### Issue: Build Fails
**Solution:**
- Check build logs in dashboard
- Verify all dependencies are installed
- Ensure build command is correct
- Test build locally first

### Issue: Custom Domain Not Verifying
**Solution:**
- Verify DNS records are correct
- Check DNS propagation
- Wait up to 24 hours
- Contact Render support if issues persist

## ✅ Checklist Before Submitting PR

- [ ] Service deployed successfully on Render
- [ ] Render URL is accessible
- [ ] Website loads without errors
- [ ] All functionality works correctly
- [ ] No console errors
- [ ] Content is appropriate
- [ ] Environment variables configured (if needed)

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Static Sites](https://render.com/docs/static-sites)
- [Web Services](https://render.com/docs/web-services)
- [Custom Domains](https://render.com/docs/custom-domains)
- [Environment Variables](https://render.com/docs/environment-variables)

---

Ready to submit? Follow the [Getting Started Guide](getting-started.md) to create your PR!
