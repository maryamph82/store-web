window.addEventListener('load', function () { document.body.classList.add('loaded'); });
window.addEventListener('load', () => final_buy)
function final_buy() { 
    document.getElementById("cart").innerHTML = "Your purchase request has been sent to the admin.";
}

let productArray = JSON.parse(localStorage.products)

console.log(productArray)