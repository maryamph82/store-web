// script.js
document.addEventListener('DOMContentLoaded', () => {
    const userName = document.getElementById('userName');
    const userEmail = document.getElementById('userEmail');
    const purchaseList = document.getElementById('purchaseList');
    const cartList = document.getElementById('cartList');

// user information
    const user = {
        name: 'ali',
        email: 'ali@example.com'
    };

// Purchase history
    const purchases = [
        'shows',
        'scarf'
    ];

// cart list items
    const cartItems = [
        'scarf',
        'bag'
    ];

// user information
    userName.textContent = user.name;
    userEmail.textContent = user.email;

// Purchase history
    purchases.forEach(purchase => {
        const li = document.createElement('li');
        li.textContent = purchase;
        purchaseList.appendChild(li);
    });

// cart list items
    cartItems.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        cartList.appendChild(li);
    });
});
