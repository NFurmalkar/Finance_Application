console.log("partner working..");

form = document.getElementById("form");
function holdSubmit(e)
{
    e.preventDefault();
    validation();
}
form.addEventListener('submit',holdSubmit);

function validation()
{
    var isMsg="";
    nameVal = document.getElementById("idName").value;
    initialAmountVal = document.getElementById("idInitialAmount").value;
    mobileVal = document.getElementById("idMobile").value;
    addressVal = document.getElementById("idAddress").value;
//Name Validation
    errorName = document.getElementById("errorName")
    getId = errorName.getAttribute('id');
    if(nameVal.length <=3)
    {
        setErrorMsg("idName",getId,"Name must be 4 char");
        return false;
    }
    else
    {
        setSuccessMsg("idName",getId);
    }
// Initial Amount
    errorName = document.getElementById("errorInitialAmount");
    getId = errorName.getAttribute('id');
    if(initialAmountVal.length <=3)
    {
        setErrorMsg("idInitialAmount",getId,"InitialAmount must be 4 digit");
        return false;
    }
    else
    {
        setSuccessMsg("idInitialAmount",getId);
    }
// mobile validation
    var val = ['0','1','2','3','4','5','6'];
    fv = mobileVal[0];
    fyTrue = val.includes(fv);
    console.log(fyTrue);

    errorName = document.getElementById("errorMobile");
    getId = errorName.getAttribute('id');
    if(mobileVal.length <=9 || mobileVal.length >10 || fyTrue)
    {
        setErrorMsg("idMobile",getId,"Invalid mobile");
        return false;
    }
    else
    {
        setSuccessMsg("idMobile",getId);
    }
//Address validation
    errorName = document.getElementById("errorAddress");
    getId = errorName.getAttribute('id');
    if(addressVal.length <=3)
    {
        setErrorMsg("idAddress",getId,"InitialAmount must be 4 char");
        return false;
    }
    else
    {
        isMsg = "successMsg";
        setSuccessMsg("idAddress",getId);
    }


    function setErrorMsg(input,getId,errorMsg)
    {
        var addClass = document.getElementById(input);
        addClass.className = "form-control errors";
        document.getElementById(getId).innerText = errorMsg;
    }
    function setSuccessMsg(input,getId)
    {
        addClass = document.getElementById(input);
        addClass.className = "form-control success";
        document.getElementById(getId).innerText = '';
    }

    if(isMsg)
    {
        form.submit();
    }
}