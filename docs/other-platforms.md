# 🌐 Other Deployment Platforms

This guide covers other popular hosting platforms you can use.

## Firebase Hosting

### Setup
1. Install Firebase CLI: `npm install -g firebase-tools`
2. Login: `firebase login`
3. Initialize: `firebase init hosting`
4. Deploy: `firebase deploy`

### Domain Configuration
```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.web.app",
  "owner": { ... },
  "project": { ... }
}
```

---

## Surge.sh

### Setup
```bash
npm install -g surge
surge ./dist your-project.surge.sh
```

### Domain Configuration
```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.surge.sh",
  "owner": { ... },
  "project": { ... }
}
```

---

## GitLab Pages

### Setup
1. Create `.gitlab-ci.yml`:
```yaml
pages:
  stage: deploy
  script:
    - npm run build
  artifacts:
    paths:
      - public
  only:
    - main
```

### Domain Configuration
```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "username.gitlab.io",
  "owner": { ... },
  "project": { ... }
}
```

---

## AWS Amplify

### Setup
1. Go to [aws.amazon.com/amplify](https://aws.amazon.com/amplify)
2. Connect your repository
3. Configure build settings
4. Deploy automatically

### Domain Configuration
```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "main.xxxxxx.amplifyapp.com",
  "owner": { ... },
  "project": { ... }
}
```

---

## Heroku

### Setup
```bash
heroku create your-app
git push heroku main
```

### Domain Configuration
```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-app.herokuapp.com",
  "owner": { ... },
  "project": { ... }
}
```

---

## Railway

### Setup
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Auto-deploys on push

### Domain Configuration
```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.railway.app",
  "owner": { ... },
  "project": { ... }
}
```

---

## Fly.io

### Setup
```bash
flyctl launch
flyctl deploy
```

### Domain Configuration
```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-app.fly.dev",
  "owner": { ... },
  "project": { ... }
}
```

---

## DigitalOcean App Platform

### Setup
1. Go to DigitalOcean App Platform
2. Connect repository
3. Configure and deploy

### Domain Configuration
```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-app.ondigitalocean.app",
  "owner": { ... },
  "project": { ... }
}
```

---

## Vercel Alternatives Comparison

| Platform | Best For | Free Tier | Custom Domain |
|----------|----------|-----------|---------------|
| Vercel | Next.js, React | ✅ | ✅ |
| Netlify | Static sites, JAMstack | ✅ | ✅ |
| GitHub Pages | Simple projects | ✅ | ✅ |
| Cloudflare Pages | Performance, CDN | ✅ | ✅ |
| Render | Full-stack apps | ✅ | ✅ |
| Firebase | Google ecosystem | ✅ | ✅ |
| Surge | Quick deployments | ✅ | ✅ |
| GitLab Pages | GitLab users | ✅ | ✅ |
| AWS Amplify | AWS integration | ✅ (1 year) | ✅ |
| Railway | Backend services | Trial | ✅ |

---

## General Steps for Any Platform

1. **Deploy your site** on your chosen platform
2. **Get your deployment URL** (e.g., `your-project.platform.com`)
3. **Test the URL** to ensure it's working
4. **Create domain configuration JSON** with your platform's URL
5. **Submit PR** to this repository
6. **Wait for approval** and DNS configuration
7. **Configure custom domain** in your platform's dashboard
8. **Test your subdomain** after DNS propagation

---

## Need Help?

If your platform isn't listed here:
1. Deploy your site following the platform's documentation
2. Get your deployment URL
3. Use the same format for domain configuration
4. Submit a PR with your details

The process is similar for most platforms - just replace the deployment URL!

---

Ready to submit? Follow the [Getting Started Guide](getting-started.md) to create your PR!
