# Security validation functions
import re
import html
from functools import wraps
from flask import redirect, url_for, flash
from flask_login import login_required, current_user


def validate_username(username):
    """Validate username format and security"""
    if not username or len(username.strip()) == 0:
        return False, "Username cannot be empty"
    
    username = username.strip()
    
    # Check length
    if len(username) < 3 or len(username) > 50:
        return False, "Username must be between 3 and 50 characters"
    
    # Check for valid characters (alphanumeric including Spanish chars, underscore, hyphen)
    if not re.match(r'^[a-zA-Z0-9_\-áéíóúÁÉÍÓÚñÑüÜ]+$', username):
        return False, "Username can only contain letters, numbers, underscores, hyphens, and Spanish characters"
    
    return True, "Valid"

def validate_password(password):
    """Validate password strength"""
    if not password or len(password.strip()) == 0:
        return False, "Password cannot be empty"
    
    password = password.strip()
    
    # Check minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number"
    
    return True, "Valid"

def sanitize_input(input_string):
    """
    Sanitize user input to prevent XSS (Cross-Site Scripting) attacks.

    This function takes a string provided by the user, removes any leading or trailing whitespace,
    and then escapes special HTML characters (like <, >, &, ", and ') so that any potentially
    dangerous code is rendered harmless in HTML output.

    Args:
        input_string (str): The user-provided input string.

    Returns:
        str: The sanitized (escaped) string, safe for HTML rendering.
    """
    if not input_string:
        # If the input is None or empty, return an empty string
        return ""
    
    # Remove leading/trailing whitespace and limit length
    sanitized = input_string.strip()
    
    # 🔒 SECURITY: Limit input length to prevent DoS attacks
    if len(sanitized) > 20:  # Reasonable limit for usernames/text inputs
        sanitized = sanitized[:20]
    
    # 🔒 SECURITY: Remove null bytes and other dangerous characters
    sanitized = sanitized.replace('\x00', '').replace('\r', '').replace('\n', ' ')
    
    # "Escape HTML" means converting special characters (like <, >, &, ", and ') into their HTML-safe representations
    # so that any code a user tries to inject is displayed as plain text, not executed by the browser.
    # For example, < becomes &lt;, > becomes &gt;, & becomes &amp;, " becomes &quot;, and ' becomes &#x27;.
    # The html.escape() function does this automatically for us.
    escaped = html.escape(sanitized, quote=True)  # quote=True also escapes single quotes
    return escaped

def validate_and_sanitize_username(username):
    """
    Enhanced username validation with sanitization for admin systems
    
    Args:
        username (str): The username to validate and sanitize
        
    Returns:
        tuple: (is_valid, sanitized_username, error_message)
    """
    if not username or len(username.strip()) == 0:
        return False, "", "Username cannot be empty"
    
    # First sanitize
    sanitized = sanitize_input(username)
    
    # Then validate the sanitized version
    valid, message = validate_username(sanitized)
    
    if not valid:
        return False, sanitized, message
    
    # 🔒 SECURITY: Additional checks for municipal systems
    dangerous_patterns = [
        'script', 'javascript:', 'vbscript:', 'onload', 'onerror', 'onclick',
        'alert(', 'document.', 'window.', 'eval(', 'function(', '=>'
    ]
    
    username_lower = sanitized.lower()
    for pattern in dangerous_patterns:
        if pattern in username_lower:
            return False, sanitized, f"Username contains prohibited content: {pattern}"
    
    return True, sanitized, "Valid"

# Admin authentication decorator
def admin_required(f):
    """Decorator to require admin privileges for routes"""
    @wraps(f)
    @login_required  # Must be logged in first
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('Access denied. Administrator privileges required.')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function