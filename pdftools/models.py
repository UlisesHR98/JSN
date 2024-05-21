# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.
class CJAliasDocument(models.Model):
    file_hash = models.CharField(max_length=255)

class SCDobDocument(models.Model):
    file_hash = models.CharField(max_length=255, db_index=True)
    judgment_num = models.CharField(max_length=25, db_index=True)
    party_name = models.CharField(max_length=50)
    party_dob = models.CharField(max_length=25)
    party_ssn = models.CharField(max_length=25, default=None, null=True)
    party_dlicense = models.CharField(max_length=50, default=None, null=True)

    class Meta:
        unique_together = ('judgment_num', 'party_name')