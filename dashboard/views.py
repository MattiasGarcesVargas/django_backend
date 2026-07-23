import requests
from django.conf import settings
from django.shortcuts import render


def index(request):
    total_responses = 0

    try:
        response = requests.get(settings.API_URL, timeout=10)
        response.raise_for_status()
        posts = response.json()
        total_responses = len(posts)
    except (requests.RequestException, ValueError):
        pass

    data = {
        "title": "Landing Page' Dashboard",
        "total_responses": total_responses,
    }

    return render(request, "dashboard/index.html", data)
