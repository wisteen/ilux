from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('core.urls')),
    # path('auth/', include('account.urls')),

    # path('todo/', include('tas.urls')),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('api/', include('agreco_page.api_urls')),
    # path('page/', include('pages.urls')),
   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import handler400, handler403, handler404, handler500
from core.views import error_400_view, error_403_view, error_404_view, error_500_view, error_401_view

handler400 = error_400_view
handler403 = error_403_view
handler404 = error_404_view
handler500 = error_500_view
