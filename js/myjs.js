// Toggle Competency Questions

function showProT() {
    var bar = document.getElementById('cqbar');
    var labelT = document.getElementById('cqTtxt');
    var labelG = document.getElementById('cqGtxt');
    var labelC = document.getElementById('cqCtxt');
    var cqsT = document.getElementById('cqtaut');
    var cqsG = document.getElementById('cqgrop');
    var cqsC = document.getElementById('cqcomp');
    bar.style.width = "25%";
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
    bar.style.width = "60%";
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
    bar.style.width = "100%";
    labelT.style.color = "black";
    labelG.style.color = "black";
    labelC.style.color = "black";
    cqsT.style.display = "none";
    cqsG.style.display = "none";
    cqsC.style.display = "block";
}

// Toggle Ontology Taut

function showTauttl() {
    var ser = document.getElementById("TautTTL");
    var graph = document.getElementById("TautGraph");
    ser.style.display = "block";
    graph.style.display = "none";
}

function showTautgraph() {
    var ser = document.getElementById("TautTTL");
    var graph = document.getElementById("TautGraph");
    ser.style.display = "none";
    graph.style.display = "block";
}

// Toggle Ontology Gropius

function showGropiusttl() {
    var ser = document.getElementById("GropiusTTL");
    var graph = document.getElementById("GropiusGraph");
    ser.style.display = "block";
    graph.style.display = "none";
}

function showGropiusgraph() {
    var ser = document.getElementById("GropiusTTL");
    var graph = document.getElementById("GropiusGraph");
    ser.style.display = "none";
    graph.style.display = "block";
}