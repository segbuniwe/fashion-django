from .models import CustomUser
from .json import ModelEncoder


class CustomUserEncoder(ModelEncoder):
    model = CustomUser
    properties = [
        'id',
        'email',
        'first_name',
        'last_name',
        'date_joined',
        'is_active',
        'is_staff'
    ]
