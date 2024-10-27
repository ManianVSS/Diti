from core.views import default_search_fields, default_ordering, id_fields_filter_lookups, \
    string_fields_filter_lookups, exact_fields_filter_lookups, DitiOrgGroupObjectLevelPermission, \
    DitiOrgGroupViewSet, datetime_fields_filter_lookups, fk_fields_filter_lookups
from .models import Attachment, Tag, TestCase, TestCategory
from .serializers import AttachmentSerializer, TagSerializer, TestCaseSerializer, TestCategorySerializer


class AttachmentViewSet(DitiOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [DitiOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TagViewSet(DitiOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [DitiOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TestCategoryViewSet(DitiOrgGroupViewSet):
    queryset = TestCategory.objects.all()
    serializer_class = TestCategorySerializer
    permission_classes = [DitiOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'parent', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published',
                       'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TestCaseViewSet(DitiOrgGroupViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [DitiOrgGroupObjectLevelPermission]
    search_fields = default_search_fields + ['steps']
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }
