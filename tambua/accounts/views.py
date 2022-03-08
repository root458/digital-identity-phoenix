import os
from uuid import uuid4
from validators import length, uuid
from .uploads.handle_file import upload
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Customers
from .biometrics.voice_auth import enroll as enroll_voice

container_names = ['photos', 'recordings', 'signatures', 'fingerprints']
cutomer_files_urls = []

def enroll(request):
    if not request.user.is_authenticated:
        return redirect(to='login')
    
    if request.method == 'POST':
        print(request.POST)
        fs = FileSystemStorage()
        
        for item in request.FILES.items():
            m=0
            myfile = request.FILES.get(item[0])
            filename = fs.save(myfile.name, myfile)
            if m != 1:
                uploaded_file_url = fs.url(filename)
                cutomer_files_urls.append(uploaded_file_url)
                upload(container_names[m], uploaded_file_url, uuid()+os.path.splitext(str(uploaded_file_url)))
            m += 1
        
        Customers.objects.create(
            customer_id = uuid4(length=15),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            customer_photo = request.POST.get(cutomer_files_urls[0]),
            customer_recording = enroll_voice(cutomer_files_urls[1][1]),
            customer_signature =  request.POST.get(cutomer_files_urls[2]),
            customer_fingerprint = request.POST.get(cutomer_files_urls[3]),
            # enrollment_date = models.DateField(auto_now=True)
        )
        
        # Add a success message
        
    return render(request, 'enroll.html')

def verify(request):
    if not request.user.is_authenticated:
        return redirect(to='login')
    verify_context = {
        
    }
    
    return render(request, 'verify.html', verify_context)

def records(request):
    if not request.user.is_authenticated:
        return redirect(to='login')
    records_context = {
        
    }
    return render(request, 'records.html', records_context)