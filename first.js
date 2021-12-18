
function helloWorld() {
    document.getElementById("demo").innerHTML = "Paragraph changed from js file.";
    document.getElementById("btn").onclick = myFunction;
}


function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
    document.getElementById("btn").onclick = helloWorld;
}