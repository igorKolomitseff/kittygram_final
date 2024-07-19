from django.contrib import admin

from .models import Achievement, AchievementCat, Cat


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class AchievementCatInline(admin.TabularInline):
    model = AchievementCat
    extra = 1


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'birth_year', 'owner', 'get_achievements')
    search_fields = ('name', 'color', 'owner__username')
    list_filter = ('color', 'birth_year')
    list_select_related = ('owner',)
    readonly_fields = ('color',)
    inlines = (AchievementCatInline,)

    def get_queryset(self, request):
        return super().get_queryset(
            request
        ).prefetch_related(
            'achievements'
        )

    @admin.display(description='Достижения')
    def get_achievements(self, obj):
        return ', '.join(
            achievement.name for achievement in obj.achievements.all()
        )
