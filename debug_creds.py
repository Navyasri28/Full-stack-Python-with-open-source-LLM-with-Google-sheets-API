import json

with open('credentials.json', 'r') as f:
    creds = json.load(f)

pk = creds['private_key']
print(f"Private Key length: {len(pk)}")
if len(pk) > 1344:
    print(f"Char at 1344: '{pk[1344]}' (ordinal: {ord(pk[1344])})")
    print(f"Surrounding text: '{pk[1340:1350]}'")

# Let's also try to load it with google-auth to see if it fails here
from google.oauth2 import service_account
try:
    service_account.Credentials.from_service_account_info(creds)
    print("google-auth: Success loading creds info")
except Exception as e:
    print(f"google-auth: Failed loading creds info: {e}")
