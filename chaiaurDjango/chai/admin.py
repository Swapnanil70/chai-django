from django.contrib import admin
from .models import ChaiVariety, ChaiReview, ChaiCertificate, Store

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    # Read docs about list_display : https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline] # ChaiReviewInline er sathe ChaiVariety er sathe
    # Ref : https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'chai')
    

# Admin e login kore models gulo dekha jabe. 
admin.site.register(ChaiVariety, ChaiVarietyAdmin)  
admin.site.register(ChaiReview)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
admin.site.register(Store, StoreAdmin)