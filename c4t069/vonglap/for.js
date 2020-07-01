// for(let i = 0; i>0; i++){
//     console.log(i)
// }
// while(true){
//     console.log('hello');
// }

// var a = [1,5,8,2,0,3,12,6,8,19,20]
// for(let i=0; i<a.length; i++){
//     if(a[i] % 2 == 1){
//         console.log(a[i])
//     }
// }

var minus=document.getElementById('minus')
var plus=document.getElementById('plus')
var num=document.getElementById('num')
var x = Number(num.textContent)

minus.addEventListener('click', () => {
    x--;
    num.innerHTML = x
})
plus.addEventListener('click', () => {
    x++;
    num.innerHTML = x
})
