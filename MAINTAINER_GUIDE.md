# 🔧 Maintainer Guide - DNS Configuration

This guide is for repository maintainers who need to manually configure DNS records.

## 📋 Review Process

### 1. Validate PR Submission

When a PR is submitted:

```bash
# Run validation script
python scripts/validate.py domains/subdomain.json

# Check the deployment URL is accessible
# Visit the URL in browser
```

### 2. Review Checklist

- [ ] JSON format is valid
- [ ] All required fields present
- [ ] Subdomain name is appropriate
- [ ] Deployment URL is accessible
- [ ] Content is appropriate (check website)
- [ ] No duplicate subdomains
- [ ] Owner information looks legitimate
- [ ] PR template is completely filled

### 3. Approve or Request Changes

**If approved:**
- Comment on PR with approval
- Proceed to DNS configuration

**If changes needed:**
- Comment specific issues
- Request changes via GitHub

## 🌐 DNS Configuration Steps

### For Cloudflare DNS (Recommended)

1. **Login to Cloudflare Dashboard**
   - Go to [dash.cloudflare.com](https://dash.cloudflare.com)
   - Select your domain (iths.online)

2. **Add DNS Record**
   - Go to DNS → Records
   - Click "Add Record"
   
3. **Configure CNAME Record**
   ```
   Type: CNAME
   Name: subdomain (e.g., "john")
   Target: deployment-url (e.g., "john.vercel.app")
   TTL: Auto
   Proxy status: Proxied (orange cloud)
   ```

4. **Verify Record**
   - Record should appear in DNS list
   - Status should show as active

5. **Test DNS Resolution**
   ```bash
   # Wait 5-10 minutes, then test
   nslookup subdomain.iths.online
   
   # Or use dig
   dig subdomain.iths.online
   
   # Online tools
   # https://dnschecker.org/
   ```

### For Other DNS Providers

The process is similar for other providers:
- **AWS Route 53**: Create CNAME record in hosted zone
- **Google Domains**: Add custom resource record
- **Namecheap**: Add CNAME record in Advanced DNS
- **GoDaddy**: Add CNAME in DNS Management

## 📝 After DNS Configuration

1. **Comment on PR**
   ```
   ✅ DNS records configured!
   
   Your subdomain `subdomain.iths.online` should be active within 24-48 hours 
   (usually much faster).
   
   Next steps:
   1. Configure custom domain in your deployment platform
   2. Enable HTTPS/SSL
   3. Test your subdomain
   ```

2. **Merge the PR**
   - Squash and merge
   - Use descriptive commit message

3. **Update Documentation** (if needed)
   - Keep track of active subdomains
   - Monitor for issues

## 🔍 Troubleshooting

### DNS Not Resolving

**Check:**
- Record exists in DNS dashboard
- No typos in subdomain or target
- Proxy status is correct
- Wait at least 1 hour for propagation

**Tools:**
- [DNS Checker](https://dnschecker.org/)
- [WhatsMyDNS](https://www.whatsmydns.net/)
- `nslookup` or `dig` commands

### SSL/HTTPS Issues

Most platforms handle SSL automatically:
- **Vercel**: Automatic SSL provisioning
- **Netlify**: Let's Encrypt auto-configured
- **Cloudflare Pages**: Automatic SSL
- **GitHub Pages**: Enable "Enforce HTTPS"

If issues persist:
1. Check platform's custom domain settings
2. Verify domain is added correctly
3. Wait for SSL certificate provisioning (up to 24 hours)

### Platform-Specific Configuration

Remind users to configure their platform:

**Vercel:**
- Settings → Domains → Add domain
- Enter `subdomain.iths.online`

**Netlify:**
- Site settings → Domain management
- Add custom domain

**GitHub Pages:**
- Settings → Pages → Custom domain
- Add `subdomain.iths.online`
- Enable "Enforce HTTPS"

## 📊 Monitoring

### Track Active Subdomains

Create a simple tracking system:
```bash
# List all active subdomains
ls domains/*.json | grep -v examples
```

### Regular Maintenance

Monthly checks:
- [ ] Verify sample of subdomains are active
- [ ] Remove inactive/abandoned domains
- [ ] Update documentation if needed
- [ ] Check for abuse reports

## 🚨 Handling Abuse

If a subdomain is misused:

1. **Immediate Action**
   - Remove DNS record
   - Delete JSON file from repo
   - Block user if necessary

2. **Document**
   - Note reason for removal
   - Keep record for future reference

3. **Communicate**
   - Inform user via email/GitHub
   - Explain violation

## 📞 Support

For technical issues:
- Check platform documentation
- Contact DNS provider support
- Reach out to community

## 🛡️ Security Best Practices

- Never share DNS credentials
- Use strong passwords for DNS provider
- Enable 2FA on DNS provider account
- Regular security audits
- Monitor for unauthorized changes

## 📈 Statistics

Track usage (optional):
```bash
# Count total subdomains
ls domains/*.json | grep -v examples | wc -l

# View recent additions
git log --oneline domains/ | head -20
```

---

**Remember:** Always double-check DNS records before adding them. A typo can cause issues for users!
