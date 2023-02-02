from django.shortcuts import render

# Create your views here.
def searchposts(request):
    query = request.GET.get('q')
    posts = File.objects.filter(title__icontains=query)
    return render(request,'search.html')

