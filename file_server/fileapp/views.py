from django.shortcuts import render, redirect, get_object_or_404
from fileapp.forms import FileForm
from fileapp.models import File

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'fileapp/upload_file.html', {'form': form})

def download_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    file.downloads += 1
    file.save()
    return render(request, 'download_file.html', {'file': file})

    
