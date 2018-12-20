from django.db import models
from django.utils import timezone


class Organisation(models.Model):
    SIZE = (
        ('0-10', '0 - 10'),
        ('11-50', '11 - 50'),
        ('51-250', '51 - 250'),
        ('250+', '250+'),
    )
    ANNUAL_EXPENDITURE = (
        ('0-20K', 'USD < 20K'),
        ('20K-100K', 'USD 20K - 100K'),
        ('100K-500K', 'USD 100K - 500K'),
        ('500K-5M', 'USD 500K - 5M'),
        ('5M-100M', 'USD 5M - 100M'),
        ('100M+', 'USD >100M'),
    )

    legal_name = models.CharField(max_length=255, unique=True,)
    known_as = models.CharField(max_length=30, blank=True, default='')
    acronym = models.CharField(max_length=30, blank=True, default='')
    parent_organisation = models.CharField(max_length=50, blank=True, default='')
    registration_number = models.CharField(max_length=60, default='', blank=True)
    iat_uid = models.CharField(max_length=255, blank=True, default='')
    # types = models.ManyToManyField(OrganisationType, blank=False)
    address_1 = models.CharField(max_length=255, default='')
    address_2 = models.CharField(max_length=255, default='', blank=True)
    city = models.CharField(max_length=30, default='')
    province = models.CharField(max_length=30, blank=True, default='')
    zip = models.CharField(max_length=15, blank=True, default='')
    po_box = models.CharField(max_length=30, blank=True, default='')
    landmark = models.CharField(max_length=30, blank=True, default='')
    size = models.CharField(max_length=30, default='', blank=True, choices=SIZE)
    annual_expenditure = models.CharField(max_length=30, default='', blank=True, choices=ANNUAL_EXPENDITURE)
    website = models.URLField(max_length=100, default='', blank=True)
    social_media = models.URLField(max_length=100, default='', blank=True)
    other_social_media = models.URLField(max_length=100, default='', blank=True)
    biography = models.TextField(default='', blank=True)
    terms_acceptance_date = models.DateTimeField(default=timezone.now)
    privacy_acceptance_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.legal_name


class User(models.Model):

    name = models.CharField(max_length=30)
    user_mobile = models.CharField(max_length=15)
    job_role = models.CharField(max_length=255, default='')
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name
