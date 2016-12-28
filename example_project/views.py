from django.http import HttpResponse


def view(request):
    return HttpResponse("logged in as %s" % request.user)
