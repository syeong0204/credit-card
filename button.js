let btn = document.createElement('button');
btn.innerHTML = 'Add';
add_button = function(){
   //var str = document.getElementById('immediate').ariaValueMax();
    let count = parseInt(document.getElementById('count').innerHTML) +1;
    document.getElementById('count').innerHTML = count;
    let gender_count = 'gender_'+ count;

    let gender = document.getElementById('gender');
    let div = document.createElement('div');

    let input_male = document.createElement('input');
    input_male.setAttribute('type', 'radio');
    input_male.setAttribute('name', gender_count);
    input_male.setAttribute('value', 'male');
    let label_male = document.createElement('label');
    label_male.setAttribute('for', gender_count);
    label_male.innerHTML = 'Male';
    div.appendChild(input_male);
    div.appendChild(label_male);


    let input_female = document.createElement('input');
    input_female.setAttribute('type', 'radio');
    input_female.setAttribute('name', gender_count);
    input_female.setAttribute('value', 'female');
    let label_female = document.createElement('label');
    label_female.setAttribute('for', gender_count);
    label_female.innerHTML = 'Female';
    div.appendChild(input_female);
    div.appendChild(label_female);

    gender.appendChild(div);
}
document.body.appendChild(btn);