```python
import os
import hashlib
from getpass import getpass

class Security:
    def __init__(self):
        self.salt = os.urandom(32)

    def hash_password(self, password):
        """Hash a password for storing."""
        key = hashlib.pbkdf2_hmac(
            'sha256',  # The hash digest algorithm for HMAC
            password.encode('utf-8'),  # Convert the password to bytes
            self.salt,  # Provide the salt
            100000  # It is recommended to use at least 100,000 iterations of SHA-256 
        )
        return key

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        key = hashlib.pbkdf2_hmac(
            'sha256',
            provided_password.encode('utf-8'),
            self.salt,
            100000
        )
        return key == stored_password

    def secure_api_key(self):
        """Securely store the API key"""
        api_key = getpass("Enter your API key: ")
        hashed_key = self.hash_password(api_key)
        return hashed_key

    def verify_api_key(self, stored_key):
        """Verify the API key"""
        api_key = getpass("Enter your API key: ")
        return self.verify_password(stored_key, api_key)
```
