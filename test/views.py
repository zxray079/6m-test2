import time

from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_welcome_email_task


@api_view(["GET"])
def     stats_view(request):
        cache_key = "api_stats"


        cached_data = cache.get(cache_key)

        if cached_data is not None: 
            return Response({
        "source": "cache",
        "data": cached_data,
        })

        time.sleep(2)

        stats = {
         "users_count": 1000,
        "active_orders": 42,
        }

        cache.set(cache_key, stats, timeout=60)

        return Response({
          "source": "computed",
           "data": stats,
        })

@api_view(["POST"])
def register_view(request):
    email = request.data.get("email")

    if not email:
        return Response(
            {"error": "Email is required"},
            status=400,
        )

    send_welcome_email_task.delay(email)

    return Response(
        {
            "message": "Registration accepted",
            "email": email,
        },
        status=201,
    )
@api_view(["POST"])
def register_view(request):
    email = request.data.get("email")

    if not email:
        return Response(
            {"error": "Email is required"},
            status=400,
        )

    send_welcome_email_task.delay(email)

    return Response(
        {
            "message": "Registration accepted",
            "email": email,
        },
        status=201,
    )