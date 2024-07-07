#!/usr/bin/env python3
"""Generate  sercret key"""

import secrets
import string


def generate_secret_key():
    #  secret key should be 32-bit string
    secret_key = secrets.token_urlsafe(32)
    return secret_key


def generate_database_user_password():
    """Generate a random password with the specified length"""
    password_length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = "".join(
        secrets.choice(characters) for _ in range(password_length)
    )

    return secure_password


if __name__ == "__main__":
    # Generate a random  secret key
    secret_key = generate_secret_key()

    # Print or use the generated key as needed
    print(f"Generated  Secret Key: {secret_key}")

    # Generate a random database user password
    database_password = generate_database_user_password()

    # Print or use the generated password as needed
    print(f"Generated Database User Password: {database_password}")
