from django.contrib import admin
from django.utils.html import format_html
from .models import Order, Customer


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'total_price',
        'colored_status',
        'created_at',
    )

    list_filter = ('status', 'created_at')
    search_fields = ('customer_name',)
    ordering = ('-created_at',)

    actions = ['mark_new','mark_ready', 'mark_done']


    def colored_status(self, obj):
        colors = {
            'new': 'orange',
            'ready': 'green',
            'done': 'gray',
        }
        return format_html(
            '<b style="color:{}">{}</b>',
            colors.get(obj.status, 'black'),
            obj.get_status_display()
        )

    colored_status.short_description = 'Статус'

    @admin.action(description='Новый заказ')
    def mark_new(self, request, queryset):
        queryset.update(status='new')

    @admin.action(description='Отметить как ГОТОВО')
    def mark_ready(self, request, queryset):
        queryset.update(status='ready')

    @admin.action(description='Отметить как ЗАВЕРШЕНО')
    def mark_done(self, request, queryset):
        queryset.update(status='done')
