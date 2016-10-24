from django.conf.urls import url

from . import views

app_name = 'code'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<code_id>........)/', views.view_code, name='code'),
]
