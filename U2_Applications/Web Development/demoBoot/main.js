var currActive = document.getElementsByClassName("active");

var navLinks = document.getElementById("navBar").getElementsByTagName("li");

for (var i = 0; i < navLinks.length; i++){
    navLinks[i].addEventListener('click', changeActive);
}

function changeActive(){
    currActive[0].classList.remove("active");
    this.classList.add("active");
}
//console.log("success")
