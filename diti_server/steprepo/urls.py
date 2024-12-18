from django.urls import include, path
from rest_framework import routers

from .views import AttachmentViewSet, TagViewSet, StepDefinitionViewSet, StepDefinitionCategoryViewSet

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'step_definition_categories', StepDefinitionCategoryViewSet)
router.register(r'step_definitions', StepDefinitionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
