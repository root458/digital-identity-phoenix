from django.shortcuts import render, redirect
from .forms import CustomersWithFilesForm


def enroll(request):
        
    if not request.user.is_authenticated:
        return redirect(to='login')
    enroll_context = {
        'form': CustomersWithFilesForm
    }
    
    return render(request, 'enroll.html', enroll_context)

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