from jose import jwt
from jose.exceptions import JWTError
from urllib.request import urlopen
import json
import os


AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
API_AUDIENCE = os.getenv("AUTH0_AUDIENCE")

ALGORITHMS = ["RS256"]


def validate_jwt(token):

    try:

        # Fetch JWKS
        jsonurl = urlopen(
            f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
        )

        jwks = json.loads(jsonurl.read())

        # Get token header
        unverified_header = jwt.get_unverified_header(token)

        rsa_key = {}

        # Find matching public key
        for key in jwks["keys"]:

            if key["kid"] == unverified_header["kid"]:

                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }

        if rsa_key:

            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )

            return payload

        raise Exception("Unable to find appropriate key")

    except JWTError as e:

        raise Exception(f"Invalid token: {str(e)}")

    except Exception as e:

        raise Exception(str(e))