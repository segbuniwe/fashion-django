import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout
from .models import CustomUser
from .encoders import CustomUserEncoder


@require_http_methods(['POST'])
def signup(request):
    try:
        content = json.loads(request.body)
        user = CustomUser.objects.create(
            email=content.get('email'),
            password=content.get('password'),
            first_name=content.get('first_name'),
            last_name=content.get('last_name')
        )
        serialized_user = CustomUserEncoder().encode(user)
        return JsonResponse(
            serialized_user,
            encoder=CustomUserEncoder,
            safe=False,
        )
    except TypeError:
        return JsonResponse(
            {'message': 'Invalid key name'},
            status=400,
        )


@require_http_methods(['POST'])
def login_view(request):
    content = json.loads(request.body)
    email = content.get('email')
    password = content.get('password')
    user = CustomUser.objects.get(email=email, password=password)
    if user is not None:
        login(request, user)
        serialized_user = CustomUserEncoder().encode(user)
        return JsonResponse(
            json.loads(serialized_user),
            safe=False,
        )
    else:
        return JsonResponse(
            {'error': 'Invalid email or password'},
            status=400
        )


@require_http_methods(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse(
        {'message': 'User logged out'},
        status=200,
    )
