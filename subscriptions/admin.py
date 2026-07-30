from django.contrib import admin
from .models import SubscriptionPlan, Subscription, Product, ProductVariant, AccessScope

admin.site.register(SubscriptionPlan)
admin.site.register(Subscription)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(AccessScope)
