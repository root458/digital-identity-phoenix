from django.forms import ModelForm
from .models import CustomersWithFiles

class CustomersWithFilesForm(ModelForm):
    
    class Meta:
        model = CustomersWithFiles
        fields = [
            'first_name',
            'last_name',
            'customer_photo',
            'customer_recording',
            'customer_signature',
            'customer_fingerprint',
        ]