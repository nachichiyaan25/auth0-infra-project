from django.http import JsonResponse
from django.shortcuts import render
import jwt


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
                id_token = request.session.get("id_token")

                decoded_id_token = jwt.decode(
                    id_token,
                    options={"verify_signature": False}
                )

                return render(
                    request,
                    "admin/forbidden.html",
                    {
                        "user": request.session.get("user"),

                        "roles": decoded_id_token.get(
                            "https://auth0-infra/roles",
                            []
                        ),

                        "connection": decoded_id_token.get(
                            "https://auth0-infra/connection",
                            "Unknown"
                        ),

                        "permissions": request.jwt_payload.get(
                            "permissions",
                            []
                        ),

                        "required_permission": permission_name
                    },
                    status=403
                )

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator