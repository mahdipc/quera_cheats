const paramTemplate = '<input class="q-input" placeholder="Param Key" />';
const queryTemplate =
  '<input class="q-input" placeholder="Query Key" /><input class="q-input" placeholder="Query Value" />';
const baseUrl = "https://website.ir";
function removeDuplicates(data, key) {
  return [
    ...new Map(data.map(item => [key(item), item])).values()
  ]
};
const addNewParam = () => {
   var elmnt = document.getElementById("params-container").getElementsByClassName("q-input")
   if (elmnt[elmnt.length-1].value!=""){
    var div = document.createElement('div');
    div.setAttribute('class', 'keyValue-box');
    div.innerHTML = '<input class="q-input" placeholder="Param" />';
    document.getElementById("params-container").appendChild(div);
   }
};
const addNewQuery = () => {
  var elmnt = document.getElementById("queries-container").getElementsByClassName("q-input")
  if (elmnt[elmnt.length-2].value!="" ){
   var div = document.createElement('div');
   div.setAttribute('class', 'keyValue-box');
   div.innerHTML = '<input class="q-input" placeholder="Query Key" /><input class="q-input" placeholder="Query Value" />';
   document.getElementById("queries-container").appendChild(div);
  }


};
const generateURL = () => {
  var q=[];
  var queries = document.getElementById("queries-container").getElementsByClassName("q-input")
  for (let index = 0; index < queries.length; index+=2) {
    if (queries[index].value!="" && queries[index+1].value!="" ) {
      q.push({ key:queries[index].value,value:queries[index+1].value})
    }
  }
  q.reverse();
  q=removeDuplicates(q,item=>item.key).map(item=>item.key.trim()+"="+item.value.trim())
  q.reverse()
  q=q.join('&')

  var params=[];
  var elmnt = document.getElementById("params-container").getElementsByClassName("q-input")
  for (let index = 0; index < elmnt.length; index++) {
    const element = elmnt[index].value;
    if (element!="") {
      params.push(element)
    }
  }
  var parm=params.join('/');
  if (parm!="") parm='/'+parm;
  if (q!="") q='?'+q;
  var url='https://website.ir';
   url+=parm;
   url+=q;
  renderUrl(url)
};

const renderUrl = (url) => {
  const el = document.getElementById("url-container");
  el.innerHTML = `<p>${url}</p>`;
};

document.getElementById("param-submit").addEventListener("click", addNewParam);
document.getElementById("query-submit").addEventListener("click", addNewQuery);
document.getElementById("generate").addEventListener("click", generateURL);
