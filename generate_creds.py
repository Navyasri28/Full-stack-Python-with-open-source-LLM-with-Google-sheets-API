import json

# The private key provided by the user had a typo: \Q instead of \nQ
private_key_raw = r"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCgzmlM4I8VD/AM\nwTKxYKuC5Kc4rMkM3dx01hWLFABuXcR+VmZYlQ01pIKdee8TBc9LSgPB98jrv3Ub\nvTMeq2cRHSgdpD6q3c5Xggve3g7ZhTxdbu2khDlewu0MHH4VCaN6dz3IuWXRyklM\nqvRgtE8KJxrDFza/o/Dfsa8ghJU4Tgrhsgv6D6QhpoDvqx/vnlxl9rpY1lUF3dO4\nWXfHCkGB239LMyqNrKs7mLnENeH1abYnhiSawDu++GUcI+8d8y3Zy0JK75JCbjip\npe4VgCz40XjG2cr4pq1cLp0aQlV9nGaKo097D7+joq9O95+nDxSn/Q0Xe0+Ee2J0\nq8xneXvNAgMBAAECggEAFv1blZeXLSoxpgkq76wD6Ts6YwJk3feMEJIY02DhLOYv\n9OXyTODGWjByUgRAN0aB2+AxiFYd/gJJwlT6zXwwyIQUG6TDJtd+LAmWG99AXT3M\nowj8ZaRXtWIF1NDv/574pcYNabiDw4n5j8HzHS46DJgJnfGgLKbKBZkYEfySftGD\nanUFVIshclI8Ux3fEOKmIoPGzydKF4qYLzhJAfgONd0+XBBc+/P707RVekiIJFLB\nVLpjqZhsuCaN+eJiWrNF9KCJy4vr3gs7vvBbdp3HDA1dG/CDjBgC/Y5hsj8iKWa7\n2ln4hfvw0OdIQ/C/fQMV8m+lW6x8guL575oU8nAVIQKBgQDVkimLJqULVjsFM9jQ\ngHN/3RJxPRnZodhLy1hNPinNps9fMDNtqsTmDh/vr6eXFacgnvCLw7DMziS506Xm\n2vJwT/kqkY2C/3ffsIvOT+5PC6C1m5ERP2YuR14UgbY6p/vA97KzbYbuhYpX0TyC\nJ6Kl5ImwC47Co5L0mNsAFuqF0QKBgQDAwLudu0OijNUN4wY0azMjwrIAwn9lORQy\nc6pQkxf+pLspgn3DMHKyz8clWTstywLlxF/CueeTGaqx+plgMpCXEhtAVkcYLvIX\nSNqreTI/JTRWVaGCzVUfbDWwX819k+fXv/H3KWCTdFmjbbEvdI+OnwNmks6IAUIi\nZ6cWsz9JPQKBgQCUJB2C8xxaf8bStgL3pZH4KE2JlLtglX3mHTez5KG0j7eaLGIP\n+Ps5JKUMaghSqWdTHkx2dhgmB/u7lk6mkkrGkwKff3TsX+4zkE95nUINPGCOeEko\n8JQdF83vZYYUq77aPDaNdTS6MJEklvNkyL9uWNcU8P9mjXX7CigmqL6mcQKBgHwF\nhrJeo44bf5qH0J45u5Xu2AmVG9NNfqlXsuZVPsMhyytSQwksSyCygDiPyXwVe6/L\QrJQW6hSg3ow/C7hWhdaFx62ZNgynKJOxiQ+vw3SKnLCdkFrTLIDNihd/CIo4Kv5\nXP7jKLi3zFVTZwZZwWTK+60sGKd558urVd9NRhMhAoGANXNPJ9r4rlTuPdjdWzFt\nMdAZmFpCg/QJUkZrq95Gq5hAeK32rnbRjRpGtOKfeUQZVcfi4+KQwCMmUO/E7uIG\nDvjmJyHyI5HXa7wYg/T/1I0+k7fWRdoDLzOBnB366LKQjDPBXTcmtiHZMCbq0Ob+\npvolGyIAdKvMVqQqZZ6pp/U=\n-----END PRIVATE KEY-----\n"

# Fix the typo \Q -> \nQ
private_key_fixed = private_key_raw.replace(r"\Q", r"\nQ")

# Replace literal \n with actual newlines
private_key = private_key_fixed.replace(r"\n", "\n")

creds = {
  "type": "service_account",
  "project_id": "sheets-llm-project",
  "private_key_id": "932aa841d5445e57d89070d922c4049f3a7e9956",
  "private_key": private_key,
  "client_email": "llm-500@sheets-llm-project.iam.gserviceaccount.com",
  "client_id": "108912331898044706899",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/llm-500%40sheets-llm-project.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

with open('credentials.json', 'w') as f:
    json.dump(creds, f, indent=2)

print("credentials.json updated with corrected private key typo.")
