const resultTag = document.getElementById("result");
const textArea = document.getElementById("textarea");
const submitBtn = document.getElementById("submit-btn");

// TODO: Write your codes here
function invalidCode(txt){

}
function typeclass(value){
    return typeof value;
}
function objectJson(txt){
    txt=txt.trim().replace("\n","");
    var ul="<ul>";

    const rows=txt.slice(1,-1).split(",");
    rows.forEach(row => {
        const keyValue=row.split(":");
        if (keyValue[1][0]=="{") {
            ul+="<li><span class=\"json-viewer-object-start\">"+keyValue[0]+"{</span>";

            ul+= "<ul>"+objectJson(keyValue[1]);

            ul+="<span class=\"json-viewer-object-start\">}</span></li>";
        }else{
           ul+="<span class=\"key\">"+ keyValue[0]+"</span><span class=\"value-"+typeclass(keyValue[1])+"\">"+keyValue[1]+"</span>";
        }
    });
    ul+="</ul>";
    return ul;
}
document.querySelector("#submit-btn").addEventListener("click", () => {
    const jsonText=document.querySelector("#textarea").value;

    const result= objectJson(jsonText);
    console.log(result);

});
