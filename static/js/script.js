console.clear();
function typingEffect(element,speed){
  let text=element.innerText;
  element.innerText="";
  var i=0;
  var timer=setInterval(function(){
    if(i<text.length){
      element.append(text.charAt(i))
      i++;
    }
    else{
      clearInterval(timer);
    }
  },speed)

}

const latest=document.querySelector('.message:nth-of-type(2)');
typingEffect(latest,25);
