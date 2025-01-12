const productName = document.querySelector('.name')
const productPrice = document.querySelector('.price')
const productDesc = document.querySelector('.Description')
const productImage = document.querySelector('img')
const productsArray = []

window.addEventListener('load', function () { document.body.classList.add('loaded'); });


function buy() {
    document.getElementById("paragraph").innerHTML = "Paragraph changed.";

    localStorage.setItem('name', productName.innerHTML)
    localStorage.setItem('price', productPrice.innerHTML)
    localStorage.setItem('desc', productDesc.innerHTML)
    localStorage.setItem('Img', productImage.src)


    let product = [{
        name: localStorage.getItem('name'),
        price: localStorage.getItem('price'),
        desc: localStorage.getItem('desc'),
        img: localStorage.getItem('Img')
    },
    ]



    productsArray.push({ product })
    localStorage.setItem('products', (localStorage.getItem('products')) + JSON.stringify(productsArray));
}


console.log(productsArray)

//  اضافه کردن همه ی محصولاتی که
//  کابر انتخاب میکند (وقتی که دکمه ی خرید را میزند
//  ) به صفحه ی سبد حرید و نشان دادن ان ها 
