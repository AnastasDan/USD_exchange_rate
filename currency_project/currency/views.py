from datetime import datetime

from django.core.cache import cache
from django.utils import timezone

import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .constants import DATE, HOUR, TEN, URL


@api_view(["GET"])
def get_current_usd(request):
    """Получение текущего курса доллара к рублю."""
    last_time = cache.get("last_time")
    current_time = timezone.now()

    if not last_time:
        last_time = datetime(1970, 1, 1, tzinfo=timezone.utc)

    difference_time = (current_time - last_time).seconds
    if difference_time < TEN:
        return Response(
            {"error": "Минимальная пауза между запросами - 10 секунд"},
            status=status.HTTP_429_TOO_MANY_REQUESTS,
        )

    try:
        response = requests.get(URL)
    except requests.exceptions.RequestException as error:
        return Response(
            {
                "error": f"Ошибка при получении курса доллара: {error}"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if response.status_code == status.HTTP_200_OK:
        cache.set("last_time", current_time, HOUR)
        data = response.json()
        usd_to_rub = data["Valute"]["USD"]["Value"]
        last_requests = cache.get("last_requests", [])
        last_requests.insert(
            0,
            {
                "timestamp": current_time.strftime(DATE),
                "usd_to_rub": usd_to_rub,
            },
        )
        cache.set("last_requests", last_requests[:TEN], HOUR)
        return Response(
            {"usd_to_rub": usd_to_rub, "last_requests": last_requests[:TEN]},
            status=status.HTTP_200_OK,
        )

    return Response(
        {"error": "Не удалось получить информацию о курсе доллара"},
        status=response.status_code,
    )
