function change() {
    var typecb = document.querySelectorAll("#typecb input[type='checkbox']");
    var weakcb = document.querySelectorAll("#weakcb input[type='checkbox']");
    var immunecb = document.querySelectorAll("#immunecb input[type='checkbox']");
    var filters = {
        type: getClassOfCheckedCheckboxes(typecb),
        weak: getClassOfCheckedCheckboxes(weakcb),
        immune: getClassOfCheckedCheckboxes(immunecb),
    };
    filterResults(filters);
    
};
function getClassOfCheckedCheckboxes(checkboxes) {
    var classes = [];
  
    if (checkboxes && checkboxes.length > 0) {
        for (var i = 0; i < checkboxes.length; i++) {
            var cb = checkboxes[i];
    
            if (cb.checked) {
            classes.push(cb.getAttribute("rel"));
            }
        }
    }
  
    return classes;
  };

function filterResults(filters) {
    var rElems = document.querySelectorAll(".bossimg");
    var hiddenElems = [];
  
    if (!rElems || rElems.length <= 0) {
      return;
    }

    for (var i = 0; i < rElems.length; i++) {
        var el = rElems[i];
    
        if (filters.type.length > 0) {
            var isHidden = true;
        
            for (var j = 0; j < filters.type.length; j++) {
                var filter = filters.type[j];
        
                if (el.classList.contains(filter)) {
                    isHidden = false;
                    break;
                }
            }
        
            if (isHidden) {
                hiddenElems.push(el);
            }
        }
    
        if (filters.immune.length > 0) {
          var isHidden = true;
    
            for (var j = 0; j < filters.immune.length; j++) {
                var filter = filters.immune[j];
        
                if (el.classList.contains(filter)) {
                    isHidden = false;
                    break;
                }
            }
        
            if (isHidden) {
                hiddenElems.push(el);
            }
        }

        if (filters.weak.length > 0) {
            var isHidden = true;
      
              for (var j = 0; j < filters.weak.length; j++) {
                  var filter = filters.weak[j];
          
                  if (el.classList.contains(filter)) {
                  isHidden = false;
                  break;
                  }
              }
          
              if (isHidden) {
                  hiddenElems.push(el);
              }
          }
    }   
    
    for (var i = 0; i < rElems.length; i++) {
        rElems[i].style.display = "inline-block";
    }

    if (hiddenElems.length <= 0) {
        return;
    }

    for (var i = 0; i < hiddenElems.length; i++) {
        hiddenElems[i].style.display = "none";
    }
}
window.onscroll = function() {filter_fix()};
var banner = document.getElementById("bannerimg")
var bosslist = document.getElementById("bosslist")
var sticky = banner.offsetHeight
var filter= document.getElementById("filter")
var limit = bosslist.offsetHeight
function filter_fix(){
    
    if (window.pageYOffset >= sticky & window.pageYOffset < limit) {
        filter.classList.add("fix-filter");
        bosslist.classList.add("newbosslist")
    } else {
        filter.classList.remove("fix-filter");
        bosslist.classList.remove("newbosslist")
    }
    
}

// Get the button that opens the modal
var modalBtns = [...document.querySelectorAll(".bossimg")];
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
      