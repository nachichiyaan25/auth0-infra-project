from django.shortcuts import render
from django.http import JsonResponse
from authentication.decorators import requires_permission
from authentication.authentication import requires_auth

# Create your views here.

def profile_api(request):

    # API clients (Postman, curl, etc.)
    if request.headers.get("Authorization"):

        return JsonResponse({
            "message": "Protected Profile API Success",
            "user": request.jwt_payload
        })

    user = request.session.get("user")

    if not user:

        return render(
            request,
            "errors/401.html",
            status=401
        )

    permissions = request.session.get(
        "permissions",
        []
    )

    return render(
        request,
        "profile/profile.html",
        {
            "user": user,
            "permissions": permissions
        }
    )

@requires_auth
@requires_permission("admin:all")
def admin_dashboard(request):

    # API Clients (Postman, curl, external integrations)
    if request.headers.get("Authorization"):

        return JsonResponse({
            "message": "Welcome Admin!",
            "status": "Authorized",
            "jwt_payload": request.jwt_payload
        })

    # Browser Users
    return render(request, "admin/admin.html", {    
        "user": request.session.get("user"),
        "permissions": request.jwt_payload.get("permissions", []),
        "jwt_payload": request.jwt_payload
    })


def health_check(request):

    return JsonResponse(
        {
            "status": "healthy"
        }
    )