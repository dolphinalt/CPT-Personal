var sidebar_Expanded = 0;
function showSidebar() {
  var sidebar_Width = document.getElementById("sidebar0").offsetWidth;
  if (sidebar_Expanded == 0) {
    document.getElementById("sidebar0").style.transition = "left 0.25s ease-in-out";
    document.getElementById("sidebar0").style.left = "-74.5px";
    setTimeout(function() {
      document.getElementById("sidebar1").style.transition = "top 0.5s ease-in-out, opacity 0.8s ease-in-out";
      document.getElementById("sidebar1").style.top = "117px";
      document.getElementById("sidebar1").style.opacity = "0.5";
      document.getElementById("sidebar2").style.transition = "top 0.6s ease-in-out, opacity 0.8s ease-in-out";
      document.getElementById("sidebar2").style.top = "197px";
      document.getElementById("sidebar2").style.opacity = "0.5";
      document.getElementById("sidebar3").style.transition = "top 0.7s ease-in-out, opacity 0.8s ease-in-out";
      document.getElementById("sidebar3").style.top = "277px";
      document.getElementById("sidebar3").style.opacity = "0.5";
      document.getElementById("sidebar4").style.transition = "top 0.8s ease-in-out, opacity 0.8s ease-in-out";
      document.getElementById("sidebar4").style.top = "357px";
      document.getElementById("sidebar4").style.opacity = "0.5";
    }, 500);
    sidebar_Expanded = 1;
  } else if (sidebar_Expanded == 1) {
    document.getElementById("sidebar1").style.transition = "top 0.8s ease-in-out, opacity 0.8s ease-in-out";
    document.getElementById("sidebar1").style.top = "97px";
    document.getElementById("sidebar1").style.opacity = "0";
    document.getElementById("sidebar2").style.transition = "top 0.7s ease-in-out, opacity 0.8s ease-in-out";
    document.getElementById("sidebar2").style.top = "177px";
    document.getElementById("sidebar2").style.opacity = "0";
    document.getElementById("sidebar3").style.transition = "top 0.6s ease-in-out, opacity 0.8s ease-in-out";
    document.getElementById("sidebar3").style.top = "257px";
    document.getElementById("sidebar3").style.opacity = "0";
    
    document.getElementById("sidebar4").style.transition = "top 0.5s ease-in-out, opacity 0.8s ease-in-out";
    document.getElementById("sidebar4").style.top = "337px";
    document.getElementById("sidebar4").style.opacity = "0";
    setTimeout(function() {
      document.getElementById("sidebar0").style.transition = "left 0.25s ease-in-out";
      document.getElementById("sidebar0").style.left = "-" + sidebar_Width + "px";
    }, 500);
    sidebar_Expanded = 0;
  }
}