const input = document.querySelector('input')
let search = ''
input.addEventListener('keydown', searchFunc)
function searchFunc(event) {
    if (event.key == "Enter") {
        console.log(event.key)
        console.log("search " + search)
    } else {
        search = search + event.key
    }
}