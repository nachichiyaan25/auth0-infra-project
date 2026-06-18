import requests
import os


AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")

CLIENT_ID = os.getenv("AUTH0_M2M_CLIENT_ID")

CLIENT_SECRET = os.getenv("AUTH0_M2M_CLIENT_SECRET")

AUDIENCE = os.getenv("AUTH0_MANAGEMENT_API_AUDIENCE")


def get_management_api_token():

    url = f"https://{AUTH0_DOMAIN}/oauth/token"

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": AUDIENCE,
        "grant_type": "client_credentials"
    }

    headers = {
        "content-type": "application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.json()


def fetch_access_token():

    token_response = get_management_api_token()

    access_token = token_response.get('access_token')

    return access_token 


def get_all_users():

    access_token = fetch_access_token()

    url = f"https://{AUTH0_DOMAIN}/api/v2/users"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()


def get_roles():

    access_token = fetch_access_token()

    url = f"https://{AUTH0_DOMAIN}/api/v2/roles"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()


def assign_role_to_user(user_id, role_id):

    access_token = fetch_access_token()

    url = (
        f"https://{AUTH0_DOMAIN}"
        f"/api/v2/users/{user_id}/roles"
    )

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "roles": [role_id]
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    return response.status_code


def create_user(email, password, name, department, team):

    access_token = fetch_access_token()

    url = (
        f"https://{AUTH0_DOMAIN}/api/v2/users"
    )

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "email": email,
        "password": password,
        "name": name,
        "connection": "Username-Password-Authentication",
        
        "user_metadata": {
            "department": department,
            "location": "Bengaluru"
        },

        "app_metadata": {
            "team": team
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    return response.json()


def get_role_id_by_name(role_name):

    roles = get_roles()

    for role in roles:

        if role["name"] == role_name:

            return role["id"]

    return None


def search_user_by_email(email):

    access_token = fetch_access_token()

    url = (
        f"https://{AUTH0_DOMAIN}"
        f"/api/v2/users-by-email"
    )

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "email": email
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return response.json()


def update_user_metadata(user_id, department, team):

    access_token = fetch_access_token()

    url = (
        f"https://{AUTH0_DOMAIN}"
        f"/api/v2/users/{user_id}"
    )

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "user_metadata": {
            "department": department
        },

        "app_metadata": {
            "team": team
        }
    }

    response = requests.patch(
        url,
        headers=headers,
        json=payload
    )

    return response.json()


def block_user(user_id):

    access_token = fetch_access_token()

    url = (
        f"https://{AUTH0_DOMAIN}"
        f"/api/v2/users/{user_id}"
    )

    headers = {
        "Authorization": f'Bearer {access_token}',
        "Content-Type": "application/json"
    }

    payload = {
        "blocked" : True
    }

    response = requests.patch(
        url,
        headers=headers,
        json=payload  
    )

    return response.json()


def remove_role_from_user(user_id, role_id):

    access_token = fetch_access_token()

    url = (
        f"https://{AUTH0_DOMAIN}"
        f"/api/v2/users/{user_id}/roles"
    )

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "roles": [role_id]
    }

    response = requests.delete(
        url,
        headers=headers,
        json=payload
    )

    return response.status_code


def delete_user(user_id):

    access_token = fetch_access_token()

    url = (
        f"https://{AUTH0_DOMAIN}"
        f"/api/v2/users/{user_id}"
    )

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.delete(
        url,
        headers=headers
    )

    return response.status_code


def get_user_roles(user_id):

    access_token = fetch_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}"   
    }

    response = requests.get(
    f"https://{AUTH0_DOMAIN}"
    f"/api/v2/users/{user_id}/roles",
    headers=headers
    )   

    return response.json()

def assign_default_role_if_missing(user_id):

    existing_roles = get_user_roles(user_id)

    # Validate API response
    if not isinstance(existing_roles, list):
        print("Failed to fetch roles:", existing_roles)
        return

    # Extract role names
    role_names = [role.get("name") for role in existing_roles]

    # If user already has ANY role, skip assignment
    if role_names:
        return

    # Fetch Viewer role ID
    viewer_role_id = get_role_id_by_name("Viewer")

    if not viewer_role_id:
        return

    # Assign Viewer role
    assign_role_to_user(
        user_id,
        viewer_role_id
    )




