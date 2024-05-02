from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Item, UserProfile, LikedItem
from .forms import ItemForm, UserCreationWithEmailForm
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.middleware.csrf import get_token



def index(request):
    sort_by = request.GET.get("sort", None)

    if sort_by == "popular":
        items = Item.objects.order_by("-view_count")
    elif sort_by == "newest":
        items = Item.objects.order_by("-created_at")
    elif sort_by == "liked":
        items = Item.objects.annotate(like_count=Count("liked_by")).order_by(
            "-like_count"
        )
    else:
        items = Item.objects.order_by("-created_at")

    return render(request, "marketplace/index.html", {"items": items})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    items = user.items.all()
    liked_items = user_profile.liked_items()  # 메서드 호출로 수정
    followers_count = user_profile.followed_by.count()
    following_count = user.following.count()
    return render(
        request,
        "marketplace/profile.html",
        {
            "user": user,
            "items": items,
            "liked_items": liked_items,
            "followers_count": followers_count,
            "following_count": following_count,
        },
    )

@login_required
def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    liked_items = Item.objects.filter(liked_by=request.user)
    item.view_count += 1
    item.save()
    return render(
        request,
        "marketplace/item_detail.html",
        {"item": item, "liked_items": liked_items},
    )


@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect("index")
    else:
        form = ItemForm()
    return render(request, "marketplace/add_item.html", {"form": form})


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ItemForm(instance=item)
    return render(request, "marketplace/edit_item.html", {"form": form, "item": item})


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("profile")
    return render(request, "marketplace/delete_item.html", {"item": item})


@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    user_profile = request.user.userprofile
    if (
        user_to_follow != request.user
        and user_to_follow not in user_profile.followed_by.all()
    ):
        user_profile.followed_by.add(user_to_follow)
    return redirect("profile", username=username)


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    user_profile = request.user.userprofile
    if user_to_unfollow in user_profile.followed_by.all():
        user_profile.followed_by.remove(user_to_unfollow)
    return redirect("profile", username=username)


@login_required
def like_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.user not in item.liked_by.all():
        item.liked_by.add(request.user)
    return redirect("item_detail", item_id=item_id)


@login_required
def unlike_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.user in item.liked_by.all():
        item.liked_by.remove(request.user)
    return redirect("item_detail", item_id=item_id)


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                response_data = {"token": token.key, "csrf_token": get_token(request)}
                return redirect("index")
    return render(request, "accounts/login.html")
    
def custom_logout(request):
    logout(request)
    return redirect("index")


def custom_register(request):
    if request.method == "POST":
        form = UserCreationWithEmailForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                form.add_error('username', '이미 사용 중인 사용자 이름입니다.')
                return render(request, "accounts/register.html", {"form": form})
            if User.objects.filter(email=email).exists():
                form.add_error('email', '이미 사용 중인 이메일 주소입니다.')
                return render(request, "accounts/register.html", {"form": form})
            form.save()
            return redirect("login")
    else:
        form = UserCreationWithEmailForm()
    return render(request, "accounts/register.html", {"form": form})