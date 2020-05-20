var z = {
    name: 'Diep',
    age: 17,
    favouriteMovie: 'Tom Jerry',
    address: 'Thanh Xuan',
}
var l = {
    name: 'Linh',
    age: 17,
    favouriteMovie: 'anime',
    address: 'Thanh Xuan',
}
var a = prompt('Ban muon biet Diep hay Linh?')
if (a == 'Diep') { 
    console.log('ten ban la: '+ z.name)
    console.log('tuoi cua ban: '+z.age)
    console.log('bo phim yeu thich: '+z.favouriteMovie)
    console.log('nha ban o: '+z.address) 
} 
if (a=='Linh') {
    console.log('ten ban la: '+ l.name)
    console.log('tuoi cua ban: '+l.age)
    console.log('bo phim yeu thich: '+l.favouriteMovie)
    console.log('nha ban o: '+l.addresls) 
}