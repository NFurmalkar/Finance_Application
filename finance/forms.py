from django import forms
from finance.models import signupModel,bankdetailModel,customerModel,partnerModel,LoanModel,transactionModel

class signupForm(forms.ModelForm):
    class Meta:
        model = signupModel
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }

class bankdetailForm(forms.ModelForm):
    class Meta:
        model = bankdetailModel
        fields = '__all__'

class customerForm(forms.ModelForm):
    class Meta:
        model = customerModel
        fields= '__all__'

class partnerForm(forms.ModelForm):
    class Meta:
        model = partnerModel
        fields = '__all__'

class LoanForm(forms.ModelForm):
    class Meta:
        model = LoanModel
        fields = '__all__'

class transactionForm(forms.ModelForm):
    class Meta:
        model = transactionModel
        fields='__all__'