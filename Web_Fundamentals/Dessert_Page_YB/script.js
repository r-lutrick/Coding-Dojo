// Function for removing the Join Element
function joinRemover(element) {
    element.remove();
}
// A function used to incriment the provided ID's innerText
function loveIt(id) {
    document.querySelector(id).innerText++;
}

// Function for displaying the alert for the Search Bar
function searchAlert() {
    alert(
        'You are searching for "' +
        document.querySelector("#search-bar").value +
        '"'
    );
}