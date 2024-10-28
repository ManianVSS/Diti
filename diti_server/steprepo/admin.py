from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from core.admin import CustomModelAdmin
from .models import Attachment, Tag, StepDefinition, StepDefinitionCategory


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


@admin.register(StepDefinitionCategory)
class StepDefinitionCategoryAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 3


@admin.register(StepDefinition)
class StepDefinitionAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
        'type',
        'status',
    )
    search_fields = ['name', 'summary', 'description', 'path', 'code', ]
    display_order = 4
