# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Inventory(models.Model):

    #__Inventory_FIELDS__
    product_code = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(blank=True, null=True, default=timezone.now)
    total_price = models.IntegerField(null=True, blank=True)

    #__Inventory_FIELDS__END

    class Meta:
        verbose_name        = _("Inventory")
        verbose_name_plural = _("Inventory")


class Deliverynote(models.Model):

    #__Deliverynote_FIELDS__
    delivery_id = models.IntegerField(null=True, blank=True)
    product_code = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    patient_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    tin = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    delivery_no = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Deliverynote_FIELDS__END

    class Meta:
        verbose_name        = _("Deliverynote")
        verbose_name_plural = _("Deliverynote")


class Deliverynumber(models.Model):

    #__Deliverynumber_FIELDS__
    current_number = models.IntegerField(null=True, blank=True)

    #__Deliverynumber_FIELDS__END

    class Meta:
        verbose_name        = _("Deliverynumber")
        verbose_name_plural = _("Deliverynumber")



#__MODELS__END
