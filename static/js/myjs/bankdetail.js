
const form = document.getElementById('idform'); //
function stopSubmit(e)
{
    e.preventDefault();
    validate();
}
form.addEventListener('submit',stopSubmit);
// if(isvalidate)
// {
//     form.submit();
// }



//console.log(isvalidate, typeof(isvalidate),"showvalid");


//var isvalidate = "error"; 
// console.log(isvalidate);
//     form.addEventListener("submit", (Event)=> {
//         Event.preventDefault();
//         validate();
//     })

// if(isvalidate =="success")
// {

// }
// else("success" == isvalidate)
// {
//     form.addEventListener("submit", (Event)=> {
//         Event.preventDefault();
//         validate();
//     })
// }

//const validate=() =>  OR
function validate()
{  
     var isMsg = "";
    console.log("in validation:",typeof(isMsg),isMsg);
    const formval = document.getElementById('idform').value;
    const nameval = document.getElementById('idName').value;
    const BankNameval = document.getElementById('idBankName').value;
    const ifscCodeval = document.getElementById('idifscCode').value;
    const accountNumberval = document.getElementById('idaccountNumber').value;
    const Branchval = document.getElementById('idBranch').value;
//Name validation
    errorName = document.getElementById('errorName');
    getid = errorName.getAttribute('id');
    if(nameval =='')
    {
        setErrorMsg('idName',getid,'Name cant be blank');
        return false;
    }
    else if(nameval.length <=3)
    {
        setErrorMsg('idName',getid,'Name must be 4 char');
        return false;
    }
    else
    {
        setSuccesMsg('idName',getid);
    }
// Bank name    
    errorName = document.getElementById('errorBankName');
    getid = errorName.getAttribute('id');
    if(BankNameval =='')
    {
        setErrorMsg('idBankName',getid,'Bank Name cant be blank');
        return false;
    }
    else if(BankNameval.length <=3)
    {
        setErrorMsg('idBankName',getid,'Bank Name must be 4 char');
        return false;
    }
    else
    {
        setSuccesMsg('idBankName',getid);
    }
//ifscCode  idifscCode
    errorName = document.getElementById('errorifscCode');
    getid = errorName.getAttribute('id');
    if(ifscCodeval =='')
    {
        setErrorMsg('idifscCode',getid,'ifscCode cant be blank');
        return false;
    }
    else if(ifscCodeval.length <=3)
    {
        setErrorMsg('idifscCode',getid,'ifscCode must be 4 char');
        return false;
    }
    else
    {
        setSuccesMsg('idifscCode',getid);
    }
// account Number
    errorName = document.getElementById('erroraccountNumber');
    getid = errorName.getAttribute('id');
    if(accountNumberval =='')
    {
        setErrorMsg('idaccountNumber',getid,'account Number cant be blank');
        return false;
    }
    else if(accountNumberval.length <=11 || accountNumberval.length >=13)
    {
        setErrorMsg('idaccountNumber',getid,'account Number must be 12 char');
        return false;
    }
    else
    {
        setSuccesMsg('idaccountNumber',getid);
    }
// Branch Number
    errorName = document.getElementById('errorbranch');
    getid = errorName.getAttribute('id');
    if(Branchval =='')
    {
        setErrorMsg('idBranch',getid,'Branch Number Name cant be blank');
        return false;
    }
    else if(Branchval.length <=3)
    {
        setErrorMsg('idBranch',getid,'Branch Number must be 4 char');
        return false;
    }
    else
    {
        isMsg = "successMsg";
        setSuccesMsg('idBranch',getid);
    }

    function setErrorMsg(input,getId,errorMsgs)
    {
    //console.log(input,getId,errorMsgs);
      var addClass = document.getElementById(input);
      addClass.className = "form-control errors";

      document.getElementById(getId).innerText = errorMsgs;
      //console.log(addClass);
    }
    function setSuccesMsg(input,getid)
    {
        var remClass = document.getElementById(input)
        remClass.className = "form-control success";
        document.getElementById(getid).innerText ='';
    }

    console.log(isMsg);
    if(isMsg)
    {
        form.submit();
    }

}