from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hello!</h1><p>New videos will be uploaded soon.</p>")
