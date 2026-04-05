# Contributing Guidelines

Thank you for your interest in contributing to free.iths.online! This document provides guidelines and instructions for submitting domain requests.

## 🎯 Who Can Contribute

- Students looking for free subdomains for portfolios
- Open-source developers hosting projects
- Anyone building educational or personal projects

## 📋 Prerequisites

Before submitting a PR, ensure you have:

1. ✅ Deployed your website on a hosting platform
2. ✅ A working deployment URL
3. ✅ Read the [Getting Started Guide](docs/getting-started.md)
4. ✅ Reviewed the [Acceptable Use Policy](README.md#-acceptable-use-policy)

## 🚀 Step-by-Step Contribution Process

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/free.iths.online.git
cd free.iths.online
```

### 3. Create Your Domain Configuration

Create a new JSON file in the `domains/` directory:

```bash
# Example
touch domains/yourname.json
```

Add the following content (customize with your details):

```json
{
  "subdomain": "yourname",
  "type": "CNAME",
  "value": "your-project.vercel.app",
  "owner": {
    "name": "Your Full Name",
    "email": "your.email@example.com",
    "github": "your-github-username"
  },
  "project": {
    "name": "Your Project Name",
    "description": "Brief description of your project",
    "url": "https://github.com/username/repo"
  }
}
```

### 4. Validate Your Configuration

Run the validation script to check for errors:

```bash
python scripts/validate.py domains/yourname.json
```

Fix any errors before proceeding.

### 5. Commit Your Changes

```bash
git add domains/yourname.json
git commit -m "Add domain: yourname.iths.online"
git push origin main
```

### 6. Submit a Pull Request

1. Go to the original repository
2. Click "New Pull Request"
3. Select your fork and branch
4. The PR template will load automatically
5. Fill in all required information
6. Submit your PR

## 📝 Domain Configuration Format

### Required Fields

```json
{
  "subdomain": "string (required) - Your requested subdomain",
  "type": "string (required) - DNS record type (CNAME or A)",
  "value": "string (required) - Your deployment URL",
  "owner": {
    "name": "string (required) - Your full name",
    "email": "string (required) - Valid email address",
    "github": "string (required) - GitHub username"
  },
  "project": {
    "name": "string (required) - Project/portfolio name",
    "description": "string (required) - Brief project description",
    "url": "string (required) - GitHub repository URL"
  }
}
```

### Field Requirements

- **subdomain**: 
  - Lowercase letters, numbers, and hyphens only
  - 3-30 characters
  - Must be unique
  - No special characters
  
- **type**: 
  - Must be "CNAME" (most common) or "A"
  
- **value**: 
  - Valid deployment URL
  - No protocol (http/https)
  - Must be accessible
  
- **owner.name**: 
  - Your real full name
  - Not a nickname
  
- **owner.email**: 
  - Valid email format
  - You have access to this email
  
- **owner.github**: 
  - Valid GitHub username
  - Without @ symbol
  
- **project.name**: 
  - Descriptive project name
  
- **project.description**: 
  - Clear, concise description
  - 10-200 characters
  
- **project.url**: 
  - Valid GitHub URL
  - Public repository preferred

## ✅ Quality Standards

### Acceptable Content

- Personal portfolios
- Student projects
- Open-source projects
- Educational content
- Technical blogs
- Project demos

### Unacceptable Content

- Illegal activities
- Hate speech or discrimination
- Adult/explicit content
- Malware or phishing
- Spam or scams
- Copyright infringement
- Commercial advertising (non-educational)

## 🔍 Review Process

### What We Check

1. **Format Validation**
   - JSON syntax is correct
   - All required fields present
   - Field values meet requirements

2. **Deployment Verification**
   - Deployment URL is accessible
   - Website loads without errors
   - Content matches description

3. **Content Review**
   - Appropriate for educational use
   - Follows acceptable use policy
   - No prohibited content

4. **Subdomain Availability**
   - Subdomain not already taken
   - Name is appropriate
   - No trademark violations

### Timeline

- **Initial Review**: 24-48 hours
- **DNS Configuration**: 1-2 hours after approval
- **DNS Propagation**: Up to 24-48 hours globally

### Possible Outcomes

1. **Approved** ✅
   - PR merged
   - DNS records added
   - You configure custom domain on your platform

2. **Changes Requested** 🔄
   - Reviewer comments on what needs fixing
   - Update your configuration
   - Push changes to same PR

3. **Rejected** ❌
   - Clear explanation provided
   - Common reasons:
     - Inappropriate content
     - Invalid deployment
     - Duplicate subdomain
     - Incomplete information

## 🛠️ Best Practices

### Before Submitting

- Test your deployment URL thoroughly
- Ensure all pages work correctly
- Check mobile responsiveness
- Verify no console errors
- Review content for appropriateness

### During Review

- Respond promptly to reviewer comments
- Be professional and courteous
- Make requested changes quickly
- Ask questions if unclear

### After Approval

- Configure custom domain in your platform
- Enable HTTPS/SSL
- Test your subdomain
- Report any issues
- Keep contact info updated

## ⚠️ Common Mistakes to Avoid

1. ❌ Submitting before site is deployed
2. ❌ Using invalid or unreachable URLs
3. ❌ Incorrect JSON format or syntax errors
4. ❌ Missing required fields
5. ❌ Not filling PR template completely
6. ❌ Requesting inappropriate subdomain names
7. ❌ Providing fake contact information
8. ❌ Not validating configuration before submit

## 🆘 Getting Help

### Resources

- [Getting Started Guide](docs/getting-started.md)
- [Platform-Specific Docs](docs/)
- [Example Configurations](domains/examples/)
- [Validation Script](scripts/validate.py)

### Support Channels

- 📖 Read documentation first
- 💬 Open a GitHub Issue
- 📧 Email: support@iths.online
- 👥 Community discussions

## 🔄 Updating Your Domain

To update your domain configuration:

1. Fork the repository (if you haven't)
2. Edit your existing JSON file
3. Submit a new PR
4. Reference your previous PR

## 🗑️ Removing Your Domain

To remove your domain:

1. Submit a PR deleting your JSON file
2. Explain reason for removal
3. We'll process within 24 hours

## 📞 Contact Maintainers

For urgent issues or questions:
- Email: support@iths.online
- GitHub Issues: Create an issue
- Response time: 24-48 hours

## 🙏 Thank You

Thank you for contributing to free.iths.online! We're excited to help you establish your online presence.

---

**Questions?** Don't hesitate to reach out. We're here to help!
