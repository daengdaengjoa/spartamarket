from django.urls import path, include
from articles import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<str:username>/", views.profile, name="profile"),
    # path('profile/', views.profile, name='profile'),
    path("item/<int:item_id>/", views.item_detail, name="item_detail"),
    path("item/add/", views.add_item, name="add_item"),
    path("item/<int:item_id>/edit/", views.edit_item, name="edit_item"),
    path("item/<int:item_id>/delete/", views.delete_item, name="delete_item"),
    path("user/<str:username>/follow/", views.follow_user, name="follow_user"),
    path("user/<str:username>/unfollow/", views.unfollow_user, name="unfollow_user"),
    path("item/<int:item_id>/like/", views.like_item, name="like_item"),
    path("item/<int:item_id>/unlike/", views.unlike_item, name="unlike_item"),
    path("accounts/login/", views.custom_login, name="login"),
    path("accounts/logout/", views.custom_logout, name="logout"),
    path("accounts/register/", views.custom_register, name="register"),
]
