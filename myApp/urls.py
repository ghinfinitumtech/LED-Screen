from django.urls import path
from myApp.views import *
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.conf.urls.static import static

# urls.py
from django.urls import path
from .views import event_list, create_event,  delete_event

urlpatterns = [
    
   
    path('events/', event_list, name='event_list'),
    path('', create_event, name='create_event'),
    path('events/<int:event_id>/edit/', edit_event, name='edit_event'),
    path('events/<int:event_id>/delete/', delete_event, name='delete_event'),
]
# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


