import json
from google.oauth2 import service_account

with open('credentials.json', 'r') as f:
    creds = json.load(f)

pk = creds['private_key']
print(f"PK Length: {len(pk)}")

# Check byte 1344
if len(pk) > 1344:
    char = pk[1344]
    print(f"Char at 1344: '{char}' (ord: {ord(char)})")
    print(f"Slice around 1344: '{pk[1340:1350]}'")

try:
    service_account.Credentials.from_service_account_info(creds)
    print("google-auth success")
except Exception as e:
    print(f"google-auth failure: {e}")
