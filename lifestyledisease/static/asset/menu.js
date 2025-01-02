const menu=document.querySelector('#menu-btn')
const nav=document.querySelector('.navbar')

menu.onclick=()=>{
       menu.classList.toggle('fa-times')
       nav.classList.toggle("active")
       console.log("click")
}
window.onscroll=()=>{
       menu.classList.remove('fa-times')
       nav.classList.remove("active")
}