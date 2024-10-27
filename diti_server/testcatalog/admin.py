from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from core.admin import CustomModelAdmin
from .models import Attachment, Tag, TestCase, TestCategory


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    display_order = 1


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 2


@admin.register(TestCategory)
class TestCategoryAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 5


@admin.register(TestCase)
class TestCaseAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'steps', ]
    display_order = 6
