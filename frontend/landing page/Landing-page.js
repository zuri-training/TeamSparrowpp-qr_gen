function myFunction() {
    var x = document.getElementsByClassName("nav-link");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }