# I wrote this code

from .models import Status
from django import forms


class CreateStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('title', 'image', 'caption')

# end of code I wrote
