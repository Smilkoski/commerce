from django.conf.urls.static import static
from django.urls import path

from commerce import settings
from .views import (
    ListingListView,
    ListingCreateView,
    login_view,
    logout_view,
    register,

)

urlpatterns = [
    path("", ListingListView.as_view(), name="index"),
    path("create/", ListingCreateView.as_view(), name="create"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
