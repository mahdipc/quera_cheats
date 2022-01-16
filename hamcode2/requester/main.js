async function urlloaded(url){
    var res="";
     res+="<div class=\"result\">";

    try {
    const request = new Request(url);
        
    const response=await fetch(request);
    if (response.status != 200) {
        res+="error";
        
    }
    else{
        const data=await response.json();
        res+=JSON.stringify(data);
    }
    } catch (error) {
        res+="error";
        
    }
    return res+"</div>";

}
document.querySelector("#send-requests").addEventListener("click", async () => {
    const urls=document.querySelector("#urls").value.replace( /\n/g, " " ).split(" ");
    document.querySelector("#results").innerHTML="";
    var ress="";
    for (let index = 0; index < urls.length; index++) {
        const url = urls[index].trim();
        if (url !=""){

            document.querySelector("#results").innerHTML+= await  urlloaded(url);
        //code


    }
    };



})