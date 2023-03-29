from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<h1>Hello Django from <span style='color:red'>P10</span></h1>")
