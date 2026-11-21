import json
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Link

# Create your views here.
def redirect_link(request, code):
    link = get_object_or_404(Link, code=code)
    link.clicks += 1
    link.save()
    return redirect(link.original_url)
@csrf_exempt
@require_POST
def create_link(request):
    data = json.loads(request.body)
    url = data.get("url", "")
    try:
        URLValidator(schemes=["http", "https"])(url)
    except ValidationError:
        return JsonResponse({"error": "Invalid URL"}, status=400)
    link = Link.objects.create(original_url=url)
    return JsonResponse(
        {
            "code": link.code,
            "short_url": request.build_absolute_uri(f"/{link.code}")
        },
        status=201, 
    )
def link_stats(request, code):
    link = get_object_or_404(Link, code=code)
    return JsonResponse(
        {
            "code": link.code,
            "original_url": link.original_url,
            "clicks": link.clicks,
            "created at": link.created_at,
            
        }
    )