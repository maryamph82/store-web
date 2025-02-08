
document.getElementById('product_choose').addEventListener('change', function () {

    const size = document.getElementById('size');
    const type = document.getElementById('product_choose').value;


    const textInput =  document.getElementById('text-input');


    textInput.style.display = 'none' ; 
    const type = document.getElementById('product_choose').value;
    const size = document.getElementById('size');

    if (type === 'scarf' || type === 'belt' || type === 'hat' || type === 'sock' || type === 'bag') {
        size.style.display = 'none';
    } else {
        size.style.display = 'block';
    }


})

document.getElementById('changePart').addEventListener('change', function () {
    const changePart = document.getElementById('changePart').value ; 
    const textInput = document.getElementById('text-input');
    const numberInput = document.getElementById('number-input');
    const pictureInput = document.getElementById('image-input');
    const sizeInput = document.getElementById('size-input').value;
    const genderInput = document.getElementById('gender-input');
    
    if (changePart === 'name' || changePart === 'color' || changePart === 'description' || changePart === 'brand' || changePart === 'material') {
        textInput.style.display = 'block'; 
    } else if (changePart === 'price' || changePart === 'quantity') {
        numberInput.style.display = 'block'; 
    }else if (changePart === 'picture') {
        pictureInput.style.display = 'block' ;
    }
    else if (changePart === 'gender') {
        genderInput.style.display = 'block' ; 
    } else if (changePart === 'size') {
        sizeInput.style.display = 'block' ;
    }


})

    const changePart = document.getElementById('changePart').value;

    
    if (changePart === 'name' || changePart === 'color' || changePart === 'description' || changePart === 'brand' || changePart === 'material') {
        textInput.style.display = 'block';
    }
    else if (changePart === 'price' || changePart === 'quantity') {

    }
    else if (changePart === 'picture') {

    }
    else if(changePart === 'gender' ){

    }else if(changePart === 'size'){

    }



