const leftSide = document.querySelector(".left-side");
const rightSide = document.querySelector(".right-side");

// InitialValues
let leftList = [
  { id: "item1", checked: false, title: "PHP" },
  { id: "item2", checked: false, title: "Python" },
  { id: "item3", checked: false, title: "Ruby" },
  { id: "item4", checked: false, title: "C++" },
];
let rightList = [
  { id: "item5", checked: false, title: "HTML" },
  { id: "item6", checked: false, title: "Css" },
  { id: "item7", checked: false, title: "JavaScript" },
  { id: "item8", checked: false, title: "Java" },
];

renderDom(leftList, rightList);
function rend(leftListToRender, rightListToRender) {
  if (leftListToRender.length==0){
    document.querySelector(".all-to-right").classList.add("disabled");
    document.querySelector(".checked-to-right").classList.add("disabled");
    document.querySelector(".all-to-left").classList.remove("disabled");
    document.querySelector(".checked-to-left").classList.remove("disabled");
  }
  else if(rightListToRender.length==0){
    
    document.querySelector(".all-to-right").classList.remove("disabled");
    document.querySelector(".checked-to-right").classList.remove("disabled");
    document.querySelector(".all-to-left").classList.add("disabled");
    document.querySelector(".checked-to-left").classList.add("disabled");
  }
  else{
    document.querySelector(".all-to-right").classList.remove("disabled");
    document.querySelector(".checked-to-right").classList.remove("disabled");
    document.querySelector(".all-to-left").classList.remove("disabled");
    document.querySelector(".checked-to-left").classList.remove("disabled");
  }
  renderDom(leftListToRender, rightListToRender)
}
// Render Dom
function renderDom(leftListToRender, rightListToRender) {
  leftListToRender.forEach((item) => {
    leftSide.innerHTML += `<div class="box">
        <input type="checkbox" class="input-box" id="${item.id}" />
        <label for="${item.id}">${item.title}</label>
        </div>`;
  });

  rightListToRender.forEach((item) => {
    rightSide.innerHTML += `<div class="box">
          <input type="checkbox" class="input-box" id="${item.id}" />
          <label for="${item.id}">${item.title}</label>
          </div>`;
  });

  registerEvents();
}

// Clear Dom
function clearDom() {
  document.querySelectorAll(".side").forEach((el) => {
    el.innerHTML = "";
  });
}

document.querySelector(".all-to-right").addEventListener("click",  () => {
  rightList.push(...leftList)
  leftList=[];
  leftSide.innerHTML="";
  rightSide.innerHTML="";
  rend(leftList,rightList);
});
document.querySelector(".checked-to-right").addEventListener("click",  () => {
 var s= document.querySelector(".left-side").querySelectorAll(".input-box");
 for (let index = 0; index < s.length; index++) {
   const element = s[index];
   if (element.checked){
   const tt= leftList.filter(x=>{
     if(x.id==element.id){
       return x;
     }
      
    });
    rightList.push(...tt);
    leftList = leftList.filter(function(item) {
      return item !== tt[0]
  })
   }
 }
 
 leftSide.innerHTML="";
 rightSide.innerHTML="";
 rend(leftList,rightList);
});
document.querySelector(".all-to-left").addEventListener("click",  () => {
  leftList.push(...rightList)
  rightList=[];
  leftSide.innerHTML="";
  rightSide.innerHTML="";
  rend(leftList,rightList);
});

document.querySelector(".checked-to-left").addEventListener("click",  () => {
  var s= document.querySelector(".right-side").querySelectorAll(".input-box");
  for (let index = 0; index < s.length; index++) {
    const element = s[index];
    if (element.checked){
    const tt= rightList.filter(x=>{
      if(x.id==element.id){
        return x;
      }
       
     });
     rightList = rightList.filter(function(item) {
      return item !== tt[0]
  })
     leftList.push(...tt);
    }
  }
  
  leftSide.innerHTML="";
  rightSide.innerHTML="";
  rend(leftList,rightList);
 });
// Event
function registerEvents() {}
