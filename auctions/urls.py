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
    CategoryListView,
    add_to_watchlist,
    remove_from_watchlist,
    detail,
)

urlpatterns = [
    path("", ListingListView.as_view(), name="index"),
    path("create/", ListingCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", detail, name="detail_listing"),
    path("watchlist/<int:pk>/", WatchlistListView.as_view(), name="watchlist"),
    path("category/<str:category>/", CategoryListView.as_view(), name="category"),
    path("add_to_watchlist/<int:user>/<int:listing>/", add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<int:user>/<int:listing>/", remove_from_watchlist, name="remove_from_watchlist"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
