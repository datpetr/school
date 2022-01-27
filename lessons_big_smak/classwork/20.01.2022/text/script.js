function areaRectangle(){
    var a = Number(document.forma1.t1.value);
    var b = Number(document.forma1.t2.value);
    var c = Number(document.forma1.t3.value);


    if ((a < b + c) && (c < b + a) && (b< a + c)){
        var p = (a + b + c) / 2;
        s = Math.sqrt(p * (p - a) * (p - b) * (p - c))
        document.forma1.rez.value=s;
    }
    else {
        document.forma1.rez.value="треугольник не существует"
    }
}