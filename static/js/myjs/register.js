
function holdSubmit(e)
{
    e.preventDefault();
    validation();
}
var form = document.getElementById("myForm");
form.addEventListener('submit',holdSubmit);

function validation()
{
    var isMsg="";
    firstName = document.getElementById("InputfirstName").value;
    lastName = document.getElementById("InputlastName").value;
    email = document.getElementById("Inputemail").value;
    gender = document.getElementById("Inputgender").value;
    password = document.getElementById("Inputpassword").value;
    initialcapital = document.getElementById("InputInitialCapital").value;
    console.log(firstName,lastName,email,gender,password,initialcapital);

    var ErrorValue = document.getElementById("errorfirstName");
    var getId = ErrorValue.getAttribute('id');
    console.log(getId);
    if (firstName.length <=1 )
    {
        setErrorMsg("InputfirstName",getId,"Must be 2 Character");
        return false;
    }
    else
    {
        setSuccessMsg("InputfirstName",getId)
    }

    var ErrorValue = document.getElementById("errorlastName");
    var getId = ErrorValue.getAttribute('id');
    console.log(getId);
    if (lastName.length <=1 )
    {
        setErrorMsg("InputlastName",getId,"Must be 2 Character");
        return false;
    }
    else
    {
        setSuccessMsg("InputlastName",getId)
    }

    var ErrorValue = document.getElementById("erroremail");
    var getId = ErrorValue.getAttribute('id');
    console.log(getId);
    if (email.length <=1 )
    {
        setErrorMsg("Inputemail",getId,"Invalid Email");
        return false;
    }
    else
    {
        setSuccessMsg("Inputemail",getId)
    }

    var ErrorValue = document.getElementById("errorinitialCapital");
    var getId = ErrorValue.getAttribute('id')
    if(initialcapital.length == 0)
    {
        setErrorMsg("InputInitialCapital",getId,"Cant be empty")
        return false;
    }
    else
    {
        setSuccessMsg("InputInitialCapital",getId)
    }




    var ErrorValue = document.getElementById("errorpassword");
    var getId = ErrorValue.getAttribute('id');
    console.log(getId);
    if (password.length <=5)
    {
        setErrorMsg("Inputpassword",getId,"password too short");
        return false;
    }
    else
    {
        isMsg = "successMsg";
        setSuccessMsg("Inputpassword",getId)
    }


    function setErrorMsg(input,getId,msg)
    {
        var addClass = document.getElementById(input);
        addClass.className += " " + 'errors';
        document.getElementById(getId).innerText=msg;
    }
    function setSuccessMsg(input,getId)
    {
        var addClass = document.getElementById(input);
        addClass.classList.remove('errors'); 
        document.getElementById(getId).innerText='';
    }

    if(isMsg)
    {
        form.submit()
    }
}