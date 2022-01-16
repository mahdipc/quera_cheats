
function printSierpinski(ns)
{
    n=[2,4,8,16,32,64,128][ns-1];
    const container= document.querySelector("#container");
    var s="";

    for (var y = n-1 ; y >= 0; y--) {
        // for (var i = 0; i < y; i++) {
            s=s+"<div class=\"row\">";
        // }
 
        for (var x = 0; x + y < n; x++) {
 
            if ((x & y) != 0)
            {  
                s+= "<div class=\"block\"></div>";
            }
            else
            {    
                s+="<div class=\"block active\"></div>";
               
            }
        }
 
        s+="</div>";
        container.innerHTML+=s;
        s="";
    }
}
 

 

 
document.querySelector("#submit").addEventListener("click", () => {
    document.querySelector("#container").innerHTML="";
    const n=document.querySelector("#number").value;
// Function calling
printSierpinski(n);

});