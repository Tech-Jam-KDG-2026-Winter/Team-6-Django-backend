from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    body = json.loads(request.body)
    username = body.get("username")
    password = body.get("password")

    return JsonResponse({
        "message": "login api reached",
        "username": username
    })
