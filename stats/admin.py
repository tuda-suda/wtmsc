from django.contrib import admin

from .models import Vehicle, Battle


class VehicleInline(admin.TabularInline):
    model = Vehicle
    min_num = 1
    extra = 0


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_name',
        'tier',
        'BR',
        'class_',
        'is_premium'
    )
    list_filter = ('tier', 'class_')
    search_fields = ('^name', '^display_name')


@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    inlines = (VehicleInline, )
    list_display = (
        'gamemode',
        'is_victory',
        'sl_reward',
        'rp_reward',
        'activity',
        'match_date'
    )
    list_filter = ('gamemode', 'is_victory', 'with_premium')
    ordering = ('-match_date', )
