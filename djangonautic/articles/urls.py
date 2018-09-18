from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.articles_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail")
]
