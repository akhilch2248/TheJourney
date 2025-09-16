import jwt
import datetime

SECRET = "test-secret"   # Only for local testing

# Fake payload (what Apple/Google tokens would normally contain)
payload = {
    "sub": "fake-user-123",                 # unique ID
    "email": "testuser@example.com",        # optional email
    "aud": "com.yourbundleid.TheJourney",   # your iOS bundle ID
    "iss": "https://appleid.apple.com",     # pretend issuer
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)  # expiry
}

# Generate token
fake_token = jwt.encode(payload, SECRET, algorithm="HS256")
print(fake_token)

