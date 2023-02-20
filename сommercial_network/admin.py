from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from сommercial_network.models import Product, Company, Network


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ Админ-панель для работы с моделями приложения network """
    list_display = ('name', 'type', 'provider_link', 'debt', 'city')
    list_filter = ('city',)
    readonly_fields = ('created_date',)
    fieldsets = [
        (None, {'fields': ['hierarchy', 'name', 'type', 'network', 'provider', 'debt']}),
        ('Контактная информация', {'fields': ['email', 'country', 'city', 'street', 'building_number']}),
        ('Информация',
         {'fields': ('created_date', 'products')})
    ]

    def provider_link(self, obj):
        """Поставщик """
        if obj.provider:
            url = reverse(
                'admin:retail_company_change',
                args=(obj.provider.id,)
            )

            return mark_safe(u'<a href="{0}">{1}</a>'.format(url, obj.provider))

    actions = ['clear_debt']

    @admin.action(description='Очиcтить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)


admin.site.register(Product)
admin.site.register(Network)
