#!/usr/bin/env python3
"""
Domain Configuration Validator
Validates domain configuration JSON files for free.iths.online
"""

import json
import sys
import re
import os
from pathlib import Path


class DomainValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.errors = []
        self.warnings = []
        self.data = None
        
    def validate(self):
        """Run all validations"""
        print(f"🔍 Validating: {self.file_path}\n")
        
        # Check file exists
        if not self._check_file_exists():
            return False
            
        # Load and parse JSON
        if not self._load_json():
            return False
            
        # Run validations
        self._validate_structure()
        self._validate_subdomain()
        self._validate_type()
        self._validate_value()
        self._validate_owner()
        self._validate_project()
        self._check_duplicate_subdomain()
        
        # Print results
        self._print_results()
        
        return len(self.errors) == 0
    
    def _check_file_exists(self):
        """Check if file exists"""
        if not os.path.exists(self.file_path):
            self.errors.append(f"❌ File not found: {self.file_path}")
            return False
        return True
    
    def _load_json(self):
        """Load and parse JSON file"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            print("✅ JSON syntax is valid\n")
            return True
        except json.JSONDecodeError as e:
            self.errors.append(f"❌ Invalid JSON syntax: {str(e)}")
            return False
        except Exception as e:
            self.errors.append(f"❌ Error reading file: {str(e)}")
            return False
    
    def _validate_structure(self):
        """Validate required structure"""
        required_fields = ['subdomain', 'type', 'value', 'owner', 'project']
        
        for field in required_fields:
            if field not in self.data:
                self.errors.append(f"❌ Missing required field: '{field}'")
        
        # Validate owner structure
        if 'owner' in self.data:
            owner_fields = ['name', 'email', 'github']
            for field in owner_fields:
                if field not in self.data['owner']:
                    self.errors.append(f"❌ Missing required owner field: '{field}'")
        
        # Validate project structure
        if 'project' in self.data:
            project_fields = ['name', 'description', 'url']
            for field in project_fields:
                if field not in self.data['project']:
                    self.errors.append(f"❌ Missing required project field: '{field}'")
    
    def _validate_subdomain(self):
        """Validate subdomain field"""
        if 'subdomain' not in self.data:
            return
            
        subdomain = self.data['subdomain']
        
        # Check type
        if not isinstance(subdomain, str):
            self.errors.append("❌ Subdomain must be a string")
            return
        
        # Check length
        if len(subdomain) < 3:
            self.errors.append("❌ Subdomain must be at least 3 characters long")
        elif len(subdomain) > 30:
            self.errors.append("❌ Subdomain must be no more than 30 characters long")
        
        # Check format (lowercase, numbers, hyphens only)
        if not re.match(r'^[a-z0-9-]+$', subdomain):
            self.errors.append("❌ Subdomain can only contain lowercase letters, numbers, and hyphens")
        
        # Check starts/ends with letter or number
        if not re.match(r'^[a-z0-9]', subdomain):
            self.errors.append("❌ Subdomain must start with a letter or number")
        if not re.match(r'.*[a-z0-9]$', subdomain):
            self.errors.append("❌ Subdomain must end with a letter or number")
        
        # Check for consecutive hyphens
        if '--' in subdomain:
            self.errors.append("❌ Subdomain cannot contain consecutive hyphens")
        
        # Check if it's a reserved name
        reserved_names = ['www', 'mail', 'ftp', 'admin', 'api', 'dev', 'staging', 'test']
        if subdomain.lower() in reserved_names:
            self.errors.append(f"❌ '{subdomain}' is a reserved subdomain name")
    
    def _validate_type(self):
        """Validate DNS record type"""
        if 'type' not in self.data:
            return
            
        dns_type = self.data['type']
        valid_types = ['CNAME', 'A']
        
        if dns_type not in valid_types:
            self.errors.append(f"❌ Type must be one of: {', '.join(valid_types)}")
    
    def _validate_value(self):
        """Validate deployment URL value"""
        if 'value' not in self.data:
            return
            
        value = self.data['value']
        
        # Check type
        if not isinstance(value, str):
            self.errors.append("❌ Value must be a string")
            return
        
        # Check not empty
        if not value.strip():
            self.errors.append("❌ Value cannot be empty")
            return
        
        # Check doesn't contain protocol
        if value.startswith('http://') or value.startswith('https://'):
            self.errors.append("❌ Value should not include http:// or https:// protocol")
        
        # Check for common deployment platforms
        valid_patterns = [
            r'\.vercel\.app$',
            r'\.netlify\.app$',
            r'\.github\.io$',
            r'\.pages\.dev$',
            r'\.onrender\.com$',
            r'\.web\.app$',
            r'\.firebaseapp\.com$',
            r'\.surge\.sh$',
            r'\.herokuapp\.com$',
            r'\.railway\.app$',
            r'\.fly\.dev$',
            r'\.ondigitalocean\.app$',
            r'\.amplifyapp\.com$',
        ]
        
        is_valid_platform = any(re.search(pattern, value) for pattern in valid_patterns)
        
        if not is_valid_platform:
            self.warnings.append(
                "⚠️  Value doesn't match known deployment platforms. "
                "Please ensure it's a valid deployment URL."
            )
    
    def _validate_owner(self):
        """Validate owner information"""
        if 'owner' not in self.data:
            return
            
        owner = self.data['owner']
        
        # Validate name
        if 'name' in owner:
            if not isinstance(owner['name'], str) or len(owner['name'].strip()) < 2:
                self.errors.append("❌ Owner name must be at least 2 characters")
        
        # Validate email
        if 'email' in owner:
            email = owner['email']
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                self.errors.append("❌ Invalid email format")
        
        # Validate GitHub username
        if 'github' in owner:
            github = owner['github']
            # Remove @ if present
            if github.startswith('@'):
                github = github[1:]
                self.warnings.append("⚠️  GitHub username should not include @ symbol")
            
            github_pattern = r'^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$'
            if not re.match(github_pattern, github):
                self.errors.append("❌ Invalid GitHub username format")
    
    def _validate_project(self):
        """Validate project information"""
        if 'project' not in self.data:
            return
            
        project = self.data['project']
        
        # Validate description length
        if 'description' in project:
            desc = project['description']
            if len(desc) < 10:
                self.warnings.append("⚠️  Project description is very short (should be 10-200 characters)")
            elif len(desc) > 200:
                self.warnings.append("⚠️  Project description is too long (should be 10-200 characters)")
        
        # Validate URL format
        if 'url' in project:
            url = project['url']
            if not url.startswith('http://') and not url.startswith('https://'):
                self.errors.append("❌ Project URL must start with http:// or https://")
            elif 'github.com' not in url.lower():
                self.warnings.append("⚠️  Project URL should be a GitHub repository")
    
    def _check_duplicate_subdomain(self):
        """Check if subdomain already exists"""
        if 'subdomain' not in self.data:
            return
            
        subdomain = self.data['subdomain']
        domains_dir = Path(__file__).parent.parent / 'domains'
        
        # Skip if domains directory doesn't exist
        if not domains_dir.exists():
            return
        
        # Check all JSON files in domains directory
        for json_file in domains_dir.glob('*.json'):
            # Skip examples directory
            if 'examples' in str(json_file):
                continue
            
            # Skip the file being validated
            if json_file.absolute() == Path(self.file_path).absolute():
                continue
            
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data.get('subdomain') == subdomain:
                        self.errors.append(
                            f"❌ Subdomain '{subdomain}' is already taken by {json_file.name}"
                        )
                        return
            except:
                pass
    
    def _print_results(self):
        """Print validation results"""
        print("=" * 60)
        
        if self.errors:
            print("\n❌ VALIDATION FAILED\n")
            print("Errors found:")
            for error in self.errors:
                print(f"  {error}")
        
        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"  {warning}")
        
        if not self.errors and not self.warnings:
            print("\n✅ VALIDATION PASSED\n")
            print("Your domain configuration looks good!")
            print(f"\nSubdomain: {self.data.get('subdomain', 'N/A')}.iths.online")
            print(f"Type: {self.data.get('type', 'N/A')}")
            print(f"Value: {self.data.get('value', 'N/A')}")
            print(f"Owner: {self.data.get('owner', {}).get('name', 'N/A')}")
            print(f"Project: {self.data.get('project', {}).get('name', 'N/A')}")
        
        print("\n" + "=" * 60)
        
        if self.errors:
            print(f"\n❌ Found {len(self.errors)} error(s). Please fix them before submitting.")
            if self.warnings:
                print(f"⚠️  Also {len(self.warnings)} warning(s) to review.")
        elif self.warnings:
            print(f"\n⚠️  Found {len(self.warnings)} warning(s). Review and fix if needed.")
        else:
            print("\n✅ No issues found! You're ready to submit your PR.")
        
        print()


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python validate.py <path-to-json-file>")
        print("Example: python validate.py domains/yourname.json")
        sys.exit(1)
    
    file_path = sys.argv[1]
    validator = DomainValidator(file_path)
    is_valid = validator.validate()
    
    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
