from django.shortcuts import render
from django.http import JsonResponse
from authentication.decorators import requires_permission
from authentication.authentication import requires_auth

# Create your views here.

def profile_api(request):

    user = request.session.get('user')

    if not user:
        return JsonResponse({
            "error": "Unauthorized"
        }, status=401)

    return JsonResponse({
        "message": "Protected API Success",
        "user": user
    })

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