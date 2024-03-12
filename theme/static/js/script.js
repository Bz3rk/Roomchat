document.addEventListener("DOMContentLoaded", function () {
  // Check if the form was submitted on a previous page load
  if (sessionStorage.getItem("formSubmitted")) {
    document.body.style.opacity = 1; // Remove opacity
    document.body.style.animation = "none"; // Disable the animation
    sessionStorage.removeItem("formSubmitted"); // Clear the flag
  }

  document.getElementById("myForm").addEventListener("submit", function () {
    // Set a flag in sessionStorage to indicate that the form was submitted
    sessionStorage.setItem("formSubmitted", "true");
  });
});

const menu = document.getElementById("menu");
const mobile = document.getElementById("mobile");
const closeBtn = document.getElementById("close");
const revealTopicBtn = document.querySelector("topicReveal");
console.log("hello world");

menu.addEventListener("click", () => {
  menu.classList.add("hidden");
  closeBtn.classList.remove("hidden");
  mobile.classList.remove("translate-x-full", "invisible");
  mobile.classList.add("translate-x-0", "visible");
});

closeBtn.addEventListener("click", function () {
  closeBtn.classList.add("hidden");
  menu.classList.remove("hidden");

  mobile.classList.remove("translate-x-0", "visible");
  mobile.classList.add("translate-x-full", "invisible");
});

revealTopicBtn.addEventListener("click", () => {
  console.log("clicked");
});
