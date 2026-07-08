from django.shortcuts import render
import json
from django.http import JsonResponse
import csv
from django.views.decorators.csrf import csrf_exempt
from .services import get_management_api_token, get_all_users, get_roles, assign_role_to_user, create_user, search_user_by_email, update_user_metadata, block_user, remove_role_from_user, delete_user, get_role_id_by_name, get_user_roles

# Create your views here.

@csrf_exempt
def test_management_token(request):

    token_response = get_management_api_token()

    return JsonResponse(token_response)


@csrf_exempt
def list_users(request):

    users = get_all_users()

    return JsonResponse(users, safe=False)


@csrf_exempt
def list_roles(request):

    roles = get_roles()

    return JsonResponse(roles, safe=False)


@csrf_exempt
def assign_role(request):

    if request.method != "POST":

        return JsonResponse({
            "error": "POST request required"
        }, status=405)

    try:

        data = json.loads(request.body)

        user_id = data.get("user_id")

        role_id = data.get("role_id")

        status = assign_role_to_user(
            user_id,
            role_id
        )

        return JsonResponse({
            "message": "Role assigned",
            "status_code": status
        })

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)


@csrf_exempt
def create_user_view(request):

    if request.method != "POST":

        return JsonResponse({
            "error": "POST request required"
        }, status=405)

    try:

        data = json.loads(request.body)

        email = data.get("email")

        password = data.get("password")

        name = data.get("name")

        role_id = data.get("role_id")

        user = create_user(
            email,
            password,
            name
        )

        user_id = user.get("user_id")

        assign_role_to_user(
            user_id,
            role_id
        )

        return JsonResponse({
            "message": "User created and role assigned",
            "user": user
        })

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)
    

@csrf_exempt
def search_user(request):

    email = request.GET.get("email")

    if not email:

        return JsonResponse({
            "error": "Email parameter required"
        }, status=400)

    users = search_user_by_email(email)

    return JsonResponse(users, safe=False)


@csrf_exempt
def update_metadata(request):

    if request.method != "PATCH":

        return JsonResponse({
            "error": "PATCH request required"
        }, status=405)

    try:

        data = json.loads(request.body)

        user_id = data.get("user_id")

        department = data.get("department")

        team = data.get("team")

        updated_user = update_user_metadata(
            user_id,
            department,
            team
        )

        return JsonResponse(updated_user)

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)


@csrf_exempt
def block_user_view(request):

    if request.method != "PATCH":

        return JsonResponse({
            "error": "PATCH request required"
        }, status=405)
    
    try: 

        data = json.loads(request.body)

        user_id = data.get("user_id")

        blocked_user = block_user(
            user_id
        )

        return JsonResponse(blocked_user)

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)



@csrf_exempt
def change_user_role(request):

    if request.method != "PATCH":

        return JsonResponse({
            "error": "PATCH request required"
        }, status=405)

    try:

        data = json.loads(request.body)

        user_id = data.get("user_id")

        old_role_id = data.get("old_role_id")

        new_role_id = data.get("new_role_id")

        remove_role_from_user(
            user_id,
            old_role_id
        )

        assign_role_to_user(
            user_id,
            new_role_id
        )

        return JsonResponse({
            "message": "User role updated successfully"
        })

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)


@csrf_exempt
def delete_user_view(request):

    if request.method != "DELETE":

        return JsonResponse({
            "error": "DELETE request required"
        }, status=405)

    try:

        data = json.loads(request.body)

        user_id = data.get("user_id")

        status = delete_user(user_id)

        if status == 204:

            return JsonResponse({
                "message": "User deleted successfully"
            })

        return JsonResponse({
            "error": "Deletion failed"
        }, status=500)

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)


@csrf_exempt
def bulk_create_users(request):

    if request.method != "POST":

        return JsonResponse({
            "error": "POST request required"
        }, status=405)

    try:

        users = [
            {
                "email": "developer1@test.com",
                "password": "Test@123",
                "name": "Developer One",
                "role_name": "Developer",
                "department": "Engineering",
                "team": "IAM"
            },
            {
                "email": "viewer1@test.com",
                "password": "Test@123",
                "name": "Viewer One",
                "role_name": "Viewer",
                "department": "Operations",
                "team": "Support"
            },
            {
                "email": "admin1@test.com",
                "password": "Test@123",
                "name": "Admin One",
                "role_name": "Admin",
                "department": "Security",
                "team": "Platform"
            }
        ]

        results = []

        for user in users:

            role_name = user["role_name"]

            created_user = create_user(
                email=user["email"],
                password=user["password"],
                name=user["name"],
                department=user["department"],
                team=user["team"]
            )

            user_id = created_user.get("user_id")

            role_id = get_role_id_by_name(role_name)

            if role_id:

                assign_role_to_user(
                    user_id,
                    role_id
                )

            results.append(created_user)

        return JsonResponse({
            "message": "Bulk provisioning completed",
            "results": results
        })

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)


@csrf_exempt
def import_users_from_csv(request):

    if request.method != "POST":

        return JsonResponse({
            "error": "POST request required"
        }, status=405)

    try:

        csv_file = request.FILES.get("file")

        if not csv_file:

            return JsonResponse({
                "error": "CSV file missing"
            }, status=400)

        decoded_file = csv_file.read().decode("utf-8").splitlines()

        reader = csv.DictReader(decoded_file)

        results = []

        for row in reader:

            role_name = row["role_name"]

            existing_user = search_user_by_email(row["email"])

            if existing_user:

                results.append({
                    "email": row["email"],
                    "status": "User already exist"
                })

                continue

            created_user = create_user(
                email=row["email"],
                password=row["password"],
                name=row["name"],
                department=row["department"],
                team=row["team"]
            )

            user_id = created_user.get("user_id")

            role_id = get_role_id_by_name(role_name)

            if role_id:

                role_response = assign_role_to_user(
                    user_id,
                    role_id
                )

                if role_response == 204:

                    results.append({
                        "email": created_user.get("email"),
                        "status": "Provisioned Successfully"
                    })

                else:

                    results.append({
                        "email": created_user.get("email"),
                        "status": "Role Assignment Failed"
                })

            else:

                results.append({
                    "email": created_user.get("email"),
                    "status": "Role Not Found"
                })

        return JsonResponse({
            "message": "CSV provisioning completed",
            "results": results
        })

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)
    
