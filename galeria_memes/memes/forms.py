"""
ModelForm del meme.
"""
from django import forms

from .models import Meme


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ["titulo", "url_imagen", "categoria", "descripcion", "publicado"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 3}),
            "url_imagen": forms.URLInput(attrs={"placeholder": "https://..."}),
        }

    def clean_url_imagen(self):
        url = self.cleaned_data["url_imagen"]
        if not url.lower().startswith("https://"):
            raise forms.ValidationError("La URL de la imagen debe empezar con https://")
        return url
