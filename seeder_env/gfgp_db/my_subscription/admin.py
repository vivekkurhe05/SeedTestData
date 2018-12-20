from django.contrib import admin
from .models import Order, Subscription, AssessmentPurchase, AssessmentPackage


admin.site.register(Order)
admin.site.register(Subscription)
admin.site.register(AssessmentPackage)
admin.site.register(AssessmentPurchase)

