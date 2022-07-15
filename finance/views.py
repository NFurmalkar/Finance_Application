from django.shortcuts import render,redirect
from finance.forms import signupForm,bankdetailForm,customerForm,partnerForm,LoanForm,transactionForm
from finance.models import signupModel,bankdetailModel,customerModel,partnerModel,LoanModel,transactionModel
import datetime
import json
from django.core.mail import BadHeaderError,send_mail
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages

from django.http import HttpResponse
from django.db.models import Count,Sum
# Create your views here.

def getsessionEmail(email):
    getId=None
    try:
        getId = signupModel.objects.get(email=email)
    except:
        pass
    print(getId)
    return getId

def signin(request):
    try:
        del request.session['email']
        del request.session['password']
    except:
        pass
    request.session.clear()
    print(request.session.get('email'))
    #dataform = signupModel.objects.all().values("email","password")
    #conform_mail = signupModel.objects.filter(email='naf@gmail.com', password=123456)
    if request.method == 'POST':
        uemail = request.POST.get('uemail')
        upassword = request.POST.get('upassword')
        print("User mail is:",uemail)
        print("PAssword is:",upassword)
        conform_mail = signupModel.objects.filter(email=uemail,password=upassword)
        print(bool(conform_mail),conform_mail)
        if conform_mail:
            request.session['email'] = uemail
            request.session['password'] = upassword
            return redirect('/home')
        else:
            messages.error(request,'Incorrect email or password')
            return redirect('/')

    #error_msg = "Incorrect email & password"
    #data = {'error_msg':error_msg}
    return render(request,'finance/signin.html')

def signup(request):
    form = signupForm()
    error_msg=None
    if request.method == "POST":
        error_msg=None
        form = signupForm(request.POST)
        ufname = request.POST.get('firstName')
        ulname = request.POST.get('lastName')
        uemail = request.POST.get('email')
        ugender = request.POST.get('gender')
        password = request.POST.get('password')
        initialcapital = request.POST.get('initialCapital')
        print("Name", type(ufname), "Email", type(uemail), "password", type(password),type('initialCapital'),initialcapital)
        values = {'ufname':ufname,'ulname':ulname,'uemail':uemail,'initialCapital':initialcapital}
        data=None
        try:
            data = signupModel.objects.get(email=uemail)
        except:
            pass
        print("data is:",data)
        if data is not None:
            error_msg ="Email Id is already Register"

        if not error_msg:
            regform = signupModel(firstName=ufname,lastName=ulname,email=uemail,initialCapital=initialcapital ,gender=ugender,password=password)
            regform.save()
            #meg = f"Hi {ufname} {ulname},You have successfully login with our site.Thanky you login"
            #send_mails(uemail,meg)
            messages.success(request,"Successfully Register")
        else:
            data={'values':values,'error_msg':error_msg}
            return render(request,'finance/signup.html',data)

        """
        if form.is_valid():   
            values = {'ufname': ufname, 'ulname': ulname, 'uemail': uemail, 'udob': udob, 'ugender': ugender}
            #error_msg = validation(ufname,ulname,uemail,udob,ugender,password1,password2)
            getMailValue = len(uemail)-9
            #nf@gmail.com
            nameError = charvalid(ufname)
            lnameError = charvalid(ulname)
            if nameError:
                error_msg="first " + nameError
            elif lnameError:
                error_msg="last " + lnameError
            elif uemail[getMailValue:] != 'gmail.com':
                error_msg="Enter only google Email Address like **@gmail.com"
            elif len(password) <=5:
                error_msg="password contain number and alphabet or greater than 4"
            
            error_msg = "Already exists"
            if not error_msg:
                form.save()

                return redirect('/')
            else:
                print(error_msg)
                return render(request,'finance/signup.html',{'error_msg':error_msg,'values':values})
        """

    return render(request,'finance/signup.html', {'form':form})

def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('forgrEemail')
        print("Forget Password:",email)
        try:
            data = signupModel.objects.get(email=email)
        except:
            messages.error(request,"This Email is Not Exists")
            data = {'email':email}
            return render(request, 'finance/forgetpassword.html', data)
        #print("U R data is",data.email)
        #print("U R data is",data.password)
        db_email = data.email
        db_password = data.password
        msg = f"You Email Id is {db_email} and password is {db_password}"
        print("UR msg is:",msg)
        send_mails(email,msg)
        messages.success(request,"we sent you Password on Your Email!!!")
    return render(request,'finance/forgetpassword.html')

def home(request):
    global sumOfTotalCapital
    email = request.session.get('email')
    bankdetaildata = bankdetailModel.objects.filter(profileId__email=email).aggregate(Count('id'))  #{'id__count': 2}
    customerinfo = customerModel.objects.filter(profileId__email=email).aggregate(Count('id'))
    partnerinfo = partnerModel.objects.filter(profileId__email=email).aggregate(Count('id'))
    pendingLoan = LoanModel.objects.filter(iscompleted=False,approve=False).filter(customerName__profileId__email=email).aggregate(Count('id'))
    approvedLoan = LoanModel.objects.filter(approve=True).filter(customerName__profileId__email=email).aggregate(Count('id'),Sum('Amountfinal'))
    completedLoan = LoanModel.objects.filter(approve=True, iscompleted=True).filter(customerName__profileId__email=email).aggregate(Count('id'))
    totalApprovedLoan = LoanModel.objects.filter(approve=True, iscompleted=False).filter(customerName__profileId__email=email).aggregate(Count('id'))
    #print(totalApprovedLoan)
    totalCapital = signupModel.objects.filter(email=email).aggregate(Sum('initialCapital'))
    partnerinitialAmount = partnerModel.objects.filter(profileId__email=email).aggregate(Sum('initialAmount'))
    val = totalCapital.get('initialCapital__sum')
    val2 = partnerinitialAmount.get('initialAmount__sum')
    if val2 is None:
        val2 = 0
    #print(val2)
    print(val,val2,val+val2)
    sumOfTotalCapital = val+val2
    print("start sumOfTotalCapital:",sumOfTotalCapital)
    tdate = datetime.datetime.today()
    todayCollection = transactionModel.objects.filter(paidDate__month=tdate.month,paidDate__day=tdate.day,paidDate__year=tdate.year)\
                        .filter(customerId__customerName__profileId__email=email).aggregate(Sum('paidAmount'))
    #print("todayCollection:--->",todayCollection)
    sumOfApprove = approvedLoan.get('Amountfinal__sum')
    if sumOfApprove is None:
        sumOfApprove = 0
    print("sumOfApprove:",sumOfApprove)
    sumOfTotalCapital = sumOfTotalCapital - sumOfApprove
    print("after sumOfTotalCapital:", sumOfTotalCapital)
    #print("sumofApp",approvedLoan,"and sum is:",sumOfApprove,"after minus:",sumOfTotalCapital)

    transactionData = transactionModel.objects.filter(customerId__customerName__profileId__email=email).aggregate(Sum('paidAmount'))
    #print("transactionTodayData:",transactionData)
    sumOfTransaction = transactionData.get('paidAmount__sum')
    if sumOfTransaction is None:
        sumOfTransaction = 0
    print("sumOfTransaction",sumOfTransaction)
    #*************************************************************************************
    sumOfTotalCapital = sumOfTotalCapital + sumOfTransaction
    print("AfterTransaction sumOfTotalCapital: ",sumOfTotalCapital)

    data={'bankdetaildata':bankdetaildata,'customerinfo':customerinfo,'partnerinfo':partnerinfo,
          'pendingLoan':pendingLoan,'approvedLoan':approvedLoan,'completedLoan':completedLoan,'sumOfTotalCapital':sumOfTotalCapital,
          'todayCollection':todayCollection,'totalApprovedLoan':totalApprovedLoan}

    return render(request,'finance/home.html',data)

def send_mails(uemail,msg):
    to = uemail
    subject = "Finance company"
    message = msg
    send_mail(subject,message,'gavarthor@gmail.com',[to])

'''def send_mail(uemail,ufname,ulname):
    subject = "Finance company"
    message = f"Hi {ufname} {ulname},You have successfully login with our site.Thanky you"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("gavarthor@gmail.com","8805059015")
    server.sendmail("gavarthor@gmail.com",uemail,message,)'''

def bankdetail(request):
    error_msg = None
    form = bankdetailForm()
    #email=request.session['email']
    #password=request.session['password']
    email = request.session.get('email')
    email = getsessionEmail(email)
    print("seeion are:",email)

    #bankdetaildata = bankdetailModel.objects.all()
    bankdetaildata = bankdetailModel.objects.filter(profileId__email=email)

    searchName = request.GET.get('searchName')
    #print("name is",searchName)
    if searchName:
        bankdetaildata = bankdetailModel.objects.filter(name__icontains=searchName).filter(profileId__email=email)
    else:
        paginator = Paginator(bankdetaildata, 10)  # Show 3 contacts per page.
        page_number = request.GET.get('page')
        try:
            bankdetaildata = paginator.get_page(page_number)
        except PageNotAnInteger:
            bankdetaildata = Paginator.page(1)
        except EmptyPage:
            bankdetaildata = Paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = bankdetailForm(request.POST)
        #getId = signupModel.objects.get(email=email)
        getId = getsessionEmail(email)
        print(getId.id)
        profileId = getId
        name = request.POST.get('name')
        bankName = request.POST.get('bankName')
        ifscCode = request.POST.get('ifscCode')
        accountNumber = request.POST.get('accountNumber')
        branch = request.POST.get('branch')
        form = bankdetailModel(profileId=profileId,name=name,bankName=bankName,ifscCode=ifscCode,accountNumber=accountNumber,branch=branch)
        form.save()
        messages.success(request, "Bank Details added Successfully.")

        """
        if form.is_valid():
            name = form.cleaned_data['name']
            bankName = form.cleaned_data['bankName']
            ifscCode = form.cleaned_data['ifscCode']
            accountNumber = form.cleaned_data['accountNumber']
            branch = form.cleaned_data['branch']
            #print("details:",name,bankName,ifscCode,accountNumber,branch)
            updatedetail = {'name':name,'bankName':bankName,'ifscCode':ifscCode,'accountNumber':accountNumber,'branch':branch}

            f = form.save(commit=False)
            f.profileId = getId.email
            f.save(commit=True)

            messages.success(request,"Bank Details added Successfully.")
            return redirect('/bankdetail')
        print(form.errors)
        """
        return redirect('/bankdetail')
    data = {'form':form,'bankdetaildata':bankdetaildata}
    return render(request,'finance/bankdetail.html',data)

def updatBankDetail(request,id):
    updatedetail = bankdetailModel.objects.get(id=id)
    email = request.session.get('email')
    #email = request.session['email']
    #getId = signupModel.objects.get(email=email)
    getId = getsessionEmail(email)
    print(getId.id)

    bankdetaildata = bankdetailModel.objects.filter(profileId__email=email)
    searchName = request.GET.get('searchName')
    # print("name is",searchName)
    if searchName:
        bankdetaildata = bankdetailModel.objects.filter(name__icontains=searchName).filter(profileId__email=email)
    else:
        paginator = Paginator(bankdetaildata, 10)  # Show 3 contacts per page.
        page_number = request.GET.get('page')
        try:
            bankdetaildata = paginator.get_page(page_number)
        except PageNotAnInteger:
            bankdetaildata = Paginator.page(1)
        except EmptyPage:
            bankdetaildata = Paginator.page(paginator.num_pages)

    if request.method =='POST':
        name = request.POST.get('name')
        bankName = request.POST.get('bankName')
        ifscCode = request.POST.get('ifscCode')
        accountNumber = request.POST.get('accountNumber')
        branch = request.POST.get('branch')

        profileId = getId
        updatedetail.name = name
        updatedetail.bankName = bankName
        updatedetail.ifscCode =ifscCode
        updatedetail.accountNumber = accountNumber
        updatedetail.branch = branch
        updatedetail.save()
        messages.success(request,"Successfully Updated")
        return redirect('/bankdetail')
    """    
        form = bankdetailForm(request.POST,instance=updatedetail)
        if form.is_valid():
            form.save()
            messages.success(request,'Bank Detail Updated successfully.')
        return redirect('/bankdetail')
    """
    return render(request,'finance/bankdetail.html',{'updatedetail':updatedetail,'bankdetaildata':bankdetaildata})


def deleteBankDetail(request,id):
    deletebankdetail = bankdetailModel.objects.get(id=id)
    deletebankdetail.delete()
    messages.success(request,'Bank Detail Deleted Successfully.')
    return redirect('/bankdetail')

#---------------------------------------------------------------------------------------------------------------------
def customer(request):
    form = customerForm()
    #email = request.session['email']
    email = request.session.get('email')
    customerinfo = customerModel.objects.filter(profileId__email=email)
    searchName = request.GET.get('searchName')
    #print("name is",searchName)
    if searchName:
        customerinfo = customerModel.objects.filter(name__icontains=searchName).filter(profileId__email=email)
    else:
        #customerinfo = customerModel.objects.all()
        paginator = Paginator(customerinfo,10)
        page_number = request.GET.get('page')
        try:
            customerinfo = paginator.get_page(page_number)
        except PageNotAnInteger:
            customerinfo = paginator.page(1)
        except EmptyPage:
            customerinfo = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = customerForm(request.POST)
        #getId = signupModel.objects.get(email=email)
        getId = getsessionEmail(email)
        error_msg=None
        nameexist=False

        name = request.POST.get('name')
        aadharNo = request.POST.get('aadharNo')
        address = request.POST.get('address')
        business = request.POST.get('business')
        mobile = request.POST.get('mobile')
        try:
            # dname = customerModel.objects.get(name=name)
            dname = customerModel.objects.filter(profileId__email=email)
            print(dname)

            for val in dname:
                print(val.name,"val.name",val.profileId,":Email")
                print(val.name == name,"val.name=name")
                if name == val.name:
                    error_msg = "Name already exists!!"
                    nameexist = True
                    break
                else:
                    error_msg=None
                    nameexist=False

        except Exception as e:
            print("except block",e)
            nameexist = True

        customerDetails = {'name': name, 'aadharNo': aadharNo, 'address': address, 'business': business,'mobile': mobile}
        if nameexist:
            error_msg = "Name already exists!!"
        if not error_msg:
            form = customerModel(profileId=getId,name=name,aadharNo=aadharNo,address=address,business=business,mobile=mobile)
            form.save()
            messages.success(request, 'Customer added successfully')
            return redirect('/customer')
        else:
            return render(request, 'finance/customer.html',{'customerDetails': customerDetails, 'error_msg': error_msg,'customerinfo':customerinfo  })

    data = {'form':form,'customerinfo':customerinfo}
    return render(request,'finance/customer.html',data)

def customerUpdate(request,id):
    customerDetails = customerModel.objects.get(id=id)
    #email = request.session['email']
    email = request.session.get('email')
    #getId = signupModel.objects.get(email=email)
    getId = getsessionEmail(email)
    customerinfo = customerModel.objects.filter(profileId__email=email)

    searchName = request.GET.get('searchName')
    # print("name is",searchName)
    if searchName:
        customerinfo = customerModel.objects.filter(name__icontains=searchName).filter(profileId__email=email)
    else:
        paginator = Paginator(customerinfo, 10)
        page_number = request.GET.get('page')
        try:
            customerinfo = paginator.get_page(page_number)
        except PageNotAnInteger:
            customerinfo = paginator.page(1)
        except EmptyPage:
            customerinfo = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        """
        form = customerForm(request.POST,instance=customerDetails)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer Updated successfully')
        return redirect('/customer')
        """
        name = request.POST.get('name')
        aadharNo = request.POST.get('aadharNo')
        address = request.POST.get('address')
        business = request.POST.get('business')
        mobile = request.POST.get('mobile')

        customerDetails.profileId = getId
        customerDetails.name =name
        customerDetails.aadharNo = aadharNo
        customerDetails.address = address
        customerDetails.business = business
        customerDetails.mobile = mobile
        customerDetails.save()
        messages.success(request, 'Customer Updated successfully')
        return redirect('/customer')
    data = {'customerDetails':customerDetails,'customerinfo':customerinfo}
    return render(request,'finance/customer.html',data)

def customerDelete(request,id):
    customerDetails = customerModel.objects.get(id=id)
    customerDetails.delete()
    messages.success(request, 'Customer Deleted successfully')
    return redirect('/customer')


#=======================================================================================================================

def partner(request):
    form = partnerForm()
    error_msg = None
    #email = request.session['email']
    email = request.session.get('email')
    partnerinfo = partnerModel.objects.filter(profileId__email=email)
    searchName = request.GET.get('searchName')
    #print("name is",searchName)
    if searchName:
        partnerinfo = partnerModel.objects.filter(name__icontains=searchName).filter(profileId__email=email)
    else:
        paginator = Paginator(partnerinfo,10)
        page_number = request.GET.get('page')
        try:
            partnerinfo = paginator.get_page(page_number)
        except PageNotAnInteger:
            partnerinfo = paginator.page(1)
        except EmptyPage:
            partnerinfo = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        #email = request.session.get('email')
        #getId = signupModel.objects.get(email=email)
        getId = getsessionEmail(email)

        name = request.POST.get('name')
        initialAmount = request.POST.get('initialAmount')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        partner = partnerModel(profileId=getId,name=name,initialAmount=initialAmount,mobile=mobile,address=address)
        partner.save()
        messages.success(request, 'Partner Added successfully')
        return redirect('/partner')

    data = {'form':form,'partnerinfo':partnerinfo}
    return render(request,'finance/partner.html',data)

def partnerUpdate(request,id):
    partnerdetail = partnerModel.objects.get(id=id)
    #email = request.session['email']
    email = request.session.get('email')
    #getId = signupModel.objects.get(email=email)
    getId = getsessionEmail(email)

    partnerinfo = partnerModel.objects.filter(profileId__email=email)

    searchName = request.GET.get('searchName')
    print("name is", searchName)
    if searchName:
        partnerinfo = partnerModel.objects.filter(name__icontains=searchName).filter(profileId__email=email)
        #messages.success(request,"No record found")
    else:
        paginator = Paginator(partnerinfo, 10)
        page_number = request.GET.get('page')
        try:
            partnerinfo = paginator.get_page(page_number)
        except PageNotAnInteger:
            partnerinfo = paginator.page(1)
        except EmptyPage:
            partnerinfo = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = partnerForm(request.POST,instance=partnerdetail)
        #email = request.session['email']

        partnerdetail.profileId = getId
        partnerdetail.name = request.POST.get('name')
        partnerdetail.initialAmount = request.POST.get('initialAmount')
        partnerdetail.mobile = request.POST.get('mobile')
        partnerdetail.address = request.POST.get('address')
        partnerdetail.save()
        messages.success(request, 'Partner Updated successfully')
        return redirect('/partner')
    data = {'partnerdetail':partnerdetail,'partnerinfo':partnerinfo}
    return render(request,'finance/partner.html',data)

def partnerDelete(request,id):
    partnerdetail = partnerModel.objects.get(id=id)
    partnerdetail.delete()
    messages.success(request, 'Partner Deleted successfully')
    return redirect('/partner')

#---------------------------------------------------------------------------------------------------------------------
import random
transicationList=[]

def loan(request):
    home(request)
    totalCapital = sumOfTotalCapital
    #totalCapital = json.dumps(totalCapital)
    #print("totalCapital:",totalCapital)
    form = LoanForm()
    transicationNo = ""
    email = request.session.get('email')
    #getId = signupModel.objects.get(email=email)
    getId = getsessionEmail(email)

    customerList = customerModel.objects.filter(isapprove=False).filter(profileId__email=getId)
    loanData = LoanModel.objects.filter(iscompleted=False,approve=False).filter(customerName__profileId__email=getId)

    #displayData = LoanModel.objects.filter(approve=True,iscompleted=False)

    transicationList.clear()
    not_unique = True
    while not_unique:
        for i in range(11):
            rn = random.randint(0,9)
            transicationList.append(rn)
        for i in transicationList:
            transicationNo += str(i)
        if not LoanModel.objects.filter(transactionNo=transicationNo):
            not_unique = False

    searchName = request.GET.get('searchName')
    if searchName:
        loanData = LoanModel.objects.filter(customerName__name__icontains=searchName).filter(customerName__profileId__email=getId)
    else:
        paginator = Paginator(loanData,10)
        pageNumber = request.GET.get('page')
        try:
            loanData = paginator.get_page(pageNumber)
        except PageNotAnInteger:
            loanData = paginator.page(1)
        except EmptyPage:
            loanData = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        saveData = LoanForm(request.POST)
        error_msg = None
        chequeNum = 0
        customerName = request.POST.get('customerName')
        CN = customerModel.objects.get(id=customerName)

        transactionNo = int(request.POST.get('transactionNo'))
        amount = int(request.POST.get('amount'))
        interest = int(request.POST.get('interest'))
        interestAmount = int(request.POST.get('interestAmount'))
        Amountfinal = int(request.POST.get('Amountfinal'))
        paidAmount = int(request.POST.get('paidAmount'))
        chequeNumber = request.POST.get('chequeNumber')
        if chequeNumber:
            chequeNum = int(chequeNumber)
        #print("type of chequeNumber is", type(chequeNumber),chequeNumber)

        Udays = int(request.POST.get('Udays'))
        todayDate = str(request.POST.get('todayDate'))
        expectedDay =str(request.POST.get('expectedDay'))

        datesToday = datetime.datetime.strptime(todayDate, '%d/%m/%Y').date()
        datesEnd = datetime.datetime.strptime(expectedDay,'%d/%m/%Y').date()

        morgage = request.POST.get('morgage')
        guaranteePerson = request.POST.get('guaranteePerson')

        #if Amountfinal > totalCapital:
        #    error_msg="Loan Amount Cant be greater than Capital Amount"
        saveData = LoanModel(customerName=CN,transactionNo=transactionNo,amount=amount,interest=interest,interestAmount=interestAmount,Amountfinal=Amountfinal,
                             paidAmount=paidAmount,chequeNumber=chequeNum,Udays=Udays,todayDate=datesToday,expectedDay=datesEnd,morgage=morgage,guaranteePerson=guaranteePerson)
        issave = saveData.save()
        print("is save :",issave)
        messages.success(request, 'Loan Submitted successfully')
        return redirect('/loan')

        #if form.is_valid():
        #    form.save()
    data = {'form':form, "customerList":customerList,'tran':transicationNo,'loanData':loanData,'totalCapital':totalCapital}
    return render(request,'finance/loan.html',data)

def updateLoan(request,id):
    home(request)
    totalCapital = sumOfTotalCapital
    email = request.session.get('email')
    #getId = signupModel.objects.get(email=email)
    getId = getsessionEmail(email)

    customerList = customerModel.objects.filter(isapprove=False).filter(profileId__email=getId)
    loandetail = LoanModel.objects.get(id=id)#.filter(profileId__email=getId)

    #-------------------------------------------------Paginator--------
    loanData = LoanModel.objects.filter(iscompleted=False, approve=False).filter(customerName__profileId__email=getId)
    searchName = request.GET.get('searchName')
    if searchName:
        loanData = LoanModel.objects.filter(customerName__name__icontains=searchName).filter(customerName__profileId__email=getId)
    else:
        paginator = Paginator(loanData, 10)
        pageNumber = request.GET.get('page')
        try:
            loanData = paginator.get_page(pageNumber)
        except PageNotAnInteger:
            loanData = paginator.page(1)
        except EmptyPage:
            loanData = paginator.page(paginator.num_pages)
    #-------------------------------------------------------------------
    expDate = loandetail.expectedDay
    if request.method == 'POST':
        chequeNum = 0
        customerName = request.POST.get('customerName')
        print("cus id:",customerName)#3
        CL = LoanModel.objects.get(id=customerName)

        transactionNo = int(request.POST.get('transactionNo'))
        amount = int(request.POST.get('amount'))
        interest = int(request.POST.get('interest'))
        interestAmount = int(request.POST.get('interestAmount'))
        Amountfinal = int(request.POST.get('Amountfinal'))
        paidAmount = int(request.POST.get('paidAmount'))
        chequeNumber = request.POST.get('chequeNumber')
        if chequeNumber:
            chequeNum = int(chequeNumber)
        Udays = int(request.POST.get('Udays'))
        todayDate = str(request.POST.get('todayDate'))
        expectedDay = str(request.POST.get('expectedDay'))

        datesToday = datetime.datetime.strptime(todayDate, '%d/%m/%Y').date()
        datesEnd = datetime.datetime.strptime(expectedDay, '%d/%m/%Y').date()

        morgage = request.POST.get('morgage')
        guaranteePerson = request.POST.get('guaranteePerson')
#------save updated value-----------------------------------
        loandetail.customerName = CL.customerName
        loandetail.transactionNo= transactionNo
        loandetail.amount = amount
        loandetail.interest = interest
        loandetail.interestAmount = interestAmount
        loandetail.Amountfinal = Amountfinal
        loandetail.paidAmount = paidAmount
        loandetail.chequeNumber = chequeNum
        loandetail.Udays = Udays
        loandetail.todayDate = datesToday
        loandetail.expectedDay = datesEnd
        loandetail.morgage = morgage
        loandetail.guaranteePerson = guaranteePerson
        loandetail.save()
        messages.success(request, 'Loan Updated successfully')
        return redirect('/loan')

    data = {'loandetail':loandetail,'customerList':customerList,'loanData':loanData,'totalCapital':totalCapital}
    return render(request,'finance/loan.html',data)

def loanDelete(request,id):
    loandetail = LoanModel.objects.get(id=id)
    isdelete = loandetail.delete()
    print(isdelete)
    messages.success(request, 'Loan customer Deleted successfully')
    return redirect('/loan')

def loanApprove(request,id):
    loandetail = LoanModel.objects.get(id=id)
    #print("loan model id is:",loandetail.id)
    #print(loandetail.customerName.name)
    customerList = customerModel.objects.get(name=loandetail.customerName.name)
    print("customer list is:",customerList)

    # For customerList
    customerList.isapprove = True
    customerList.save()
    #For Loan
    loandetail.approve = True
    loandetail.iscompleted = False
    loandetail.save()
    messages.success(request, 'Loan Approved successfully')
    return redirect('/loan')

#-----------------------------------Transication -----------------------
def transication(request):

    email = request.session.get('email')
    #getId = signupModel.objects.get(email=email)
    getId = getsessionEmail(email)
    loanDetails = LoanModel.objects.filter(approve=True,iscompleted=False).filter(customerName__profileId__email=getId)
    getTransicationData = transactionModel.objects.all()

    data = {'loanDetails': loanDetails}#'getTransicationData':getTransicationData
    return render(request,'finance/transaction.html',data)

def transicationName(request,id):
    print("the id is:",id)
    #email = request.session['email']
    email = request.session.get('email')
    getId = getsessionEmail(email)
    sumOfpaidAmount =0

    #print("cust is:",id,"type is:",type(id))
    TransicationData = transactionModel.objects.filter(customerId=id).order_by('-paidDate')

    #-----Paginator--------
    paginator = Paginator(TransicationData,10)
    pageNumber = request.GET.get('page')
    try:
        TransicationData = paginator.get_page(pageNumber)
    except PageNotAnInteger:
        TransicationData = paginator.page(1)
    except EmptyPage:
        TransicationData = paginator.page(paginator.num_pages)
    #-----End paginator------

    loanDetails = LoanModel.objects.filter(approve=True,iscompleted=False).filter(customerName__profileId__email=getId)
    getCustId = LoanModel.objects.get(id=id)
    getPaidAmount = getCustId.paidAmount
    getDays = getCustId.Udays
    dailyAmount = getPaidAmount//getDays

    paidAmountFromTrancastion_tbl = transactionModel.objects.filter(customerId=id)
    for value in paidAmountFromTrancastion_tbl:
        sumOfpaidAmount = sumOfpaidAmount + value.paidAmount
        #print(value.paidAmount,type(value.paidAmount))
    #print("sum Of paidAmount",sumOfpaidAmount)

    remainingAmount = getPaidAmount-sumOfpaidAmount
    #print("remainingAmount:",remainingAmount)

    list=[]
    not_unique = True
    while not_unique:
        list.clear()
        for i in range(10):
            num = random.randint(0,9)
            list.append(str(num))
        transicationId = ''.join(list)
        if not transactionModel.objects.filter(transactionNo=transicationId):
            not_unique = False
    #----------------------------------------Get Transaction data------------------------
    #transactionData = transactionModel.objects.get(id=id)

    if request.method == 'POST':
        #custId = int(request.POST.get('customerName'))
        custTransactionNo = int(request.POST.get('transactionNo'))
        custDailyAmount = int(request.POST.get('dailyAmount'))
        custPaidAmount = int(request.POST.get('paidAmount'))
        datePaid = request.POST.get('dateValue')

        custdatePaid =None
        if datePaid:
            custdatePaid  = datetime.datetime.strptime(datePaid, '%Y-%m-%d').date()
            print("converto to date:",custdatePaid)
        else:
            custdatePaid = datetime.datetime.today()
        getId = int(id)
        print(id)
        getMyId = LoanModel.objects.get(id=id)

        saveData = transactionModel(customerId=getMyId,transactionNo=custTransactionNo,dailyAmount=custDailyAmount,paidAmount=custPaidAmount,paidDate=custdatePaid)
        saveData.save()
        messages.success(request,"Successfully Submited Amount!!!")
#------------------------------------------------------------------------------------------------------------------------------------
        getCustId = LoanModel.objects.get(id=id)
        getPaidAmount = getCustId.paidAmount

        sumOfpaidAmount = 0
        paidAmountFromTrancastion_tbl = transactionModel.objects.filter(customerId=id)
        for value in paidAmountFromTrancastion_tbl:
            sumOfpaidAmount = sumOfpaidAmount + value.paidAmount

        if getPaidAmount <= sumOfpaidAmount:
            getCustData = LoanModel.objects.get(id=id)
            getCustData.iscompleted = True
            getCustData.save()

            print("name is:",getCustId.customerName.name)
            replaceCust = customerModel.objects.get(name=getCustId.customerName.name)
            replaceCust.isapprove = False
            replaceCust.save()
            redirect('/transication')
        return redirect('/transication')

    data = {'loanDetails': loanDetails,'transicationId':transicationId,'dailyAmount':dailyAmount,'getCustId':getCustId,"remainingAmount":remainingAmount,
            'TransicationData':TransicationData}
    return render(request,'finance/transaction.html',data)



def approveLoan(request):
    email = request.session.get('email')
    approvedLoanData = LoanModel.objects.filter(iscompleted=False, approve=True).filter(customerName__profileId__email=email)
    print(approvedLoanData)
    searchName = request.GET.get('searchName')
    if searchName:
        approvedLoanData = LoanModel.objects.filter(customerName__name__icontains=searchName).filter(customerName__profileId__email=email)
    else:
        paginator = Paginator(approvedLoanData, 10)
        pageNumber = request.GET.get('page')
        try:
            approvedLoanData = paginator.get_page(pageNumber)
        except PageNotAnInteger:
            approvedLoanData = paginator.page(1)
        except EmptyPage:
            approvedLoanData = paginator.page(paginator.num_pages)

    data = {'approvedLoanData':approvedLoanData}
    return render(request,'finance/approvedloan.html',data)

def completedLoan(request):
    email = request.session.get('email')
    completedLoanData = LoanModel.objects.filter(iscompleted=True, approve=True).filter(customerName__profileId__email=email)
    print(completedLoanData)
    searchName = request.GET.get('searchName')
    if searchName:
        completedLoanData = LoanModel.objects.filter(customerName__name__icontains=searchName).filter(customerName__profileId__email=email)
    else:
        paginator = Paginator(completedLoanData, 10)
        pageNumber = request.GET.get('page')
        try:
            completedLoanData = paginator.get_page(pageNumber)
        except PageNotAnInteger:
            completedLoanData = paginator.page(1)
        except EmptyPage:
            completedLoanData = paginator.page(paginator.num_pages)

    data = {'completedLoanData':completedLoanData}
    return render(request,'finance/completedloan.html',data)

#*************************************************Char validation**********************************************
def charvalid(name):
    error_msg=None
    if len(name) >= 2:
        list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$', '?')
        if name.startswith(list):
            error_msg = "Name Cant start with number"
        elif name:
            for i in name:
                if i in list:
                    error_msg = "name cant contain number"
    elif len(name) < 1:
        error_msg = "Name length greater than 2"
    return error_msg

