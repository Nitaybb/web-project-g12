function hideOrShow(productInfo, Products) {

 var p = document.getElementById(productInfo);
 var p1 = document.getElementById(Products);

  if (p.style.display === "none") {

    p.style.display = "block";

  }
   else {

    p.style.display = "none";
  }
  if (p1.style.display === "block") {

    p1.style.display = "none";

  } else{
    p1.style.display = "block";
  }

}
