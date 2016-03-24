from django.shortcuts import render

# Create your views here.
def index(request):
    context_data = {'Title': "Mijo Friend",
                    'Image': "",
                    'mydata': "ejemplo"}
    return render(request, 'registro/base.html', context_data)
