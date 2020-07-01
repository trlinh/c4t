var color = ["red", "yellow", "green", "blue"];
const bot = document.getElementById('bot');
const btn = document.getElementsByClassName('btn');
const up = document.getElementById('up');
var s = 0
const score = document.getElementById('score');


for (var z = 0; z < btn.length; z++) {
    
    btn[z].addEventListener('click', (e)=>{
     
        
        if (up.innerHTML == e.target.style.backgroundColor){
                s++
        }
        
        if (bot.style.color == e.target.style.backgroundColor) {
            s++
        }})
    btn[z].addEventListener('click', ()=> {      
        var i = Math.floor((Math.random()*2)+1);
        var x = Math.floor(Math.random()*4);
        var y = Math.floor(Math.random()*4);
        if (i == 1) {
            bot.innerHTML =""
            up.innerHTML=color[x]
            up.style.color=color[y]
            }
        else{
            up.innerHTML =""
            bot.innerHTML=color[x]
            bot.style.color=color[y]
        
        }

        score.innerHTML = s 
        
    })
}

function restart()  {
    location.reload();
    return false;
}