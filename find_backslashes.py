import json

with open('credentials.json', 'r') as f:
    creds = json.load(f)

pk = creds['private_key']
for i, char in enumerate(pk):
    if char == '\\':
        print(f"Backslash at index {i}")

print("Done checking for backslashes.")
