document.addEventListener("DOMContentLoaded",function(){
const animate=ScrollReveal({
       origin:"top",
       distance:"60px",
       duration:"1000",
       delay:"400",
       reset:true

});
animate.reveal(".header");
animate.reveal(".img-container",{origin:"left"});
animate.reveal(".home-contents",{origin:"right"});
animate.reveal(".icon-container,.box,.heading,.box,.heading-info,.info-container,.review-section,.box-container-user_adv,.adv_bx",{interval: 100});
});