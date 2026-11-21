from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)

admin.site.register(Link, LinkAdmin)        # λέει στο admin να εμφανίσει το Link ώστε να το διαχειρίζεσαι γραφικά
