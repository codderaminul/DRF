from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
import blog,blog_api,users
from blog import urls
from users import urls
from blog_api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blog.urls)),
    path('api/', include(blog_api.urls)),
    path('api/users/', include(users.urls)),
    path('api-auth/', include('rest_framework.urls',namespace="rest_framework")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




