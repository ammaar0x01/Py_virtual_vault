/*
script.js 
=========
*/


// Type writer effect 
// original from https://www.w3schools.com/howto/howto_js_typewriter.asp
function typeWriter(text="Hello world", speed=150) {
    let i = 0;
    if (i < text.length) {
        document.getElementById("app").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}
// --------------------------------------
// onload = typeWriter()

