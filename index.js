function myFunction() {
  var x = document.getElementById("p11");
  if (x.style.display === "none") {
    x.style.display = "block";
    document.getElementById('a1').innerHTML = `<img id="img1" src='assets/images/icon-minus.svg'>`
  } else {
    x.style.display = "none";
    document.getElementById('a1').innerHTML = `<img id="img2" src='assets/images/icon-plus.svg'>`
  }
}
function myFunction2() {
    var x = document.getElementById("p22");
    if (x.style.display === "none") {
      x.style.display = "block";
      document.getElementById('a2').innerHTML = `<img id="img11" src='assets/images/icon-minus.svg'>`
    } else {
      x.style.display = "none";
      document.getElementById('a2').innerHTML = `<img id="img22" src='assets/images/icon-plus.svg'>`
    }
  }
  function myFunction3() {
    var x = document.getElementById("p33");
    if (x.style.display === "none") {
      x.style.display = "block";
      document.getElementById('a3').innerHTML = `<img id="img33" src='assets/images/icon-minus.svg'>`
    } else {
      x.style.display = "none";
      document.getElementById('a3').innerHTML = `<img id="img44" src='assets/images/icon-plus.svg'>`
    }
  }
  function myFunction4() {
    var x = document.getElementById("p44");
    if (x.style.display === "none") {
      x.style.display = "block";
       document.getElementById('a4').innerHTML = `<img id="img55" src='assets/images/icon-minus.svg'>`
    } else {
      x.style.display = "none";
      document.getElementById('a4').innerHTML = `<img id="img66" src='assets/images/icon-plus.svg'>`
    }
  }