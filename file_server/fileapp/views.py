from django.shortcuts import render, redirect, get_object_or_404
from fileapp.forms import FileForm,SendFileForm
from fileapp.models import File
from django.views.generic import ListView
from django.core.mail import EmailMessage




def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {'form': form})

def download_file(request, file_id):
    file = File.objects.get(pk=file_id)
    if file is None:
        print("file not found")
    file.downloads += 1
    file.save()
    return render(request, 'download_file.html', {'file': file})
    # return FileResponse(models.file, as_attachment=True)


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

class FileListView(ListView):
    model = File
    template_name = 'upload_list.html'
    context_object_name = 'files'
    ordering = ['title']
    paginate_by = 20


    
