import imp
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name="Home"),
    path("contact", views.contact, name="Contact"),
    path("message", views.message, name="Messsage"),
    path("start-up", views.work, name="Work")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
