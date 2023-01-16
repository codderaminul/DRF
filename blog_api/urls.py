from django.urls import path,include
from blog_api import views
from blog_api.views import PostList,PostDetail

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(),name='detailcreate'),
    path('', PostList.as_view(),name='listcreate'),
]
