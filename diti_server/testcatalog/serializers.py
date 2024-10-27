from rest_framework import serializers

from .models import Attachment, Tag, TestCase, TestCategory


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


class TestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCategory
        fields = ['id', 'parent', 'name', 'summary', 'description', 'parent', 'tags', 'org_group', 'created_at',
                  'updated_at', 'published', 'is_public', ]


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'parent', 'name', 'summary', 'description', 'tags', 'steps', 'org_group', 'created_at',
                  'updated_at', 'published', 'is_public', ]
