import functools

from django.apps.registry import apps
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.core.exceptions import FieldDoesNotExist
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from import_export.admin import ImportExportModelAdmin
from massadmin.massadmin import MassEditMixin

from .models import Configuration, OrgGroup, get_database_name, MyGroup, MyUser


class CustomModelAdmin(MassEditMixin, ImportExportModelAdmin):
    save_as = True
    readonly_fields = ('id',)
    display_order = 999

    # ordering = ('-id',)

    # search_fields = ['name', 'summary', 'description', ]

    # noinspection PyProtectedMember
    def get_list_display(self, request):
        return [f.name for f in self.model._meta.get_fields() if f.concrete and
                not (f.many_to_many or f.one_to_many)]

    def has_view_permission(self, request, obj=None):
        if (request is None) or (obj is None) or (request.user is None) or request.user.is_superuser:
            return super().has_view_permission(request, obj)

        if request.user.is_anonymous:
            try:
                return hasattr(obj, 'can_read') and obj.can_read(request.user)
            except FieldDoesNotExist:
                return super().has_view_permission(request, obj)

        if super().has_view_permission(request, obj):
            try:
                return not hasattr(obj, 'can_read') or obj.can_read(request.user)
            except FieldDoesNotExist:
                return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if (request is None) or (obj is None) or (request.user is None) or request.user.is_superuser:
            return super().has_change_permission(request, obj)
        if super().has_change_permission(request, obj):
            try:
                return not hasattr(obj, 'can_modify') or obj.can_modify(request.user)
            except FieldDoesNotExist:
                return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if (request is None) or (obj is None) or (request.user is None) or request.user.is_superuser:
            return super().has_delete_permission(request, obj)
        if super().has_delete_permission(request, obj):
            try:
                return not hasattr(obj, 'can_delete') or obj.can_delete(request.user)
            except FieldDoesNotExist:
                return True
        else:
            return False

    # Allow only listing of entities that can be viewed by the user
    def get_queryset(self, request):
        if request.user is None:
            return super().get_queryset(request)
        else:
            if ((request.method == 'GET')
                    and not request.path.endswith('/change/')
                    and hasattr(self.model, 'get_list_query_set')):
                return self.model.get_list_query_set(self.model, request.user)
            else:
                return super().get_queryset(request)


class CustomAdminSite(AdminSite):
    def __init__(self, name="admin"):
        super().__init__(name)
        self.model_ordering = {}
        # self.reload_admin_site_name()

    def register(self, model_or_iterable, admin_class=None, **options):
        super().register(model_or_iterable, admin_class, **options)

        display_order = 1
        if hasattr(admin_class, 'display_order') and admin_class.display_order:
            display_order = admin_class.display_order

        if hasattr(model_or_iterable, '__iter__'):
            self.model_ordering.update({str(k): display_order for k in model_or_iterable})
        else:
            self.model_ordering[str(model_or_iterable)] = display_order

    def _build_app_dict(self, request, label=None):
        app_dict = super()._build_app_dict(request, label)

        for app_label in app_dict.keys():
            app_config = apps.get_app_config(app_label)
            app_dict[app_label]['order'] = app_config.order if hasattr(app_config, 'order') else 'zzzzzzzzzzzzzzzzzzzzz'

        return app_dict

    def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: (x['order'], x['name']))

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: (self.model_ordering[str(x['model'])], x['name']))

        return app_list

    def reload_settings(self, database_name=None):
        if database_name is None:
            database_name = "Diti Test Management"

            # noinspection PyBroadException
            try:
                database_name = get_database_name()
            except Exception:
                print("Defaulting site name Diti as no site_setting data found")

        self.site_header = database_name + " Administration"
        self.site_title = database_name + " Admin Portal"
        self.index_title = "Welcome to " + database_name + " Administration Portal"


# Create a custom admin site with custom ordering
admin.site.unregister(Group)
admin.site.unregister(User)

site = CustomAdminSite()
admin.site = site
orig_register = admin.register
admin.register = functools.partial(orig_register, site=site)


@admin.register(MyGroup)
class CustomGroupAdmin(CustomModelAdmin, GroupAdmin):
    display_order = 'b'


@admin.register(MyUser)
class CustomUserAdmin(CustomModelAdmin, UserAdmin):
    display_order = 'c'
    pass


@admin.register(Configuration)
class ConfigurationAdmin(CustomModelAdmin):
    search_fields = ['name', 'value', 'description', ]
    ordering = ('name',)
    list_display = ['name', 'value', 'description', ]
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
    )
    display_order = 'a'


# noinspection PyUnusedLocal
@receiver(post_save, sender=Configuration, dispatch_uid="update_admin_site_name")
def update_admin_site_name(sender, instance, **kwargs):
    site.reload_settings()


@admin.register(OrgGroup)
class OrgGroupAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        ('leaders', RelatedOnlyFieldListFilter),
        ('members', RelatedOnlyFieldListFilter),
        ('guests', RelatedOnlyFieldListFilter),
        ('consumers', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 'd'