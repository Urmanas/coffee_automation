from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'total_price',
        'status',
        'created_at',
    )

    list_filter = ('status', 'created_at')
    search_fields = ('customer_name',)
    ordering = ('-created_at',)

    actions = ['mark_ready', 'mark_done']

    @admin.action(description='Отметить как ГОТОВО')
    def mark_ready(self, request, queryset):
        queryset.update(status='ready')

    @admin.action(description='Отметить как ЗАВЕРШЕНО')
    def mark_done(self, request, queryset):
        queryset.update(status='done')
