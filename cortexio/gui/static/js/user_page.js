var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("myColorImageSlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";

  var j;
  var z = document.getElementsByClassName("myDepthImageSlides");
  if (n > z.length) {slideIndex = 1}
  if (n < 1) {slideIndex = z.length}
  for (i = 0; i < z.length; i++) {
     z[i].style.display = "none";
  }
  z[slideIndex-1].style.display = "block";
}