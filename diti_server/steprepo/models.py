from django.db import models
from django_yaml_field import YAMLField

from core.models import OrgModel, OrgGroup, PythonCodeField
from core.storage import CustomFileSystemStorage


class Attachment(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='step_repo_attachments')
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='automation', blank=False, null=False)


class Tag(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='step_repo_tags')
    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class StepDefinition(OrgModel):
    name = models.CharField(max_length=1024, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    parameters = YAMLField(null=True, blank=True)
    data = YAMLField(null=True, blank=True)
    code = PythonCodeField(null=True, blank=True)


class TestCase(OrgModel):
    name = models.CharField(max_length=1024, unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='test_cases', blank=True)
    steps = YAMLField(null=True, blank=True)
