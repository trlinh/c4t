// Get the button that opens the modal
var modalBtns = [...document.querySelectorAll(".atkimg")];
modalBtns.forEach(function(btn){
    btn.onclick = function() {
        var modal = btn.getAttribute('data-modal');
        document.getElementById(modal).style.display="flex";
    }
  });

// Get the <span> element that closes the modal
var closeBtns = [...document.querySelectorAll(".close")];
closeBtns.forEach(function(btn){
  btn.onclick = function() {
    var modal = btn.closest('.myModal');
    modal.style.display = "none";
}});
    


 
window.onclick = function(event) {
    if (event.target.className === "myModal") {
        event.target.style.display = "none";
    }};