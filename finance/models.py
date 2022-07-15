from django.db import models
import datetime

# Create your models here.
class signupModel(models.Model):
    firstName = models.CharField(max_length=90)
    lastName = models.CharField(max_length=90)
    email = models.EmailField()
    initialCapital = models.BigIntegerField(default=0)
    dob = models.DateTimeField(default=datetime.datetime.today())
    gender = models.CharField(max_length=50)
    password = models.CharField(max_length=90)

    def __str__(self):
        return self.email

class bankdetailModel(models.Model):
    profileId = models.ForeignKey(signupModel,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=90)
    bankName = models.CharField(max_length=90)
    ifscCode = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    branch = models.CharField(max_length=50)

class customerModel(models.Model):
    profileId = models.ForeignKey(signupModel,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=90)
    aadharNo = models.IntegerField()
    address = models.CharField(max_length=90)
    business = models.CharField(max_length=90)
    mobile = models.IntegerField()
    isapprove = models.BooleanField(default=False)

    def __str__(self):
        id = str(self.id)
        return id



class partnerModel(models.Model):
    profileId = models.ForeignKey(signupModel,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=90)
    initialAmount = models.IntegerField()
    mobile = models.IntegerField()
    address = models.CharField(max_length=90)

class LoanModel(models.Model):
    customerName = models.ForeignKey(customerModel,on_delete=models.CASCADE)
    transactionNo = models.IntegerField()
    amount = models.IntegerField()
    interest = models.IntegerField()
    interestAmount = models.IntegerField()
    Amountfinal = models.IntegerField()
    paidAmount = models.IntegerField()
    chequeNumber = models.IntegerField(null=True,blank=True,default=00)
    Udays = models.IntegerField()
    todayDate = models.DateTimeField()
    expectedDay = models.DateTimeField()
    morgage = models.CharField(max_length=90,default="")
    guaranteePerson = models.CharField(max_length=90,default="")
    approve = models.BooleanField(default=False)
    iscompleted = models.BooleanField(default=False)

    def __str__(self):
        id = str(self.id)
        return id

class transactionModel(models.Model):
    customerId = models.ForeignKey(LoanModel,on_delete=models.CASCADE)
    transactionNo = models.IntegerField()
    dailyAmount = models.IntegerField()
    paidAmount = models.IntegerField()
    paidDate = models.DateTimeField(default=datetime.datetime.today)

