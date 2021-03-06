from django.db import models

# Create your models here.

from django.db import models


class Districts(models.Model):
    district_id = models.FloatField(db_column='DistrictID', blank=True, null=True)
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)
    locale = models.CharField(db_column='Locale', max_length=255, blank=True, null=True)
    pct_black_hispanic = models.FloatField(db_column='Pct_ethnicity', blank=True, null=True)
    county_connection = models.FloatField(db_column='County_connection', blank=True, null=True)
    pp_total_raw = models.FloatField(db_column='PP_total_raw', blank=True, null=True)

    class Meta:
        db_table = "district_info"


class ProductsInfo(models.Model):
    lpid = models.IntegerField(db_column='Lpid', blank=True, null=True)
    url = models.CharField(db_column="URL", max_length=255, blank=True, null=True)
    product_name = models.CharField(db_column='Product_Name', max_length=255, blank=True, null=True)
    provider_name = models.CharField(db_column='Provider', max_length=255, blank=True, null=True)
    sector = models.CharField(db_column='Sector', max_length=255, blank=True, null=True)
    primary_essential = models.CharField(db_column='Primary_Essential_Function', max_length=255, blank=True, null=True)

    class Meta:
        db_table = "products_info"


class EngagementInfo(models.Model):
    time = models.CharField(db_column='Time',max_length=255, blank=True, null=True)
    lp_id = models.IntegerField(db_column="Lp_id",blank=True, null=True)
    pct_access = models.FloatField(db_column='Pct_access', blank=True, null=True)
    engagement_index = models.FloatField(db_column='Engagement_index', blank=True, null=True)

    class Meta:
        db_table = "engagement_info"
