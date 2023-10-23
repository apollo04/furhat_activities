import base64
import os

secret_key = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
print(secret_key)
