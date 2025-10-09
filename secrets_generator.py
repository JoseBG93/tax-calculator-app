import secrets

def generate_keys(num_bytes: int = 32):
    hex_key = secrets.token_hex(num_bytes)        # 64 hex chars (para .env)
    urlsafe_key = secrets.token_urlsafe(num_bytes)  # URL-safe (tokens)
    return hex_key, urlsafe_key

if __name__ == "__main__":
    hex_key, urlsafe_key = generate_keys(32)
    print("SECRET_KEY (hex):", hex_key)
    print("SECRET_KEY_URLSAFE:", urlsafe_key)

# To run this script:
# python secrets_generator.py
# The output will be two keys: one in hex format and one in URL-safe format.
# Copy the URL-safe key and paste it into the .env file as the SECRET_KEY.
# The hex key is for informational purposes only.
