
from django.urls import path
from .views import pdf,notfound,index,test,download_file
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('404',notfound,name='404'),
    path('',index,name='home'),
    path('test/',test,name='test'),
    path('pdf/<str:id>',pdf,name='index'),
    path('download/', download_file),
     
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
