from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product

# Admin Action Functions
def change_rating(modeladmin, request, queryset):
	queryset.update(rating = 'e')

# Action description
change_rating.short_description = "Mark Selected Products as Excellent"


# ModelAdmin Class # DataFlair
class ProductA(admin.ModelAdmin):	
	list_display = ('name', 'description', 'mfg_date', 'rating')
	list_filter = ('mfg_date', )
	actions = [change_rating]


# DataFlair
admin.site.register(Product, ProductA)
admin.site.unregister(Group)

# DataFlair # Changing Admin header
admin.site.site_header = "DataFlair Django Tutorials"