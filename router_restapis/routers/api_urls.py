from django.urls import path, include,  re_path
from routers.api_views import RouterCreateAPIView, RouterUpdateAPIView, RouterListBasedonTypeAPIView, DeleteRouterAPIView, RouterListBasedonIPrangeAPIView

urlpatterns = [

    path('create/', RouterCreateAPIView.as_view()),
    path('update/', RouterUpdateAPIView.as_view()),
    path('list-by-type/', RouterListBasedonTypeAPIView.as_view()),
    path('list-by-ip-range/', RouterListBasedonIPrangeAPIView.as_view()),
    path('delete/', DeleteRouterAPIView.as_view()),

]