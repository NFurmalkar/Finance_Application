console.log("customer");

const formVal = document.getElementById("idForm");
function holdSubmit(e)
{
    e.preventDefault();
    validate();
}
formVal.addEventListener('submit',holdSubmit);
    
function validate()
{
    var isMsg = ""
    nameVal = document.getElementById("idName").value;
    aadharNoVal = document.getElementById("idAadharNo").value;
    addressVal = document.getElementById("idAddress").value;
    businessVal = document.getElementById("idBusiness").value;
    mobileVal = document.getElementById("idMobile").value;
    console.log(nameVal,aadharNoVal,addressVal,businessVal,mobileVal);
//Name validation
    errorName = document.getElementById("errorName");
    getId = errorName.getAttribute('id');
    if(nameVal.length <=3 || nameVal == " "||nameVal == null)
    {
        setErrorMsg("idName",getId,"Name must be 4 char.");
        return false;        
    }
    else
    {
        setSuccessMsg("idName",getId);
    } 
//idAadharNo validation
    errorName = document.getElementById("erroraadharNo");
    getId = errorName.getAttribute('id');

    if(aadharNoVal.length == 0 || aadharNoVal.length <11 || aadharNoVal.length >12)
    {
        setErrorMsg("idAadharNo",getId,"AadharNo must be 12 digit.");
        return false;
    }
    else
    {
        setSuccessMsg("idAadharNo",getId);
    }
//Address validation    
    errorName = document.getElementById("errorAddress");
    getId = errorName.getAttribute('id');
    if(addressVal.length <=3)
    {
        setErrorMsg("idAddress",getId,"Aaddress must be 4 char.");
        return false;
    }
    else
    {
        setSuccessMsg("idAddress",getId);
    }
//businessVal validation
    errorName = document.getElementById("errorBusiness")
    getId = errorName.getAttribute('id');
    if(businessVal.length <=3 )
    {
        setErrorMsg("idBusiness",getId,"Must be 4 char.");
        return false;
    }
    else
    {
        setSuccessMsg("idBusiness",getId);
    }
//idMobile validation
    var val = ['0','1','2','3','4','5','6']
    fv = mobileVal[0];
    isTrue = val.includes(fv);

    errorName = document.getElementById("errorMobile");
    getId = errorName.getAttribute('id');
    if(mobileVal.length <=9 || mobileVal.length>10 || isTrue)
    {
        setErrorMsg("idMobile",getId,"Enter valid Number.");
        return false;
    }
    else
    {
        isMsg ="successMsg";
        setSuccessMsg("idMobile",getId);
    }

    function setErrorMsg(input,getId,errorMsg)
    {
        var addClass = document.getElementById(input);
        addClass.className = "form-control errors";
        document.getElementById(getId).innerText = errorMsg;
    }
    function setSuccessMsg(input,getId)
    {
        var addClass = document.getElementById(input);
        addClass.className = "form-control success";
        document.getElementById(getId).innerText = '';

    }
    if(isMsg)
    {
        formVal.submit();  
    }
}