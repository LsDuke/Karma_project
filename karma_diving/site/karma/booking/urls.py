#booking URLS.PY
from django.conf.urls import url
from . import views

app_name ='booking'

urlpatterns =[

    url(r'^new/$',views.CreateClientView.as_view(), name='create'),
    #joe est une limace slugify==> joe-est-une-limace

]
