from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Userbase(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class Cppp(models.Model):
    tenderRefNum = models.IntegerField()
    tenderID = models.CharField(max_length=50)
    tenderTitle = models.CharField(max_length=50)
    tenderCategory = models.CharField(max_length=50, choices=[('Goods', 'Goods'), ('Services', 'Services'), ('Works', 'Works')])
    tenderFeeType = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    tenderFee = models.IntegerField()
    tenderValue = models.IntegerField()
    emdType = models.CharField(max_length=50, choices=[('Percentage', 'Percentage'), ('Fixed', 'Fixed')])
    emd = models.IntegerField()
    techBidOpeningDate = models.DateField()
    finBidOpeningDate = models.DateField()
    l1BidderName = models.CharField(max_length=50)
    contractAwardDate = models.DateField()
    l1BidderEmd = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    l1BidderEmdValue = models.IntegerField()
    l1BidderBg = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    l1BidderBgValue = models.IntegerField()
    paymentOptions = models.CharField(max_length=50, choices=[('10%', '10%'), ('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('90%', '90%'), ('100%', '100%')])


class Gem(models.Model):
    gemRefNum = models.IntegerField()
    gemBidID = models.CharField(max_length=50)
    gemTitle = models.CharField(max_length=50)
    gemCategory = models.CharField(max_length=50, choices=[('Goods', 'Goods'), ('Services', 'Services')])
    gemFeeType = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    gemFee = models.IntegerField()
    gemValue = models.IntegerField()
    emdType = models.CharField(max_length=50, choices=[('Percentage', 'Percentage'), ('Fixed', 'Fixed')])
    emd = models.IntegerField()
    techBidOpeningDate = models.DateField()
    finBidOpeningDate = models.DateField()
    l1BidderName = models.CharField(max_length=50)
    contractAwardDate = models.DateField()
    l1BidderEmd = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    l1BidderEmdValue = models.IntegerField()
    l1BidderBg = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    l1BidderBgValue = models.IntegerField()
    paymentOptions = models.CharField(max_length=50, choices=[('10%', '10%'), ('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('90%', '90%'), ('100%', '100%')])
