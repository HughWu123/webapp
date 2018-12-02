from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from locations.models import Post

urlpatterns = [url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("name")[:25],
                                    template_name="locations/locations.html"))]