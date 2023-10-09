
 if (data === 'User already registered.'){
    alert("User exists!");
}

function validate(){
     var username=document.getElementById("name").value;
     var phone=document.getElementById("phonenumber").value;
     var email=document.getElementById("email").value;
     var password=document.getElementById("password").value;
     var repassword=document.getElementById("repassword").value;

     if(username==""){
        alert("please enter name");
        return false;
     }

     if(phone==""){
         alert("please enter phone number");
         return false;
     }
     if(phone.length<10){
         alert("please enter 10 digit phone number");
         return false;
     }

     var validRegex = /^[a-z0-9]+@+[a-z]+\.[a-z]{2,3}$/;
     var result = validRegex.test(email);
     if(email==""){
         alert("please enter your email");
         return false;
     }
     if (!result) {
         alert("Invalid email address!");
         return false;
     }


     if(password==""){
         alert("please enter password");
         return false;
     }
     if(password.length<8){
         alert("please enter 8 character for password");
         return false;
     }
     if(password==""){
         alert("please re-enter password");
         return false;
     }
     if(repassword!=password){
         alert("Password does not match");
         return false;
     }

}
