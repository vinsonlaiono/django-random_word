from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1

    context = {
        "random_string": get_random_string(length=14),
        "count": request.session['count']
    }
    print('this is index')
    return render(request, "first_app/index.html", context)

def delete(request):
    print( 'thi isdelete')
    request.session['count'] = 0
    return redirect('/')
