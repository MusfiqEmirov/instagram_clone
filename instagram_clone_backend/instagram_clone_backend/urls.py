
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('interact_space.posts_bridge_core.urls.py')),
    path('api/v1/', include('interact_space.users_bridge_core.urls.py')),
    path('api/v1/', include('interact_space.reactify_bridge_core.urls.py')),
    path('api/v1/', include('interact_space.stories_bridge_core.urls.py')),
]
