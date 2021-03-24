from django.shortcuts import render

def cv_list(request):
    return render(request, 'cvapp/cv_list.html',{})
