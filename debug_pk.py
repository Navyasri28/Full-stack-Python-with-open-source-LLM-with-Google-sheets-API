import json

with open('credentials.json', 'r') as f:
    creds = json.load(f)

pk = creds['private_key']
print(f"Private Key length: {len(pk)}")
target = 1392
if len(pk) > target:
    print(f"Context around {target}: '{pk[target-10:target+10]}'")
    print(f"Chars: {[ord(c) for c in pk[target-2:target+3]]}")

# Show all backslashes
backslashes = [i for i, c in enumerate(pk) if c == '\\']
print(f"All backslashes: {backslashes}")
