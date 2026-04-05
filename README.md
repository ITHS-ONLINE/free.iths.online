# 🌐 Free Subdomains for Students - ITHS.ONLINE

Welcome to **free.iths.online**! This project provides free subdomains for students to host their portfolios, open-source projects, and personal websites.

## 🎯 What We Offer

Get your own free subdomain like:
- `yourname.iths.online`
- `project.iths.online`
- `portfolio.iths.online`

Perfect for:
- ✨ Student portfolios
- 🚀 Open-source projects
- 📝 Personal blogs
- 🎨 Creative showcases
- 💼 Project demos

## 🚀 How It Works

1. **Deploy your website** on any platform (Vercel, Netlify, GitHub Pages, etc.)
2. **Fork this repository** and create a Pull Request with your domain configuration
3. **Wait for manual review** - we'll verify your submission
4. **Get your domain** - once approved, we'll add it to our DNS records
5. **Start using** your new custom domain!

## 📚 Documentation

Detailed guides for different deployment platforms:

- [🔵 Deploy on Vercel](docs/vercel.md)
- [🟢 Deploy on Netlify](docs/netlify.md)
- [⚫ Deploy on GitHub Pages](docs/github-pages.md)
- [🔶 Deploy on Cloudflare Pages](docs/cloudflare-pages.md)
- [🟠 Deploy on Render](docs/render.md)
- [Other Platforms](docs/other-platforms.md)

## 📋 Requirements

Before submitting a PR, ensure:
- ✅ Your website is already deployed and accessible
- ✅ You have a valid deployment URL
- ✅ The content is appropriate and follows our guidelines
- ✅ You're a student or working on open-source projects

## 🤝 How to Submit

### Quick Start

1. Fork this repository
2. Create a new JSON file in the `domains/` directory:
   ```json
   {
     "subdomain": "yourname",
     "type": "CNAME",
     "value": "your-deployment-url.vercel.app"
   }
   ```
3. Submit a Pull Request using our template
4. Wait for review and approval

### Detailed Steps

See our [Contribution Guidelines](CONTRIBUTING.md) for detailed instructions.

## 📝 Domain Configuration Format

All domain configurations are stored as JSON files in the `domains/` directory:

```json
{
  "subdomain": "example",
  "type": "CNAME",
  "value": "example.vercel.app",
  "owner": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "github": "your-github-username"
  },
  "project": {
    "name": "My Portfolio",
    "description": "A brief description of your project",
    "url": "https://github.com/username/repo"
  }
}
```

## 🔍 Review Process

All submissions go through a manual review process:
1. **Automated Validation** - Our script checks the format
2. **Manual Review** - We verify the deployment and content
3. **DNS Configuration** - We add your domain to our DNS
4. **Approval** - Your PR gets merged and your domain goes live

Typical review time: **24-48 hours**

## ❓ FAQ

**Q: Is this really free?**  
A: Yes! Completely free for students and open-source projects.

**Q: How long does it take?**  
A: Usually 24-48 hours after PR submission.

**Q: Can I use any deployment platform?**  
A: Yes! We support Vercel, Netlify, GitHub Pages, Cloudflare Pages, Render, and more.

**Q: What if my PR is rejected?**  
A: We'll provide feedback. Fix the issues and resubmit.

**Q: Can I update my domain later?**  
A: Yes! Submit a new PR with updated configuration.

**Q: Are there any restrictions?**  
A: Content must be appropriate, legal, and related to your portfolio/projects.

## 🛡️ Acceptable Use Policy

By using this service, you agree to:
- Use the domain for legitimate educational or open-source purposes
- Not host illegal, harmful, or inappropriate content
- Not use the domain for spam, phishing, or malicious activities
- Respect the terms of service of your deployment platform
- Keep your contact information up to date

Violations may result in domain removal without notice.

## 🆘 Support

Need help? 
- 📖 Check our [documentation](docs/)
- 💬 Open an issue on GitHub
- 📧 Contact us at: support@iths.online

## 🙏 Acknowledgments

This project is maintained by ITHS.ONLINE to support students and developers in building their online presence.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Ready to get your free subdomain?** Check out our [Getting Started Guide](docs/getting-started.md) or browse the [deployment documentation](docs/).

Made with ❤️ for students and developers
