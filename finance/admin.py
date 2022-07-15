from django.contrib import admin
from finance.models import signupModel,bankdetailModel,customerModel,partnerModel, LoanModel,transactionModel
# Register your models here.

class signupAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','lastName','email','initialCapital','dob','gender','password')
class bankdetailAdmin(admin.ModelAdmin):
    list_display = ['id','profileId','name','bankName','ifscCode','accountNumber','branch']
class customerAdmin(admin.ModelAdmin):
    list_display = ['id','profileId','name','aadharNo','address','business','mobile','isapprove']
class partnerAdmin(admin.ModelAdmin):
    list_display = ['id','profileId','name','initialAmount','mobile','address']
class loanAdmin(admin.ModelAdmin):
    list_display = ['id','customerName','transactionNo','amount','interest','interestAmount','Amountfinal','paidAmount','chequeNumber','Udays','todayDate','expectedDay','morgage','guaranteePerson','approve','iscompleted']

class transactionAdmin(admin.ModelAdmin):
    list_display = ['id','customerId','transactionNo','dailyAmount','paidAmount','paidDate']

admin.site.register(signupModel,signupAdmin)
admin.site.register(bankdetailModel,bankdetailAdmin)
admin.site.register(customerModel,customerAdmin)
admin.site.register(partnerModel,partnerAdmin)
admin.site.register(LoanModel,loanAdmin)
admin.site.register(transactionModel,transactionAdmin)
