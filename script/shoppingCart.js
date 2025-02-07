localStorage.setItem('product', 'products');

window.addEventListener('load', function () { document.body.classList.add('loaded'); });
function final_buy() {
    document.getElementById("cart").innerHTML = "Your purchase request has been sent to the admin.";
}