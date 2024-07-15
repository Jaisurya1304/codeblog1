let bars = document.querySelector(".bars");
let menu = document.querySelector("#menu");

bars.addEventListener("click", () => {
    menu.classList.toggle("mobile-menu");
});
