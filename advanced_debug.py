import json

with open('credentials.json', 'r') as f:
    raw_content = f.read()

print(f"File contents around byte 1344: {repr(raw_content[1340:1360])}")

creds = json.loads(raw_content)
pk = creds['private_key']

# If the error is literal byte 1344 in the file or in the string
print(f"String around byte 1344: {repr(pk[1340:1350])}")

# Let's write the PK directly to a file and see where it fails
with open('debug_pk.pem', 'w') as f:
    f.write(pk)
