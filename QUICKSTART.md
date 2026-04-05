# ⚡ Quick Start Guide

Get your free subdomain in 5 minutes!

## Prerequisites

- ✅ Your website deployed on any platform (Vercel, Netlify, GitHub Pages, etc.)
- ✅ A GitHub account
- ✅ Python installed (for validation)

## Steps

### 1. Fork This Repository

Click the "Fork" button at the top right.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/free.iths.online.git
cd free.iths.online
```

### 3. Create Domain Configuration

Create `domains/yourname.json`:

```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.vercel.app",
  "owner": {
    "name": "Your Name",
    "email": "your@email.com",
    "github": "yourusername"
  },
  "project": {
    "name": "My Portfolio",
    "description": "Brief description",
    "url": "https://github.com/username/repo"
  }
}
```

### 4. Validate

```bash
python scripts/validate.py domains/yourname.json
```

### 5. Submit PR

```bash
git add domains/yourname.json
git commit -m "Add domain: yourname.iths.online"
git push origin main
```

Then create a Pull Request on GitHub using the template.

### 6. Wait for Approval

We'll review within 24-48 hours!

## Need Help?

- 📖 [Full Documentation](docs/)
- 💬 [Open an Issue](../../issues)
- 📧 Email: support@iths.online

That's it! 🎉
