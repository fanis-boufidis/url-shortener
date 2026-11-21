import secrets                  # βιβλιοθήκη για ασφαλή τυχαία νούμερα/χαρακτήρες (καλύτερη από το random για κωδικούς)
import string                   # έτοιμα σετ χαρακτήρων (γράμματα, ψηφία)
from django.db import models    # φέρνει τα εργαλεία του Django για μοντέλα/βάση

ALPHABET = string.ascii_letters + string.digits

def generate_code(length=6):
    return "".join(secrets.choice(ALPHABET) for _ in range(length)) #π.χ. "aB3xYz"

class Link(models.Model):
    original_url = models.URLField(max_length=2000)
    code = models.CharField(max_length=10, unique=True, default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0) 


    def __str__(self):          # ορίζει πώς "τυπώνεται" ένα Link (το βλέπεις στο admin)
        return f"{self.code} -> {self.original_url}"   # f-string: βάζει τις τιμές μέσα στο κείμενο, π.χ. "aB3xYz -> https://..."