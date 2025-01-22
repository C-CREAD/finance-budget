"""
Run this file to generate random secret keys for Python Flask Projects
Credit: Core Schafer - https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3
"""
import secrets

def get_key():
    return secrets.token_hex(16)