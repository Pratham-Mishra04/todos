if(localStorage.getItem("completed")==null){
    var check_completed=[];
}
else{
    var check_completed=JSON.parse(localStorage.getItem("completed")); 
}
document.querySelector("#add").addEventListener("click",()=>{
    var title=document.querySelector("#title").value;
    var des=document.querySelector("#description").value;
    temp=[title,des];
    if(localStorage.getItem("item")==null){
        var itemlist=[];
    }
    else{
        var itemlist=JSON.parse(localStorage.getItem("item")); 
    }
    itemlist.push(temp);
    localStorage.setItem('item',JSON.stringify(itemlist));
})