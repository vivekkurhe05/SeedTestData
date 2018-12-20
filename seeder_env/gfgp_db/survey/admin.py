from django.contrib import admin
from .models import Survey, SurveyArea, SurveySection, SurveyQuestion


admin.site.register(Survey)
admin.site.register(SurveyArea)
admin.site.register(SurveySection)
admin.site.register(SurveyQuestion)
