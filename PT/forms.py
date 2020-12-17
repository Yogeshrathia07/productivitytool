from django import forms
from .models import NOTE

class files(forms.ModelForm):
    class Meta:
        model = NOTE
        fields = '__all__'


