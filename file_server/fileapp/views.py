from django.shortcuts import render, redirect, get_object_or_404
from fileapp.forms import FileForm
from fileapp.models import File
from django.views.generic import ListView
from django.core.mail import EmailMessage
from .forms import SendFileForm



def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})

def download_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    file.downloads += 1
    file.save()
    return render(request, 'download.html', {'file': file})

# class Upload_List(ListView):
#     model = File
#     template_name = "fileapp/upload_file.html"


from django.core.mail import EmailMessage
from django.core.files.base import File
from django.shortcuts import render, redirect
from fileapp.models import File
from .forms import SendFileForm

def send_file_email(request, file_id):
    if request.method == 'POST':
        form = SendFileForm(request.POST)
        if form.is_valid():
            file = get_object_or_404(File, pk=file_id)
            recipient_email = form.cleaned_data['recipient_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = EmailMessage(
                subject,
                message,
                'from@example.com',
                [recipient_email],
                ['bcc@example.com'],
                reply_to=['another@example.com']
            )
            email.attach_file(file.file.path)
            email.send()
            file.emails_sent += 1
            file.save()
            return redirect('home')
    else:
        form = SendFileForm()
    return render(request, 'send_file_email.html', {'form': form, 'file': file})



    
