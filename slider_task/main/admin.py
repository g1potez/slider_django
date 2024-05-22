from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe

from main.models import Slide
from filer.admin import PermissionAdmin
from filer.models import ThumbnailOption, Folder

@admin.register(Slide)
class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('my_order', 'image_tag', 'name')

    def image_tag(self, obj):
        return mark_safe('<div><img src="{0}" width="100" height="100" style="object-fit:contain" /></div>'.format(obj.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

PermissionAdmin.autocomplete_fields = ()
admin.site.unregister(ThumbnailOption)
