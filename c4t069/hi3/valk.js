function change() {
    var typecb = document.querySelectorAll("#typecb input[type='checkbox']");
    var valkcb = document.querySelectorAll("#valkcb input[type='checkbox']");
    var featurescb = document.querySelectorAll("#featurescb input[type='checkbox']");
    var filters = {
        type: getClassOfCheckedCheckboxes(typecb),
        valk: getClassOfCheckedCheckboxes(valkcb),
        feature: getClassOfCheckedCheckboxes(featurescb),
    };
    filterResults(filters);
    console.log(typecb, valkcb, featurescb, filters)
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
    var rElems = document.querySelectorAll("#valklist img");
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
    
        if (filters.valk.length > 0) {
          var isHidden = true;
    
            for (var j = 0; j < filters.valk.length; j++) {
                var filter = filters.valk[j];
        
                if (el.classList.contains(filter)) {
                    isHidden = false;
                    break;
                }
            }
        
            if (isHidden) {
                hiddenElems.push(el);
            }
        }

        if (filters.feature.length > 0) {
            var isHidden = true;
      
              for (var j = 0; j < filters.feature.length; j++) {
                  var filter = filters.feature[j];
          
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
  



// Get the button that opens the modal
var modalBtns = [...document.querySelectorAll(".valkimg")];
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
      

 

//lambda expression

window.onscroll = function() {filter_fix()};
var banner = document.getElementById("bannerimg")
var valklist = document.getElementById("valklist")
var sticky = banner.offsetHeight
var filter= document.getElementById("filter")
var limit = valklist.offsetHeight
function filter_fix(){
    
    if (window.pageYOffset >= sticky & window.pageYOffset < limit) {
        filter.classList.add("fix-filter");
        valklist.classList.add("newvalklist")
    } else {
        filter.classList.remove("fix-filter");
        valklist.classList.remove("newvalklist")
    }
    
}