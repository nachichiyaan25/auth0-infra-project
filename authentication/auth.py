from authlib.integrations.django_client import OAuth
from django.conf import settings
import os

oauth = OAuth()

oauth.register(
    name='auth0',
    client_id=os.getenv("AUTH0_CLIENT_ID"),
    client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
    server_metadata_url=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid profile email',
    },
)