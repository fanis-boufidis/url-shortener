from django.contrib import admin   # εργαλεία του admin panel
from .models import Link           # φέρνει το Link από το models.py του ίδιου φακέλου (η τελεία = "από εδώ")

admin.site.register(Link)          # λέει στο admin να εμφανίσει το Link ώστε να το διαχειρίζεσαι γραφικά
