from django.shortcuts import render, redirect, get_object_or_404
from fileapp.forms import FileForm,SendFileForm
from fileapp.models import File
from django.views.generic import ListView
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import DeleteView



def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fileapp:upload_list')
    else:
        form = FileForm()
    return render(request, 'fileapp/upload_file.html', {'form': form})

def download_file(request, file_id):
    file = File.objects.get(pk=file_id)
    file.downloads += 1
    file.save()
    return render(request, 'fileapp/download_file.html', {'file': file})
    


def send_file_email(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if request.method == 'POST':
        form = SendFileForm(request.POST)
        if form.is_valid():
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
            return redirect('fileapp:upload_list')
    else:
        form = SendFileForm()
    return render(request, 'fileapp/send_file.html', {'form': form, 'file': file})

class FileListView(ListView):
    model = File
    template_name = 'fileapp/upload_list.html'
    context_object_name = 'files'
    ordering = ['title']
    paginate_by = 20

# class FileDeleteView(DeleteView):
#     model = File
#     success_url = reverse_lazy('upload_list')
#     template_name = 'fileapp/file_confirm_delete.html'
    
