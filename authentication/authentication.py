from django.http import JsonResponse

from .token_validation import validate_jwt


def requires_auth(view_func):

    def wrapper(request, *args, **kwargs):

        token = None

        # API Clients (Postman, curl, external applications)
        auth_header = request.headers.get("Authorization")

        if auth_header:

            try:
                token = auth_header.split()[1]

            except IndexError:

                return JsonResponse({
                    "error": "Invalid Authorization header format"
                }, status=401)

        # Browser Users (Django Session)
        else:

            token = request.session.get("access_token")

            if not token:

                return JsonResponse({
                    "error": "Authentication required"
                }, status=401)

        try:

            payload = validate_jwt(token)

            request.jwt_payload = payload

        except Exception as e:

            return JsonResponse({
                "error": str(e)
            }, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper