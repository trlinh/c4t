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
  

// Get the modal
var modal = document.querySelectorAll(".myModal");

// Get the button that opens the modal
var btn = document.querySelectorAll(".valkimg");

// Get the <span> element that closes the modal
var span = document.querySelectorAll(".close");

// When the user clicks on the button, open the modal
// btn[x].onclick = function() {
 
// }
for (var x=0; x<btn.length  ; x++){
     var final = x;
     btn[final].addEventListener( "click", ()=>{
     
        modal[final].style.display="block"
    //  console.log(e)
    //  console.log(x)
    })
    span[final].addEventListener("click",() => {
        modal[final].style.display = "none";
    } )
    window.onclick = function(event) {
        if (event.target == modal[final]) {
          modal[final].style.display = "none";
        }
      } 

    console.log(x)
}

 

//lambda expression

var filter_fix = document.getElementById("filter")
filter_fix.addEventListener("scroll", (e) =>{
    
    if (document.body.scrollTop > 147) {
      filter_fix.classList.add("fix-filter");
    } else {
      filter_fix.classList.remove("fix-filter");
    }
    
  })