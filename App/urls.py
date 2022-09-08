import imp
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name="Home"),
    path("contact", views.contact, name="Contact"),
    path("message", views.message, name="Messsage"),
    path("start-up", views.work, name="Work"),
    path('single-project/<str:pk>', views.single_project, name="Single_project"),



    path('login', views.sign_in, name="Login"),
    path("Logout", views.sign_out, name="Logout"),
    path("register", views.register, name="Register"),


    path('new-single-project/<str:pk>', views.new_single_project, name="Single")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
