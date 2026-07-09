from django.http import JsonResponse
from django.shortcuts import render


def requires_permission(permission_name):

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            permissions = request.jwt_payload.get(
                "permissions",
                []
            )

            if permission_name not in permissions:

                # API Client (Postman, curl, external integrations)
                if request.headers.get("Authorization"):

                    return JsonResponse({
                        "error": "Forbidden",
                        "message": f"Missing permission: {permission_name}"
                    }, status=403)

                # Browser User
                return render(request, "admin/forbidden.html", {
                    "required_permission": permission_name    
                }, status=403)

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator