// TODO :
function locations(substring,string){
    var a=[],i=-1;
    while((i=string.indexOf(substring,i+1)) >= 0) a.push(i);
    return a;
  }
function convertItemToTd(item,isHeader){
    item=item.trim();
    if ( isHeader){
        return "<th>"+item+"</th>"
    }
    if (item!="") {
        return "<td>"+item+"</td>"
    }
}
document.querySelector("#convert").addEventListener("click", () => {
    var table="<table><tbody>";
    const allValue=[];
    let rowHeader=[];
    const markdown=document.querySelector("#markdown").value;
    const items=markdown.trim().split("\n");
    for (let index = 0; index < items.length; index++) {
        const element = items[index];
        const itemInElement=element.split('|');
        itemInElement.shift();
        itemInElement.pop();
        if (locations("-",itemInElement[0].trim()).length>=3) {
            rowHeader.push(index);
        }
            allValue.push(itemInElement)
        
    }
for (let index = 0; index < allValue.length; index++) {
    const element = allValue[index];
    if(locations("-",element[0].trim()).length<3){
        var row="<tr>";
        if (rowHeader.includes(index+1) ) {
            const el= (element.map(x=>convertItemToTd(x,true)));
        row=row+  el.join("\n");
        }
        else{
            const el=element.map(x=>convertItemToTd(x,false));
            row=row+  el.join("\n");
        }
        row+="</tr>"
        table+=row;
    }
}
table+="</tbody></table>";

document.querySelector("#table").innerHTML=table;
});