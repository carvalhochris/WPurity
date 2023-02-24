from django.urls import include, path
from rest_framework import routers
from feed.views import WordPressViewSet

router = routers.DefaultRouter()
router.register(r'wordpress', WordPressViewSet, basename='wordpress')

urlpatterns = [
    path('', include(router.urls)),
    # path('admin/', admin.site.urls),
]

