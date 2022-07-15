"""FinanceProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finance import views

from finance.middleware import VerifyMiddleware

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signin),
    path('signin/',views.signup),
    path('forget/', views.forgetpassword),
    path('home/',VerifyMiddleware(views.home)),
    path('bankdetail/',VerifyMiddleware(views.bankdetail)),
    path('bankdetailupdate/<id>',VerifyMiddleware(views.updatBankDetail)),
    path('deletedetail/<id>',VerifyMiddleware(views.deleteBankDetail)),
    path('customer/',VerifyMiddleware(views.customer)),
    path('customerupdate/<id>',VerifyMiddleware(views.customerUpdate)),
    path('customerdelete/<id>',VerifyMiddleware(views.customerDelete)),
    path('partner/',VerifyMiddleware(views.partner)),
    path('partnerupdate/<id>',VerifyMiddleware(views.partnerUpdate)),
    path('partnerdelete/<id>',VerifyMiddleware(views.partnerDelete)),
    path('loan/',VerifyMiddleware(views.loan)),
    path('loanUpdate/<id>',VerifyMiddleware(views.updateLoan)),
    path('loanDelete/<id>',VerifyMiddleware(views.loanDelete)),
    path('loanApprove/<id>',VerifyMiddleware(views.loanApprove)),
    path('transication/',VerifyMiddleware(views.transication)),
    path('transication/<id>',VerifyMiddleware(views.transicationName)),
    path('approveLoan/',views.approveLoan),
    path('completedLoan/',views.completedLoan),

]
