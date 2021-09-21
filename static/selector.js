var job2 = document.getElementById('job2');
var home = document.getElementById('housetype');

finjob = job2[0].value;
console.log(finjob);

function selector(jobc){
console.log(jobc);
}

function homechange(home){
console.log(home);
}

function marchange(mar){
    console.log(mar);
}

function educhange(edu){
    console.log(edu);
}

function jobchange(edu){
    console.log(edu);
}

function yeshome(edu){
    console.log(edu);
}

function nohome(edu){
    console.log(edu);
}

function yescar(edu){
    console.log(edu);
}

function nocar(edu){
    console.log(edu);
}

function famsize(edu){
    console.log(edu);
}



let first = "Me"
console.log(first)

function pr() {
    document.getElementById("result").innerHTML = document.getElementById('fname').value + " " + document.getElementById('lname').value;
    first = document.getElementById('fname').value;
}

let income = "0"
console.log(income);

let children = "0"
console.log(children);

let dob = 0;
let dow = 0;

function numbers(){
    income = document.getElementById('income').value;
    children = document.getElementById('children').value;
    dob = document.getElementById('dob').value;
    dow = document.getElementById('dow').value;
}

let fams = 0;

function famsize(){
    fams = document.getElementById('fam').value;
}

let mobile = document.getElementById('mobphone').value;
mobile = mobile[0].value;

let work = document.getElementById('workphone').value;
work = work[0].value;

let homephone = document.getElementById('phone').value;
homephone = homephone[0].value;

let email = document.getElementById('email').value;
email = email[0].value;

let gender = document.getElementById('genders').value;
gender = gender[0].value;

let car = document.getElementById('car').value;
console.log(car);

let homes = document.getElementById('home').value;
console.log(homes);

let inctype = document.getElementById('job').value;
inctype = inctype[0].value;

let edu = document.getElementById('education').value;
edu = edu[0].value;

let marr = document.getElementById('marriage').value;
marr = marr[0].value;

let ht = document.getElementById('housetype').value;
ht = ht[0].value;

let occ = document.getElementById('job2').value;
occ = occ[0].value;

function linkmaker(){
        occ = document.getElementById('job2').value;
        ht = document.getElementById('housetype').value;
        edu = document.getElementById('education').value;
        marr = document.getElementById('marriage').value;
        inctype = document.getElementById('job').value;
        homes = document.getElementById('home').value;
        car = document.getElementById('car').value;
        gender = document.getElementById('genders').value;
        mobile = document.getElementById('mobphone').value;
        work = document.getElementById('workphone').value;
        homephone = document.getElementById('phone').value;
        email = document.getElementById('email').value;
        fams = document.getElementById('fam').value;
        income = document.getElementById('income').value;
        children = document.getElementById('children').value;
        dob = document.getElementById('dob').value;
        dow = document.getElementById('dow').value;
        document.write(`<a href="http://127.0.0.1:5000/test/${children}/${income}/${dob}/${dow}/${mobile}${work}${homephone}${email}/${fams}/${gender}${car}${homes}${inctype}${edu}${marr}${ht}/${occ} ">Youtube</a>`);
}

