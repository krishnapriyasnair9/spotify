from django.urls import path
from user import views
urlpatterns=[
        path("accounts/ehome",views.UserHomeView.as_view(),name="usr-home"),
        path("accounts/signup",views.SignUpView.as_view(),name="signup"),
        path("accounts/signin",views.SignInView.as_view(),name="login"),
        path("songs/add",views.SongCreateView.as_view(),name="add-song"),
        path("songs/all",views.UserSongListView.as_view(),name="usr-listsong"),
        path("songs/artists/add",views.ArtistsCreateView.as_view(),name="add-artists"),
        path("artits/all", views.UserArtistsListView.as_view(), name="usr-listartits"),

]