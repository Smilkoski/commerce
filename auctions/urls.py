from django.conf.urls.static import static
from django.urls import path

from commerce import settings
from .views import (
    ListingListView,
    ListingCreateView,
    ListingDetailView,
    login_view,
    logout_view,
    register,
    WatchlistListView,
)

urlpatterns = [
    path("", ListingListView.as_view(), name="index"),
    path("create/", ListingCreateView.as_view(), name="create"),
    path("detail/<int:pk>", ListingDetailView.as_view(), name="detail_listing"),
    path("watchlist/<int:pk>", WatchlistListView.as_view(), name="watchlist"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
