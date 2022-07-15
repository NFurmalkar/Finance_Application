from django import template
from finance.models import LoanModel,transactionModel,customerModel
register = template.Library()

@register.filter(name="getCustName")
def getCustName(value):
    #print("value id:",value,type(value))
    getCustName = LoanModel.objects.get(id=value.id)
    #print("get cust name is: ",getCustName.customerName.name)
    name = getCustName.customerName.name
    return name

@register.filter(name="getLoantName")
def getLoantName(value):
    #print("In templatetags value id:", value,type(value))
    getloanName = LoanModel.objects.filter(customerName=value)#.values_list('customerName')[0]
    #=>print(getloanName[0].customerName.name)
    #print(getloanName.customerName.name)
    #return getloanName.customerName.name
    return getloanName[0].customerName.name

@register.filter(name="custName")
def custName(value):
    #print(value)
    #print(value.id)
    val = value.id
    getName = customerModel.objects.get(id=val)
    return getName.name
