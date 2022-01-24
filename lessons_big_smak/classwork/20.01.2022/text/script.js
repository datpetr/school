function areaTriangle(){
    var a = document.forma1.a.value * 1;
    var b = document.forma1.b.value * 1;
    var c = document.forma1.c.value * 1;

    if (a * 1 + b * 1 <= c * 1) || (a * 1 + c * 1 <= b * 1) || (c * 1 + b * 1 <= a* 1) {
        document.forma1.res.value = 'такой треугольник не существует ';
    }
    else {
        var p = (a * 1 + b * 1 + c * 1) / 2;
        document.forma1.res.value = math.sqrt((p * (p - a * 1) * (p - b * 1) * (p - c * 1)));
    }

}
