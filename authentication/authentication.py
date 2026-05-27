from django.http import JsonResponse
from .token_validation import validate_jwt


def requires_auth(view_func):

    def wrapper(request, *args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:

            return JsonResponse({
                "error": "Authorization header missing"
            }, status=401)

        try:

            token = auth_header.split()[1]

            payload = validate_jwt(token)

            request.jwt_payload = payload

        except Exception as e:

            return JsonResponse({
                "error": str(e)
            }, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper