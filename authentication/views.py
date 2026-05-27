from django.shortcuts import redirect, render
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from .auth import oauth
import os
import jwt


# Create your views here.

def login(request):
    return oauth.auth0.authorize_redirect(
        request,
        request.build_absolute_uri(reverse('callback')),
        audience = os.getenv("AUTH0_AUDIENCE")
    )


def callback(request):

    #call /token endpoint to exchange authorization code for tokens
    token = oauth.auth0.authorize_access_token(request)

    access_token = token.get('access_token')
    id_token = token.get('id_token')
    userinfo = token.get('userinfo')

    # Decode access token WITHOUT signature verification
    # ONLY for learning/debugging purpose

    decoded_access_token = jwt.decode(
        access_token,
        options={"verify_signature": False}
    )

    permissions = decoded_access_token.get('permissions', [])

    # Store session data
    request.session['user'] = userinfo
    request.session['access_token'] = access_token
    request.session['id_token'] = id_token
    request.session['permissions'] = permissions

    return redirect('/dashboard/')


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{os.getenv('AUTH0_DOMAIN')}/v2/logout?"
        f"client_id={os.getenv('AUTH0_CLIENT_ID')}&"
        f"returnTo=http://localhost:8000"
    )
