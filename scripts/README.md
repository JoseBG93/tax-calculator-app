# Management Scripts 🛠️

Utility scripts for Tax Calculator Pro administration and development.

## Available Scripts

### User Management

- **`create_admin.py`** - Create or update superadmin account
  ```bash
  export SECRET_KEY="your-secret-key"
  python scripts/create_admin.py
  ```
  Interactive script to create/modify the superadmin user with enhanced security validations.

- **`change_password.py`** - Change user password securely
  ```bash
  python scripts/change_password.py
  ```
  Interactive password change utility with validation.

- **`list_users.py`** - List all registered users
  ```bash
  python scripts/list_users.py
  ```
  Display all users with their roles and status.

### Security & Configuration

- **`secrets_generator.py`** - Generate secure SECRET_KEY
  ```bash
  python scripts/secrets_generator.py
  ```
  Generates a cryptographically secure 32-byte SECRET_KEY for Flask configuration.

### Development Tools

- **`bash_aliases.sh`** - Bash aliases for development workflow
  ```bash
  source scripts/bash_aliases.sh
  ```
  Custom aliases to speed up common development tasks.

- **`ARCHITECTURE_DIAGRAM.py`** - Generate project architecture diagrams
  ```bash
  python scripts/ARCHITECTURE_DIAGRAM.py
  ```
  Visualizes the application's architecture and component relationships.

## Usage Notes

All scripts should be run from the **project root directory**:

```bash
# From tax-calculator-pro/ directory
python scripts/<script_name>.py
```

### Environment Variables

Most scripts require the Flask application context, which needs:
- `SECRET_KEY` - Required for Flask app initialization
- `DATABASE_URL` - Optional (defaults to SQLite)
- `SUPERADMIN_USERNAME` or `SUPERADMIN_USER_ID` - For admin scripts

### Security Considerations

🔒 **Important**: Never commit `.env` files or expose `SECRET_KEY` values. Use environment variables or secure secrets management in production.

## Development Workflow

1. **Initial Setup**:
   ```bash
   python scripts/secrets_generator.py  # Generate SECRET_KEY
   export SECRET_KEY="<generated-key>"
   python scripts/create_admin.py       # Create admin user
   ```

2. **Daily Development**:
   ```bash
   source scripts/bash_aliases.sh       # Load helpful aliases
   python scripts/list_users.py         # Check user status
   ```

3. **Password Management**:
   ```bash
   python scripts/change_password.py    # Update passwords securely
   ```

## Contributing

When adding new management scripts:
1. Place them in this `scripts/` directory
2. Add clear docstrings and usage examples
3. Update this README with the new script's purpose and usage
4. Follow the same shebang pattern: `#!/usr/bin/env python`
5. Make scripts executable: `chmod +x scripts/your_script.py`

---

**Last Updated**: October 2025  
**Maintainer**: José - Tax Calculator Pro Development Team

