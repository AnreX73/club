from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from therapy.models import User, ServiceCategory, Services, Graphics, Coaches, Post, ServicesGallery, PostGallery, \
    Gallery, Contacts, Commercial, Abonements


# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass


@admin.register(Graphics)
class GraphicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'gethtmlPhoto')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


class ServicesGalleryAdmin(admin.TabularInline):
    model = ServicesGallery
    fields = ('id', 'image', 'gethtmlPhoto', 'note', 'is_published')
    readonly_fields = ('gethtmlPhoto',)

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


class ServicesAdmin(admin.ModelAdmin):
    inlines = [ServicesGalleryAdmin]
    list_display = ('id', 'title', 'cat', 'gethtmlPhoto', 'price', 'is_published')
    list_display_links = ('id', 'cat', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'cat',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


@admin.register(Coaches)
class CoachesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'gethtmlPhoto', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


class PostGalleryAdmin(admin.TabularInline):
    model = PostGallery
    fields = ('id', 'image', 'gethtmlPhoto', 'note', 'is_published')
    readonly_fields = ('gethtmlPhoto',)

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


class PostAdmin(admin.ModelAdmin):
    inlines = [PostGalleryAdmin]
    list_display = ('id', 'post_cat', 'title','is_published',)
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'note', 'gethtmlPhoto', 'is_published')
    list_display_links = ('id', 'note', 'gethtmlPhoto',)
    list_editable = ('is_published',)
    search_fields = ('note',)
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


@admin.register(Commercial)
class CommercialAdmin(admin.ModelAdmin):
    list_display = ('title', 'about', 'gethtmlPhoto', 'is_published')
    list_display_links = ('title', 'gethtmlPhoto')
    search_fields = ('title',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('about',)}
    save_on_top = True
    ordering = ('-pk',)

    def gethtmlPhoto(self, picture):
        if picture.icon:
            return mark_safe(f"<img src='{picture.icon.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


@admin.register(Abonements)
class AbonementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'service_link', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'service_link')
    list_editable = ('is_published',)
    save_on_top = True


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'annotations1', 'annotations2', 'gethtmlPhoto',)
    list_display_links = ('title', 'annotations1')
    search_fields = ('annotations1',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = 'миниатюра'


admin.site.register(Post, PostAdmin)
admin.site.register(Services, ServicesAdmin)

admin.site.site_header = 'THERAPY'
