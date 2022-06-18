function showProT() {
    var bar = document.getElementById('cqbar');
    var labelT = document.getElementById('cqTtxt');
    var labelG = document.getElementById('cqGtxt');
    var labelC = document.getElementById('cqCtxt');
    var cqsT = document.getElementById('cqtaut');
    var cqsG = document.getElementById('cqgrop');
    var cqsC = document.getElementById('cqcomp');
    bar.style.width = "15%";
    labelT.style.color = "black";
    labelG.style.color = "grey";
    labelC.style.color = "grey";
    cqsT.style.display = "block";
    cqsG.style.display = "none";
    cqsC.style.display = "none";

}

function showProG() {
    var bar = document.getElementById('cqbar');
    var labelT = document.getElementById('cqTtxt');
    var labelG = document.getElementById('cqGtxt');
    var labelC = document.getElementById('cqCtxt');
    var cqsT = document.getElementById('cqtaut');
    var cqsG = document.getElementById('cqgrop');
    var cqsC = document.getElementById('cqcomp');
    bar.style.width = "50%";
    labelT.style.color = "black";
    labelG.style.color = "black";
    labelC.style.color = "grey";
    cqsT.style.display = "none";
    cqsG.style.display = "block";
    cqsC.style.display = "none";
}

function showProC() {
    var bar = document.getElementById('cqbar');
    var labelT = document.getElementById('cqTtxt');
    var labelG = document.getElementById('cqGtxt');
    var labelC = document.getElementById('cqCtxt');
    var cqsT = document.getElementById('cqtaut');
    var cqsG = document.getElementById('cqgrop');
    var cqsC = document.getElementById('cqcomp');
    bar.style.width = "85%";
    labelT.style.color = "black";
    labelG.style.color = "black";
    labelC.style.color = "black";
    cqsT.style.display = "none";
    cqsG.style.display = "none";
    cqsC.style.display = "block";
    
}