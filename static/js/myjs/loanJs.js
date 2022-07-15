var myform = document.getElementById('form')
function holdsubmit(e)
{
    e.preventDefault();
}
myform.addEventListener('submit',holdsubmit);

function calculatecheque()
{    
    inputchequeNo = document.getElementById('inputchequeNo').value;
    strchequeNo = toString(inputchequeNo);
    len = inputchequeNo.length;
    //console.log("length is : "+inputchequeNo + typeof(inputchequeNo)+ "Length is:"+inputchequeNo.length );
    if (len >17)
    {
        //document.getElementById('reqChequeNo').innerText = "must be 12 digit"
        document.getElementById('inputchequeNo').value = '';
        setErrorMsg("inputchequeNo","Too long number","reqChequeNo");
    }
    else
    {
        setSuccessMsg("inputchequeNo","reqChequeNo");
    }

    //console.log("length of cheque",inputchequeNo.length);
}


var dbCapital = 0;
function calculateAmount(totalCapital)
{
    dbCapital = totalCapital
    // console.log("interest length is",interest.toString().length);
    inputCustomerName = document.getElementById("inputCustomerName").value;
    console.log(inputCustomerName);
    amount =   document.getElementById("inputAmount").value; 
    isvalids = true;

    if(inputCustomerName == "selectCustomer")
    {
        //document.getElementById("reqName").innerText='select customer name';
        errorName = document.getElementById("reqName");
        getId = errorName.getAttribute('id');
        document.getElementById("inputAmount").value = "";
        setErrorMsg("inputCustomerName","Select Customer Field","reqName");
        return false;
    }
    else
    {
        setSuccessMsg("inputCustomerName","reqName");
        //document.getElementById("reqName").innerText='';
    }

    
    if(amount==null || amount =="")
    {
        //document.getElementById("reqAmount").innerText='Enter amount';
        isvalids = false;
        document.getElementById("inputInterestAmount").value = 00;
        document.getElementById("inputFinalAmount").value = 00;
        document.getElementById("inputPaidAmount").value = 00;
        setErrorMsg("inputAmount","Enter Amount","reqAmount");
        return false;
    }
    else if(isNaN(amount))
    {
        //document.getElementById("reqAmount").innerText='Allow only Number';
        document.getElementById("inputAmount").value = "";
        isvalids = false;
        document.getElementById("inputInterestAmount").value = 00;
        document.getElementById("inputFinalAmount").value = 00;
        document.getElementById("inputPaidAmount").value = 00;
        setErrorMsg("inputAmount","Allow only Number","reqAmount")
        return false;
    }
    else
    {
        setSuccessMsg("inputAmount","reqAmount");
        //document.getElementById("reqAmount").innerText='';
    }
    
    if(isvalids)
    {
        void calculateLoan();
    }
}

function calculateInterest()
{
    interest = document.getElementById("inputInterest").value;
    inputState = document.getElementById("inputCustomerName").value;
    //console.log(typeof(interest),interest);
    isvalids = true;
    if(interest == null || interest =="")
    {
       // document.getElementById("reqInterest").innerText='interest cant be blank';
        isvalids = false;
        document.getElementById("inputInterestAmount").value = 00;
        document.getElementById("inputFinalAmount").value = "";
        document.getElementById("inputPaidAmount").value = "";
        setErrorMsg("inputInterest","interest cant be blank","reqInterest");
        return false;
    }
    else if(isNaN(interest))
    {
       // document.getElementById("reqInterest").innerText='Enter only Number';
        document.getElementById("inputInterest").value = "";
        isvalids = false;
        document.getElementById("inputInterestAmount").value = 00;
        document.getElementById("inputFinalAmount").value = "";
        document.getElementById("inputPaidAmount").value = "";
        setErrorMsg("inputInterest","only Number allow","reqInterest");
        return false;        
    }
    else
    {
        //document.getElementById("reqInterest").innerText='';
        setSuccessMsg("inputInterest","reqInterest");
    }
    
    if(isvalids)
    {
        void calculateLoan();
    }
}

isvalid = false
function calculateLoan()
{
    amount = parseInt(document.getElementById("inputAmount").value); 
    interest =parseFloat( document.getElementById("inputInterest").value);
    
    amountStr = document.getElementById("inputAmount").value;

    interestAmount = Math.floor(amount*interest/100);
    finalAmount = amount - interestAmount;
    paidAmount = finalAmount + interestAmount;

    console.log("amount:",amount + "interest",interest, "interestAmount",interestAmount,"finalAmount",finalAmount,"paidAmount:",paidAmount,"dbData:",dbCapital);
    errorName = document.getElementById('reqFinalAmount');
    var getId = errorName.getAttribute('id');
    if (finalAmount > dbCapital)
    {
        isvalid = false;
        setErrorMsg('inputFinalAmount','Loan Amount Cant be greater than Capital Amount',getId);
        console.log(isvalid,"if condition");
    }
    else
    {
        setSuccessMsg('inputFinalAmount',getId);
        isvalid = true;
        console.log(isvalid,"else condition");
    }
    

    if(amount && interest)
    {
        if(interestAmount)
        {
            document.getElementById("inputInterestAmount").value = interestAmount;
            //console.log("final and paid amount is:",finalAmount,paidAmount);
            document.getElementById("inputFinalAmount").value = finalAmount;
            document.getElementById("inputPaidAmount").value = paidAmount;
        }
        if (interest)
        {
            finalAmount = amount - interestAmount;
            paidAmount = finalAmount + interestAmount;
            document.getElementById("inputFinalAmount").value = finalAmount;
            document.getElementById("inputPaidAmount").value = paidAmount;
        }
    }

    
}

function validatestring()
{
    morgage = document.getElementById("inputmorgage").value;
    GuaranteePerson = document.getElementById("inputGuaranteePerson").value;
    //console.log(typeof(result),'...'+morgage);
    for(var i=0;i<=morgage.length;i++)
    {
        if(!isNaN(morgage[i]))
        {
            //document.getElementById("reqMortgage").innerText='allow only character';
            document.getElementById("inputmorgage").value ='';
            setErrorMsg("inputmorgage","Invalid input","reqMortgage");
            return false;
        }
        else
        {
            //document.getElementById("reqMortgage").innerText='';
            setSuccessMsg("inputmorgage","reqMortgage")
        }
    }

    if(GuaranteePerson)
    {
        for(var i=0;i<=GuaranteePerson.length;i++)
        {
            if(!isNaN(GuaranteePerson[i]))
            {
                //document.getElementById("reqGuaranteeperson").innerText='allow only character';
                document.getElementById("inputGuaranteePerson").value ='';
                setErrorMsg("inputGuaranteePerson","Invalid input","reqGuaranteeperson");
                return false;
            }
            else
            {
                //document.getElementById("reqGuaranteeperson").innerText='';
                setSuccessMsg("inputGuaranteePerson","reqGuaranteeperson")
            }
        }
            
    }
}


todayDate = new Date();
todayDate = todayDate.getDate()+ "/" + (todayDate.getMonth()+1) + "/" + todayDate.getFullYear();
document.getElementById("inputTodayDate").value = todayDate;
//document.getElementById("inputExpectedDay").value = "";
//console.log(typeof(todayDate),todayDate);
var isDataValue = false;
function calculateDays()
{
    //days = parseInt(document.getElementById("inputDays").value);
    days = document.getElementById("inputDays").value;
    //console.log(typeof(days));
    if(days == null || days == 0)
    {
        //document.getElementById('reqDays').innerText ="days can't be empty or zero"; 
        document.getElementById("inputExpectedDay").value ="";
        document.getElementById("inputDays").value="";
        setErrorMsg("inputDays","days can't be empty or zero","reqDays");
        isDataValue = false;
        return false;
    }
    else
    {
        days = parseInt(document.getElementById("inputDays").value);
        //console.log(days);
        endDate = new Date();
        endDate.setDate(endDate.getDate() + days);
        endDate = endDate.getDate()+ "/" + (endDate.getMonth()+1) + "/" + endDate.getFullYear();
        document.getElementById("inputExpectedDay").value = endDate;
        isDataValue = true;
       // console.log("end date is:",typeof(endDate),endDate);
        //document.getElementById('reqDays').innerText ="";
        setSuccessMsg("inputDays","reqDays");

    }
    
    
}

function saveform()
{
    console.log("isDateValue is:",isDataValue)
    if(isDataValue)
    {
        console.log(isvalid,"onsave function called");
        myform.submit();
    }
}


function setErrorMsg(input,errorMsg,errorId)
{
    var addClass = document.getElementById(input);
    addClass.className = "form-control errors";
    document.getElementById(errorId).innerText = errorMsg;
}

function setSuccessMsg(input,errorId)
{
    var addClass = document.getElementById(input);
    addClass.className = "form-control success";
    document.getElementById(errorId).innerText = '';
}

