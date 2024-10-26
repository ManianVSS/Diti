from django.conf.urls.static import static
from django.urls import include, path
from django.urls import re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from core import admin
from . import settings

schema_view = get_schema_view(title='Diti API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
                  # Admin plugins and other libraries
                  path('admin/', include('massadmin.urls')),
                  path('admin/', admin.site.urls),
                  # For Advanced filters path('advanced_filters/', include('advanced_filters.urls')),

                  # Modules
                  path('api/', include('core.urls')),
                  path('steprepo/', include('steprepo.urls')),

                  # Swagger
                  path('swagger/', schema_view, name='docs'),

                  # Trap code access (?(py|sh|bat|htaccess))
                  re_path('(^.*[.](py|sh|bat|htaccess)$)',
                          TemplateView.as_view(template_name='errors/forbidden.html')),

                  re_path(
                      '(^(?!(data|admin|swagger|api|steprepo)).*$)',
                      TemplateView.as_view(template_name='index.html')),
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATICFILES_DIRS) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
