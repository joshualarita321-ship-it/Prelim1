let face = ["Pogi", "Pangit", "Maganda", "BLeh", "Engkkk"];

function describeName() {
    let name = prompt("Enter your name: ");

   
    let word = face[Math.floor(Math.random() * face.length)];

    console.log(name + " is " + word + "!");
}

describeName();
