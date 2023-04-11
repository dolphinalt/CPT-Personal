function swapObject (left, top, width, index, src, object) {
  document.getElementById(object).style.left = left + "px";
  document.getElementById(object).style.top = top + "px";
  document.getElementById(object).width = width;
  document.getElementById(object).src = src;
  document.getElementById(object).style.zIndex = index;
}

function swap (direction) {
    if (direction == "left") {
      swapObject(515, 91, 507, 1, "./assets/svg/schedulebox_main.svg", "schedule0");
      swapObject(901, 136, 432, 0, "./assets/svg/schedulebox_back.svg", "schedule1");
      document.getElementById("class0").style.opacity = "0.25";
      document.getElementById("class1").style.opacity = "0.25";
      document.getElementById("class2").style.opacity = "0.25";
      document.getElementById("class3").style.opacity = "0.25";
      document.getElementById("class4").style.opacity = "0.25";
      document.getElementById("class0entry").style.opacity = "1";
      document.getElementById("class0entry").style.zIndex = "2";
      document.getElementById("class1entry").style.opacity = "1";
      document.getElementById("class1entry").style.zIndex = "2";
      document.getElementById("class2entry").style.opacity = "1";
      document.getElementById("class2entry").style.zIndex = "2";
      document.getElementById("class3entry").style.opacity = "1";
      document.getElementById("class3entry").style.zIndex = "2";
      document.getElementById("class4entry").style.opacity = "1";
      document.getElementById("class4entry").style.zIndex = "2";
      document.getElementById("teach0").style.opacity = "0";
      document.getElementById("teach1").style.opacity = "0";
      document.getElementById("teach2").style.opacity = "0";
      document.getElementById("teach3").style.opacity = "0";
      document.getElementById("teach4").style.opacity = "0";
      document.getElementById("teach0entry").style.opacity = "0";
      document.getElementById("teach0entry").style.zIndex = "-1";
      document.getElementById("teach1entry").style.opacity = "0";
      document.getElementById("teach1entry").style.zIndex = "-1";
      document.getElementById("teach2entry").style.opacity = "0";
      document.getElementById("teach2entry").style.zIndex = "-1";
      document.getElementById("teach3entry").style.opacity = "0";
      document.getElementById("teach3entry").style.zIndex = "-1";
      document.getElementById("teach4entry").style.opacity = "0";
      document.getElementById("teach4entry").style.zIndex = "-1";
    } else if (direction == "right") {
      swapObject(201, 136, 432, 0, "./assets/svg/schedulebox_back.svg", "schedule0");
      swapObject(515, 91, 507, 1, "./assets/svg/schedulebox_main.svg", "schedule1");
      document.getElementById("schedule0").class = "scheduleMid";
      document.getElementById("schedule1").src = "./assets/svg/schedulebox_main.svg";
      document.getElementById("schedule1").class = "scheduleTop";
      document.getElementById("class0").style.opacity = "0";
      document.getElementById("class1").style.opacity = "0";
      document.getElementById("class2").style.opacity = "0";
      document.getElementById("class3").style.opacity = "0";
      document.getElementById("class4").style.opacity = "0";
      document.getElementById("class0entry").style.opacity = "0";
      document.getElementById("class0entry").style.zIndex = "-1";
      document.getElementById("class1entry").style.opacity = "0";
      document.getElementById("class1entry").style.zIndex = "-1";
      document.getElementById("class2entry").style.opacity = "0";
      document.getElementById("class2entry").style.zIndex = "-1";
      document.getElementById("class3entry").style.opacity = "0";
      document.getElementById("class3entry").style.zIndex = "-1";
      document.getElementById("class4entry").style.opacity = "0";
      document.getElementById("class4entry").style.zIndex = "-1";
      document.getElementById("teach0").style.opacity = "0.25";
      document.getElementById("teach1").style.opacity = "0.25";
      document.getElementById("teach2").style.opacity = "0.25";
      document.getElementById("teach3").style.opacity = "0.25";
      document.getElementById("teach4").style.opacity = "0.25";
      document.getElementById("teach0entry").style.opacity = "1";
      document.getElementById("teach0entry").style.zIndex = "2";
      document.getElementById("teach1entry").style.opacity = "1";
      document.getElementById("teach1entry").style.zIndex = "2";
      document.getElementById("teach2entry").style.opacity = "1";
      document.getElementById("teach2entry").style.zIndex = "2";
      document.getElementById("teach3entry").style.opacity = "1";
      document.getElementById("teach3entry").style.zIndex = "2";
      document.getElementById("teach4entry").style.opacity = "1";
      document.getElementById("teach4entry").style.zIndex = "2";
    }
  }