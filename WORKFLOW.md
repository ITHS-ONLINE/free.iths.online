# 🔄 Workflow Diagram

## Student Submission Flow

```mermaid
graph TB
    A[Student Deploys Website] --> B[Forks Repository]
    B --> C[Creates Domain Config JSON]
    C --> D[Runs Validation Script]
    D --> E{Valid?}
    E -->|No| F[Fix Errors]
    F --> D
    E -->|Yes| G[Submits Pull Request]
    G --> H[GitHub Actions Auto-Validation]
    H --> I{Passes?}
    I -->|No| J[PR Shows Error]
    J --> K[Student Fixes]
    K --> G
    I -->|Yes| L[Manual Review by Maintainer]
    L --> M{Approved?}
    M -->|No| N[Request Changes]
    N --> O[Student Updates PR]
    O --> L
    M -->|Yes| P[Add DNS Record Manually]
    P --> Q[Merge PR]
    Q --> R[Student Configures Custom Domain]
    R --> S[Wait for DNS Propagation]
    S --> T[Domain Goes Live!]
```

## Maintainer Review Process

```mermaid
graph LR
    A[New PR Received] --> B[Check PR Template]
    B --> C[Run Validation]
    C --> D[Visit Deployment URL]
    D --> E[Review Content]
    E --> F{Appropriate?}
    F -->|No| G[Reject with Explanation]
    F -->|Yes| H[Check Subdomain Availability]
    H --> I{Available?}
    I -->|No| J[Request Different Name]
    I -->|Yes| K[Add DNS Record]
    K --> L[Comment Approval on PR]
    L --> M[Merge PR]
    M --> N[Notify Student]
```

## DNS Configuration Flow

```mermaid
graph TB
    A[Receive Approved PR] --> B[Extract Subdomain Info]
    B --> C[Login to DNS Provider]
    C --> D[Create CNAME Record]
    D --> E[Subdomain: name]
    D --> F[Target: deployment-url]
    D --> G[TTL: Auto]
    D --> H[Proxy: Enabled]
    H --> I[Verify Record Created]
    I --> J[Test DNS Resolution]
    J --> K{Working?}
    K -->|No| L[Troubleshoot]
    L --> J
    K -->|Yes| M[Update PR Comment]
    M --> N[Merge PR]
```

## Complete System Architecture

```mermaid
graph TB
    subgraph Students
        A1[Student 1]
        A2[Student 2]
        A3[Student N]
    end
    
    subgraph GitHub Repository
        B1[Domain Configs in /domains]
        B2[PR Template]
        B3[Validation Script]
        B4[Documentation]
    end
    
    subgraph GitHub Actions
        C1[Auto-Validate PRs]
        C2[Check Duplicates]
        C3[Format Checking]
    end
    
    subgraph Maintainer
        D1[Review PRs]
        D2[Manual DNS Config]
        D3[Merge Approved PRs]
    end
    
    subgraph DNS Provider
        E1[CNAME Records]
        E2[subdomain.iths.online]
    end
    
    subgraph Deployment Platforms
        F1[Vercel]
        F2[Netlify]
        F3[GitHub Pages]
        F4[Cloudflare]
        F5[Others]
    end
    
    A1 --> B1
    A2 --> B1
    A3 --> B1
    B1 --> C1
    B1 --> C2
    B1 --> C3
    C1 --> D1
    C2 --> D1
    C3 --> D1
    D1 --> D2
    D2 --> E1
    E1 --> E2
    D1 --> D3
    E2 --> F1
    E2 --> F2
    E2 --> F3
    E2 --> F4
    E2 --> F5
```

## File Structure Flow

```
Repository Root
│
├── .github/
│   ├── CODEOWNERS → Defines who must review PRs
│   ├── ISSUE_TEMPLATE/ → Templates for support
│   ├── PULL_REQUEST_TEMPLATE/ → PR submission form
│   └── workflows/ → Automated validation
│
├── docs/ → Platform-specific guides
│   ├── getting-started.md → Main tutorial
│   ├── vercel.md → Vercel deployment
│   ├── netlify.md → Netlify deployment
│   ├── github-pages.md → GitHub Pages setup
│   ├── cloudflare-pages.md → Cloudflare setup
│   ├── render.md → Render deployment
│   └── other-platforms.md → Other platforms
│
├── domains/ → All domain configurations
│   ├── README.md → Directory guide
│   ├── examples/ → Sample configs
│   └── student-name.json → Actual submissions
│
├── scripts/
│   └── validate.py → Validation tool
│
├── CONTRIBUTING.md → How to contribute
├── LICENSE → MIT License
├── MAINTAINER_GUIDE.md → DNS config guide
├── QUICKSTART.md → Quick reference
├── README.md → Main documentation
└── PROJECT_SUMMARY.md → Setup complete guide
```

## Timeline

```
Day 0: Student deploys website
         ↓
Day 1: Student submits PR
         ↓
Day 1-2: Automated validation runs
         ↓
Day 1-2: Manual review (24-48 hours)
         ↓
Day 2: DNS record added
         ↓
Day 2-3: DNS propagation (up to 48 hours)
         ↓
Day 3+: Domain is live and working!
```

## Key Interactions

### Student ↔ Repository
- Fork repo
- Create domain config
- Submit PR
- Respond to review comments

### Repository ↔ GitHub Actions
- Trigger validation on PR
- Check format and duplicates
- Report results

### Maintainer ↔ Repository
- Review PRs
- Validate content
- Add DNS records
- Merge approved PRs

### DNS Provider ↔ Deployment Platform
- CNAME points to deployment URL
- SSL/TLS handled by platform
- Traffic routed through DNS

---

This system ensures:
✅ Quality control through validation
✅ Manual review for safety
✅ Clear documentation for users
✅ Automated checks where possible
✅ Scalable process for growth
