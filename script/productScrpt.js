const productName = document.querySelector('.name');  
const productPrice = document.querySelector('.price');  
const productDesc = document.querySelector('.Description');  
const productImage = document.querySelector('img');  
const productsArray = [];  

window.addEventListener('load', function () {  
    document.body.classList.add('loaded');  
<<<<<<< HEAD
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
=======
    loadProducts(); // بارگذاری محصولات از localStorage  
});  
>>>>>>> 37cfd20c77350dffb3cc801eb701272c26ceeb59

function loadProducts() {  
    const existingProducts = JSON.parse(localStorage.getItem('products'));  
    if (existingProducts) {  
        existingProducts.forEach(product => productsArray.push(product)); // اضافه کردن محصولات موجود به آرایه  
    }  
}  

<<<<<<< HEAD
=======
function buy() {  
    document.getElementById("paragraph").innerHTML = "این محصول به لیست خرید شما اضافه شد";  

    const product = {  
        name: productName.innerHTML,  
        price: productPrice.innerHTML,  
        desc: productDesc.innerHTML,  
        img: productImage.src  
    };  

    productsArray.push(product); // اضافه کردن محصول به آرایه  

    // ذخیره کردن در localStorage  
    let storedProducts = localStorage.getItem('products');  
    if (storedProducts === null) {  
        localStorage.setItem('products', JSON.stringify([product])); // ذخیره به عنوان آرایه  
    } else {  
        let existingProducts = JSON.parse(storedProducts);  
        existingProducts.push(product);  
        localStorage.setItem('products', JSON.stringify(existingProducts));  
    }  
}  

// برای آزمایش، می‌توانید آرایه محصولات را در کنسول چاپ کنید  
>>>>>>> 37cfd20c77350dffb3cc801eb701272c26ceeb59
console.log(productsArray);  