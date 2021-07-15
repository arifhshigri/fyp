from django.urls import path

from PIN.core import views as v

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
]
