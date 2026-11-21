from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Link

# Create your views here.
def redirect_link(request, code):
    link = get_object_or_404(Link, code=code)
    link.clicks += 1
    link.save()
    return redirect(link.original_url)