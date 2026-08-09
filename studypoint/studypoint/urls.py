
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cms.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="homepage"),
    path("filter/<int:topic_id>/", filter, name="filter"),
    path("search/", search,name="search"),
    path("login/",loginview,name="login"),
    path("logout/",logoutview,name="logout"),
    path("register/",register, name="register"),
    path("show/<int:content_id>", showPost, name="show"),
    path("show/<int:content_id>/comment/create", saveComment, name="saveComment"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
