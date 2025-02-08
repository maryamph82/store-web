
document.getElementById('product_choose').addEventListener('change', function () {
    const textInput =  document.getElementById('text-input');


    textInput.style.display = 'none' ; 
    const type = document.getElementById('product_choose').value;
    const size = document.getElementById('size');
    if (type === 'scarf' || type === 'belt' || type === 'hat' || type === 'sock' || type === 'bag') {
        size.style.display = 'none';
    } else {
        size.style.display = 'block';
    }
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

})
