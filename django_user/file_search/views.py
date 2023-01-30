from django.shortcuts import render
# from django.db.models import Q
# from file_search.models import Files


# def searchposts(request):
#     if request.method == 'GET':
#         query= request.GET.get('q')

#         submitbutton= request.GET.get('submit')

#         if query is not None:
#             lookups= Q(title__icontains=query) | Q(content__icontains=query)

#             results= Files.objects.filter(lookups).distinct()

#             context={'results': results,
#                      'submitbutton': submitbutton}

#             return render(request, 'search.html', context)

#         else:
#             return render(request, 'search.html')

#     else:
#         return render(request, 'search.html')

def searchposts(request):
    query = request.GET.get('q')
    results = File.objects.filter(file_title__contains=query)
    return render(request,'search.html', {'results': results})

