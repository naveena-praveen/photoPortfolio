from django.contrib import admin
from .models import Work, Work_details,Art,LoveAndWar,LoveAndWarImage,Itswhatido,Exhibition,Awards,Bio
from django.utils.html import format_html


class WorkDetailsInline(admin.TabularInline):
    model = Work_details
    extra = 1 
    readonly_fields = ('id',) 
    fields = ('image', 'description') 

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  
    prepopulated_fields = {'slug': ('name',)}  
    inlines = [WorkDetailsInline] 
    search_fields = ('name',)  
    ordering = ('name',)


@admin.register(Work_details)
class WorkDetailsAdmin(admin.ModelAdmin):
    list_display = ('work', 'id','image', 'description',)  
    list_filter = ('work',)  
    search_fields = ('work__name', 'description')  
    readonly_fields = ('id',)

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'description')  
    readonly_fields = ('image_preview',)  

 
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:150px; height:auto; object-fit:cover; border-radius:5px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'

class LoveAndWarImageInline(admin.TabularInline):
    model = LoveAndWarImage
    extra = 3 
    
@admin.register(LoveAndWar)
class LoveAndWarAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_editable = ('is_active',)
    inlines = [LoveAndWarImageInline]

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            LoveAndWar.objects.filter(is_active=True).update(is_active=False)
        super().save_model(request, obj, form, change)
        


@admin.register(Itswhatido)
class ItswhatidoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            Itswhatido.objects.filter(is_active=True).exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            Exhibition.objects.filter(is_active=True).exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            Awards.objects.filter(is_active=True).exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            Bio.objects.filter(is_active=True).exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)
