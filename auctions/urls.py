from django.urls import path

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
