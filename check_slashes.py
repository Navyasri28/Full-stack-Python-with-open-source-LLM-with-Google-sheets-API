import json

with open('credentials.json', 'r') as f:
    creds = json.load(f)

pk = creds['private_key']
print(f"Private Key length: {len(pk)}")
for i, char in enumerate(pk):
    if char == '\\':
        next_char = pk[i+1] if i+1 < len(pk) else 'None'
        print(f"Backslash at index {i}, next char: '{next_char}'")

# Check byte 1344 specifically
if len(pk) > 1344:
    print(f"pk[1344]: {pk[1344]} (ord: {ord(pk[1344])})")
