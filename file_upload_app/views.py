# file_upload_app/views.py

from django.shortcuts import render, redirect,get_object_or_404 
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, FileUploadForm, FileShareForm 
from django.db import IntegrityError 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login
from .models import UploadedFile 
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})  

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('file_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False) 
            try:
                uploaded_file.user = request.user
                uploaded_file.save()
                return redirect('file_list')
            except IntegrityError as e:
                form.errors['__all__'] = form.error_class(["An error occurred while saving the file."])
                return render(request, 'file_upload_app/file_upload.html', {'form': form})
    else:
        form = FileUploadForm()

    return render(request, 'file_upload_app/file_upload.html', {'form': form})

@login_required
def file_list(request):
    user_files = UploadedFile.objects.filter(user=request.user)
    shared_files = UploadedFile.objects.all()
    return render(request, 'file_upload_app/file_list.html', {'user_files': user_files, 'shared_files': shared_files})

def user_search(request):
    query = request.GET.get('query', '')
    users = User.objects.filter(username__icontains=query)
    return render(request, 'file_upload_app/user_search.html', {'users': users, 'query': query}) 
# file_upload_app/views.py

def file_share(request, file_id):
    file_to_share = get_object_or_404(UploadedFile, pk=file_id)

    if request.user == file_to_share.user:
        if request.method == 'POST':
            form = FileShareForm(request.POST)
            if form.is_valid():
                shared_with_users = form.cleaned_data['shared_with']
                file_to_share.shared_with.set(shared_with_users)
                file_to_share.save()
                return redirect('file_list')
        else:
            form = FileShareForm()
        return render(request, 'file_upload_app/file_share.html', {'form': form, 'file_to_share': file_to_share})
    else:
        # Handle unauthorized access to sharing
        return HttpResponseForbidden("You don't have permission to share this file.")


