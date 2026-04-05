# ✅ Maintainer Checklist

Use this checklist for reviewing and processing domain requests.

## 📋 Daily PR Review Checklist

### When a New PR Arrives

- [ ] **1. Check PR Template Completion**
  - [ ] All fields filled out
  - [ ] Subdomain specified
  - [ ] Owner information complete
  - [ ] Project details provided
  - [ ] Deployment URL included

- [ ] **2. Run Validation**
  ```bash
  python scripts/validate.py domains/filename.json
  ```
  - [ ] No errors
  - [ ] Warnings reviewed (if any)

- [ ] **3. Verify Deployment URL**
  - [ ] Visit the deployment URL in browser
  - [ ] Site loads without errors
  - [ ] All pages work
  - [ ] Assets load correctly (images, CSS, JS)
  - [ ] Mobile responsive
  - [ ] No console errors

- [ ] **4. Review Content**
  - [ ] Appropriate for educational use
  - [ ] No illegal content
  - [ ] No hate speech or discrimination
  - [ ] No adult/explicit content
  - [ ] No malware or phishing
  - [ ] Not spam or scam
  - [ ] Matches project description

- [ ] **5. Check Subdomain Availability**
  - [ ] Not already taken
  - [ ] Name is appropriate
  - [ ] No trademark violations
  - [ ] Not a reserved name

- [ ] **6. Verify Contact Information**
  - [ ] Email format is valid
  - [ ] GitHub username exists
  - [ ] Name looks legitimate

## 🔧 DNS Configuration Checklist

### Before Adding DNS Record

- [ ] **1. Extract Information**
  - Subdomain: `__________`
  - Type: `CNAME`
  - Target: `__________`

- [ ] **2. Login to DNS Provider**
  - [ ] Cloudflare Dashboard
  - [ ] Navigate to iths.online domain
  - [ ] Go to DNS → Records

- [ ] **3. Create CNAME Record**
  - Type: `CNAME`
  - Name: `[subdomain]` (without .iths.online)
  - Target: `[deployment-url]`
  - TTL: `Auto`
  - Proxy: `Proxied` (orange cloud ON)

- [ ] **4. Verify Record**
  - [ ] Record appears in list
  - [ ] No typos in name or target
  - [ ] Settings are correct

- [ ] **5. Test DNS Resolution**
  Wait 5-10 minutes, then:
  ```bash
  nslookup subdomain.iths.online
  ```
  Or use online tools:
  - [ ] https://dnschecker.org/
  - [ ] https://www.whatsmydns.net/

## 💬 Communication Checklist

### Comment on PR

Copy and customize this template:

```markdown
## Review Status: [APPROVED / CHANGES REQUESTED / REJECTED]

### ✅ What's Good
- [List positive points]

### ⚠️ Issues Found (if any)
- [List issues that need fixing]

### 📝 Next Steps
[Instructions for student]

---

**For APPROVED PRs:**
✅ DNS records have been configured!

Your subdomain `subdomain.iths.online` should be active within 24-48 hours 
(usually much faster).

**Important:** You must configure the custom domain in your deployment platform:
- Vercel: Settings → Domains → Add domain
- Netlify: Site settings → Domain management
- GitHub Pages: Settings → Pages → Custom domain

Then enable HTTPS/SSL and test your subdomain.

Thank you for your submission! 🎉
```

## 🔄 Post-Approval Checklist

After merging PR:

- [ ] **1. Update Tracking** (optional)
  - [ ] Log the new subdomain
  - [ ] Note approval date
  - [ ] Record owner contact

- [ ] **2. Monitor First 24 Hours**
  - [ ] Check if student configures domain
  - [ ] Respond to any issues
  - [ ] Help troubleshoot if needed

- [ ] **3. Follow Up** (after 1 week)
  - [ ] Verify domain is working
  - [ ] Check for any abuse reports
  - [ ] Ensure SSL is enabled

## ❌ Rejection Checklist

If rejecting a PR:

- [ ] **1. Provide Clear Reason**
  - [ ] Explain why it was rejected
  - [ ] Be specific about issues
  - [ ] Offer guidance if fixable

- [ ] **2. Be Professional**
  - [ ] Use respectful language
  - [ ] Don't be harsh
  - [ ] Encourage resubmission if appropriate

- [ ] **3. Common Rejection Reasons**
  - [ ] Inappropriate content
  - [ ] Site not deployed yet
  - [ ] Invalid deployment URL
  - [ ] Duplicate subdomain
  - [ ] Incomplete information
  - [ ] Fake contact details

Template for rejection:
```markdown
## Review Status: REJECTED

Unfortunately, we cannot approve your domain request at this time.

**Reason:** [Specific reason]

**What you can do:**
[Steps to fix the issue]

Feel free to resubmit once the issues are resolved.

Thank you for understanding.
```

## 🚨 Emergency Actions

### If Abuse is Detected

- [ ] **1. Immediate Action**
  - [ ] Remove DNS record
  - [ ] Delete JSON file from repo
  - [ ] Block user if necessary

- [ ] **2. Document**
  - [ ] Screenshot evidence
  - [ ] Note date and time
  - [ ] Record violation type

- [ ] **3. Communicate**
  - [ ] Inform user of violation
  - [ ] Explain policy breach
  - [ ] State permanent ban if applicable

### If DNS Issues Occur

- [ ] **1. Diagnose**
  - [ ] Check DNS provider status
  - [ ] Verify record exists
  - [ ] Test from multiple locations

- [ ] **2. Fix**
  - [ ] Correct any typos
  - [ ] Adjust settings if needed
  - [ ] Contact DNS support if required

- [ ] **3. Communicate**
  - [ ] Update affected users
  - [ ] Provide ETA for fix
  - [ ] Apologize for inconvenience

## 📊 Weekly Maintenance

Every week:

- [ ] Review all new subdomains added
- [ ] Check for abuse reports
- [ ] Respond to open issues
- [ ] Update documentation if needed
- [ ] Backup DNS configuration
- [ ] Review pending PRs

## 📈 Monthly Maintenance

Every month:

- [ ] Sample test active subdomains
- [ ] Remove inactive/abandoned domains
- [ ] Generate statistics report
- [ ] Review and update policies
- [ ] Check GitHub Actions logs
- [ ] Update dependencies if needed

Statistics to track:
```bash
# Total active subdomains
ls domains/*.json | grep -v examples | wc -l

# Recent additions (last 30 days)
git log --since="30 days ago" --oneline domains/ | wc -l

# Total PRs merged
git log --oneline --grep="Add domain" | wc -l
```

## 🎯 Quality Standards

Maintain these standards:

- Response time: < 48 hours
- Approval accuracy: > 95%
- User satisfaction: Monitor feedback
- Documentation quality: Keep updated
- Security: Regular audits

## 🆘 Getting Help

If you're unsure about a submission:

- [ ] Review CONTRIBUTING.md guidelines
- [ ] Check similar approved PRs
- [ ] Consult with other maintainers
- [ ] When in doubt, ask for more info from student

## 💡 Pro Tips

1. **Batch Processing**: Review multiple PRs at once for efficiency
2. **Templates**: Save common responses as templates
3. **Browser Bookmarks**: Quick links to DNS dashboard, validation tools
4. **Notifications**: Enable GitHub notifications for PRs
5. **Documentation**: Keep notes on edge cases and decisions

---

**Remember:** Every domain represents a student's opportunity to build their online presence. Be thorough but encouraging!
