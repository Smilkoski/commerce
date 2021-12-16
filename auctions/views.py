from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)

from .models import (
    User,
    Listing,
    Watchlist,
)


class ListingListView(ListView):
    model = Listing
    template_name = 'auctions/index.html'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_listings'] = Listing.objects.all()
        if self.request.user.is_authenticated:
            context['user_watchlist'] = [j.listing_id_id
                                         for j in Watchlist.objects.filter(user_id_id=self.request.user)]

        return context


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    template_name = 'auctions/create_listing.html'
    fields = ['title', 'description', 'price', 'image', 'category']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class ListingDetailView(DetailView):
    model = Listing
    template_name = 'auctions/detail_listing.html'


class WatchlistListView(ListView):
    model = Listing
    template_name = 'auctions/watchlist.html'
    context_object_name = 'listings'
    ordering = ['-date_created']

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs.get('pk'))
        return Watchlist.objects.filter(user_id_id=user.id)


@login_required(redirect_field_name='/login/')
def add_to_watchlist(request, user, listing):
    u = User.objects.get(id=user)
    l = Listing.objects.get(id=listing)

    wl = Watchlist(user_id=u, listing_id=l)
    wl.save()
    return redirect(reverse('index'))


@login_required(redirect_field_name='/login/')
def remove_from_watchlist(request, user, listing):
    Watchlist.objects.filter(user_id=user, listing_id=listing).first().delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
