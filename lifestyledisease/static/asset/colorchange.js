document.addEventListener("DOMContentLoaded",function(){
       const colors=['navy','black'];
       let index=0;
       function changeColor()
       {
              const div=document.getElementById("main-data");
              div.style.background=colors[index]
              index++;
              if(index>=colors.length)
              {
                     index=0
              }
       }
       setInterval(changeColor,1000);
});