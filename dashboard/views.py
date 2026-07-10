from django.shortcuts import render, redirect
import jwt

# Create your views here.

def dashboard(request):

    user = request.session.get('user')
    id_token = request.session.get('id_token')
    access_token = request.session.get('access_token')

    decoded_id_token = jwt.decode(
        id_token,
        options={"verify_signature": False}
    )

    decoded_access_token = jwt.decode(
        access_token,
        options={"verify_signature": False}
    )

    roles = decoded_id_token.get(
        'https://auth0-infra/roles',
        []
    )

    permissions = decoded_access_token.get(
        'permissions',
        []
    )

    department = decoded_id_token.get(
        'https://auth0-infra/department',
        'Unknown'
    )

    connection = decoded_id_token.get(
        'https://auth0-infra/connection',
        'Unknown'
    )

    return render(request, 'dashboard/dashboard.html', {
        'user': user,
        'roles': roles,
        'department': department,
        'connection': connection,
        'permissions': permissions
    })
