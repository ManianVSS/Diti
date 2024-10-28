from rest_framework import serializers

from .models import Attachment, Tag, StepDefinition, StepDefinitionCategory


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public',
                  ]


class StepDefinitionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StepDefinitionCategory
        fields = ['id', 'parent', 'name', 'summary', 'description', 'parent', 'tags', 'org_group', 'created_at',
                  'updated_at', 'published', 'is_public', ]


class StepDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepDefinition
        fields = ['id', 'parent', 'name', 'summary', 'description', 'type', 'status', 'parameters', 'data', 'path',
                  'code', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
