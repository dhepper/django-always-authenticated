from django.conf.urls import url
from django.http import HttpResponse


def dummy_view(request):
    return HttpResponse('%s' % request.user.username)

urlpatterns = [
    url(r'^$', dummy_view),
]
