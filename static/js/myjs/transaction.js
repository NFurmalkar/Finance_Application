

function holdSubmit(e)
{
    e.preventDefault();
    Validition();
}
const form = document.getElementById("form");
form.addEventListener('submit',holdSubmit);

function Validition()
{
    isMsg = "";
    inputCustomerName = document.getElementById("inputCustomerName").value;
    inputTransactionId = document.getElementById("inputTransactionId").value;
    inputDailyAmount = document.getElementById("inputDailyAmount").value;
    inputPaidAmount = document.getElementById("inputPaidAmount").value;
    //console.log(inputCustomerName);

    errorName = document.getElementById("errorSelectName");
    getId = errorName.getAttribute('id');
    if("selectName" == inputCustomerName)
    {
        setErrorMsg("inputCustomerName",getId,"select Name");
        return false;
    }
    else
    {
        setSuccessMsg("inputCustomerName",getId);
    }

    errorName = document.getElementById("errorPaidAmount");
    getId = errorName.getAttribute('id');
    if(inputPaidAmount.length <=1)
    {
        setErrorMsg("inputPaidAmount",getId,"Must be 2 digit");
        return false;
    }
    else
    {
        isMsg = "successMsg";
        setSuccessMsg("inputPaidAmount",getId,)
    }

    console.log(isMsg);
    if(isMsg)
    {
        form.submit();
    }
}

function setErrorMsg(input,getId,errorMsg)
{
    var addclass = document.getElementById(input);
    addclass.className = "form-control errors";
    document.getElementById(getId).innerText=errorMsg;
}
function setSuccessMsg(input,getId)
{
    var addclass = document.getElementById(input);
    addclass.className = "form-control success"
    document.getElementById(getId).innerText='';
}
