
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api/v1/', include('interact_space.posts_bridge_core.urls')),
    # path('api/v1/', include('interact_space.users_bridge_core.urls')),
    # path('api/v1/', include('interact_space.reactify_bridge_core.urls')),
    # path('api/v1/', include('interact_space.stories_bridge_core.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)