# Domains Directory

This directory contains all domain configuration files.

## Structure

```
domains/
├── examples/           # Example configurations for reference
│   ├── vercel-example.json
│   ├── netlify-example.json
│   ├── github-pages-example.json
│   └── cloudflare-example.json
├── yourname.json       # Your domain configuration file
└── another-user.json   # Other domain configurations
```

## How to Add Your Domain

1. Create a new JSON file named after your subdomain
2. Follow the format shown in the examples
3. Validate using: `python scripts/validate.py domains/yourname.json`
4. Submit via Pull Request

## File Naming Convention

- Use lowercase letters only
- Use hyphens for spaces (e.g., `john-doe.json`)
- No special characters except hyphens
- Must match the subdomain field in the JSON

## Need Help?

Check the [examples](examples/) directory for reference configurations.
