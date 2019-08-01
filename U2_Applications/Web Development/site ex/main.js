window.addEventListener('load', function() {
  load();
})

var button = document.getElementById('butt')

button.addEventListener("click", click);

var load =  function (){
  var pic = document.getElementById('oop');
      pic.style.visibility = 'visible';
      pic.classList.add('fade');
}

// function that changes button when clicked
function click (){
    var roll = document.getElementById('rolled');
    if (this.innerHTML == "click me"){
        this.innerHTML = "hide me";
        roll.style.display = 'block';

    }
    else if (this.innerHTML == "hide me"){
        this.innerHTML = "click me";
        roll.style.display = 'none';
    }
}


//SLIDESHOW
var pic = document.getElementById("myPic"); // get the image element
var imageList = ["images/ny1.jpg","images/ny2.jpg","images/ny3.jpeg"]; //make a list of picture that are going to be in the slideshow

var imageIndex = 0; // start off at the first picture in the list

function changePic(){ //function that changes the picture

   pic.setAttribute("src",imageList[imageIndex]); //attribute being the image src
   //Sets the value of an attribute on the specified element. If the attribute already exists, the value is updated; otherwise a new attribute is added with the specified name and value.

   if (imageIndex == imageList.length-1){
       imageIndex = 0;
   }
   else {
       imageIndex++; // change the index if it's less than the length-1
   }
}

// sets the interval time it changes pics
var intervalHandle = setInterval(changePic,3000);
