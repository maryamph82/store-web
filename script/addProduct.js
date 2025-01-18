document.getElementById('productType').addEventListener('change', function() {
    const productType = document.getElementById('productType').value;
    const commonFields = document.getElementById('commonFields');
    const hoodieFields = document.getElementById('hoodieFields');
    const tshirtFields = document.getElementById('tshirtFields');
    const shoeFields = document.getElementById('shoeFields');
    const submitButton = document.querySelector('button[type="submit"]');

    commonFields.style.display = productType ? 'block' : 'none';
    hoodieFields.style.display = productType === 'hoodie' ? 'block' : 'none';
    tshirtFields.style.display = productType === 'tshirt' ? 'block' : 'none';
    shoeFields.style.display = productType === 'shoe' ? 'block' : 'none';
    submitButton.style.display = productType ? 'block' : 'none';
});

document.getElementById('productForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const product = {
        type: document.getElementById('productType').value,
        name: document.getElementById('name').value,
        description: document.getElementById('description').value,
        color: document.getElementById('color').value,
        image: document.getElementById('image').files[0],
    };

// based on product type difrents inputs give

    if (product.type === 'hoodie') {
        product.size = document.getElementById('size').value;
        product.hasHood = document.getElementById('hasHood').checked;
    }

    if (product.type === '') {
        product.size = document.getElementById('size').value;
        product.hasHood = document.getElementById('hasHood').checked;
    }

    if (product.type === 'hoodie') {
        product.size = document.getElementById('size').value;
        product.hasHood = document.getElementById('hasHood').checked;
    }

      

    console.log('Product added:', product);


});
