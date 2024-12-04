from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d = {
        'Name' : 'Alok Kumar',
        'Age' : 23
    }
    return render(request, 'index.html', context =d)
