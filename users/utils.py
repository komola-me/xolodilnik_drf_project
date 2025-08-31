from datetime import datetime, UTC, timedelta
import jwt

from django.conf import settings

def generate_confirmation_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.now(UTC) + timedelta(hours=1),
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)