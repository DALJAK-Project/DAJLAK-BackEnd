from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="DALJAK API",  # 타이틀
        default_version='v1',  # 버전
        description="프로젝트 API 문서",  # 설명
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),

    path('admin/', admin.site.urls),
    path('v1/', include('posts.urls')),
    path("v1/users/", include("users.urls")),
    path('v1/', include('communities.urls')),
    path("", RedirectView.as_view(url='/admin/', permanent=True)),  # 기본주소 입력했을 때, /admin로 넘겨줌.
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
