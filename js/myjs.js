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

function showTurtle(turtle, graphviz) {
    var ser = document.getElementById(turtle);
    var graph = document.getElementById(graphviz);
    graph.style.display = "none";
    if (ser.style.display === "none" || ser.style.display === "") {
        ser.style.display = "block";
    } else {
        ser.style.display = "none";
    }
}

function showGraph(turtle, graphviz) {
    var ser = document.getElementById(turtle);
    var graph = document.getElementById(graphviz);
    ser.style.display = "none";
    if (graph.style.display === "none" || graph.style.display === "") {
        graph.style.display = "block";
    } else {
        graph.style.display = "none";
    }
}
