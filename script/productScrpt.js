const productName = document.querySelector('.name');  
const productPrice = document.querySelector('.price');  
const productDesc = document.querySelector('.Description');  
const productImage = document.querySelector('img');  
const productsArray = [];  

window.addEventListener('load', function () {  
    document.body.classList.add('loaded');  
    loadProducts(); 
});  

function loadProducts() {  
    const existingProducts = JSON.parse(localStorage.getItem('products'));  
    if (existingProducts) {  
        existingProducts.forEach(product => productsArray.push(product)); 
    }  
}  

function buy() {  
    document.getElementById("paragraph").innerHTML = "This product has been added to your shopping list."; 

    const product = {  
        name: productName.innerHTML,  
        price: productPrice.innerHTML,  
        desc: productDesc.innerHTML,  
        img: productImage.src  
    };  

    productsArray.push(product);

 
    let storedProducts = localStorage.getItem('products');  
    if (storedProducts === null) {  
        localStorage.setItem('products', JSON.stringify([product])); 
    } else {  
        let existingProducts = JSON.parse(storedProducts);  
        existingProducts.push(product);  
        localStorage.setItem('products', JSON.stringify(existingProducts));  
    }  
}  


console.log(productsArray);  