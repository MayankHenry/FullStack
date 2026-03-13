function validation(){
    var name = document.getElementById("name").value;
    var password = document.getElementById("password").value;
    var mobile = document.getElementById("mobile").value;
    var mobilePattern = /^[0-9]{10}$/;
    if(name === ""){
        alert("Name cannot be empty");
        return false;
    }
    if(password.length < 6){
        alert("Password must be at least 6 characters long");
        return false;
    }   
    if(!mobilePattern.test(mobile)){
        alert("Mobile number must be 10 digits");
        return false;
    }
    alert("Validation Successful");
    return true;
}