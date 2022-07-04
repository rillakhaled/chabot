console.clear();

let typingEffect = function(element, speed){
  let text = element.innerText;
  element.innerText="";

  let i = 0;
  let timer =setInterval(function(){
    if(i<text.length){
      element.append(text.charAt(i))
      i++;
    }
    else{
      clearInterval(timer);
    }
  },speed)
}

const latest=document.querySelector('.message:last-of-type');
typingEffect(latest,25);
