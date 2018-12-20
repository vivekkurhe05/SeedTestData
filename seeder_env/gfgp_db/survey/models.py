from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from users.models import Organisation


LEVEL_CHOICES = (
    (1, 'Bronze'),
    (2, 'Silver'),
    (3, 'Gold'),
    (4, 'Platinum'),
)


class Survey(models.Model):

    name = models.CharField(max_length=230, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SurveyArea(models.Model):

    name = models.CharField(max_length=230)
    number = models.IntegerField(unique=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.name


class SurveySection(models.Model):

    area = models.ForeignKey(SurveyArea, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name


class SurveyQuestion(models.Model):

    UPLOAD_TYPES = (
        ('policy', _('Policy')),
        ('procedure', _('Procedure')),
        ('process', _('Process')),
    )

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    section = models.ForeignKey(SurveySection, on_delete=models.PROTECT, default=None)
    name = models.TextField()
    notes = models.TextField(blank=True)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    question_number = models.IntegerField(validators=[MinValueValidator(1)])
    upload_type = models.CharField(max_length=255, blank=True, choices=UPLOAD_TYPES)
    reference = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.name


# class SurveyResponse(models.Model):
#
#     organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='responses')
#     created = models.DateTimeField(auto_now=True, editable=False)
#     modified = models.DateTimeField(auto_now=True)
#     submitted = models.DateTimeField(editable=False, null=True)
#     level = models.IntegerField(
#         verbose_name=_('target tier'),
#         choices=LEVEL_CHOICES,
#         blank=True,
#     )
#
#     def __str__(self):
#         return "{}".format(self.submitted)
