from django.contrib import admin
from django.contrib.admin import site as admin_site
from django.contrib.admin.utils import unquote
from django.contrib.auth import get_user_model
from django.contrib.gis.admin import OSMGeoAdmin
from django.db.models import Q
from django import forms
from guardian import admin as guardian_admin
from image_cropping import ImageCroppingMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .base import CommonExcludeMixin, PopulateCreatedAndModifiedMixin
from resources.admin.period_inline import PeriodInline
from resources.models import Day, Reservation, Resource, ResourceImage, ResourceType, Unit, Purpose
from resources.models import Equipment, ResourceEquipment, EquipmentAlias, EquipmentCategory, TermsOfUse


class EmailAndUsernameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return '%s | %s' % (obj.email, obj.username) if obj.email else obj.username


class CustomUserManage(forms.Form):
    """
    Show only apikey and staff users in a dropdown on object permission manage page
    """
    user = EmailAndUsernameChoiceField(
        queryset=get_user_model().objects.filter(
            Q(auth_token__isnull=False) | Q(is_staff=True)
        ).distinct().order_by('email', 'username')
    )


class FixedGuardedModelAdminMixin(guardian_admin.GuardedModelAdminMixin):

    # fix editing an object with quoted chars in pk
    def obj_perms_manage_user_view(self, request, object_pk, user_id):
        return super().obj_perms_manage_user_view(request, unquote(object_pk), user_id)


class HttpsFriendlyGeoAdmin(OSMGeoAdmin):
    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js'


class DayInline(admin.TabularInline):
    model = Day


class ResourceEquipmentInline(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, TranslationStackedInline):
    model = ResourceEquipment
    fields = ('equipment', 'description', 'data')
    extra = 0


class ResourceAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, TranslationAdmin, HttpsFriendlyGeoAdmin):
    inlines = [
        PeriodInline,
        ResourceEquipmentInline,
    ]

    default_lon = 2776460  # Central Railway Station in EPSG:3857
    default_lat = 8438120
    default_zoom = 12


class UnitAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, FixedGuardedModelAdminMixin,
                TranslationAdmin, HttpsFriendlyGeoAdmin):
    inlines = [
        PeriodInline
    ]

    default_lon = 2776460  # Central Railway Station in EPSG:3857
    default_lat = 8438120
    default_zoom = 12

    def get_obj_perms_user_select_form(self, request):
        return CustomUserManage


class ResourceImageAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, ImageCroppingMixin, TranslationAdmin):
    exclude = ('sort_order', 'image_format')


class EquipmentAliasInline(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, admin.TabularInline):
    model = EquipmentAlias
    readonly_fields = ()
    exclude = CommonExcludeMixin.exclude + ('id',)
    extra = 1


class EquipmentAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, TranslationAdmin):
    inlines = (
        EquipmentAliasInline,
    )


class ResourceEquipmentAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, TranslationAdmin):
    fields = ('resource', 'equipment', 'description', 'data')


class ReservationAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            read_only_fields = list(super().get_readonly_fields(request, obj))
            read_only_fields.append('access_code')
            return tuple(read_only_fields)
        return super().get_readonly_fields(request, obj)


class ResourceTypeAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, TranslationAdmin):
    pass


class EquipmentCategoryAdmin(PopulateCreatedAndModifiedMixin, TranslationAdmin):
    pass


class PurposeAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, TranslationAdmin):
    pass


class TermsOfUseAdmin(PopulateCreatedAndModifiedMixin, CommonExcludeMixin, TranslationAdmin):
    pass


admin_site.register(ResourceImage, ResourceImageAdmin)
admin_site.register(Resource, ResourceAdmin)
admin_site.register(Reservation, ReservationAdmin)
admin_site.register(ResourceType, ResourceTypeAdmin)
admin_site.register(Purpose, PurposeAdmin)
admin_site.register(Day)
admin_site.register(Unit, UnitAdmin)
admin_site.register(Equipment, EquipmentAdmin)
admin_site.register(ResourceEquipment, ResourceEquipmentAdmin)
admin_site.register(EquipmentCategory, EquipmentCategoryAdmin)
admin_site.register(TermsOfUse, TermsOfUseAdmin)
