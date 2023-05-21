if(JSON.parse(localStorage.getItem("item")).length==0){
    var elem=document.createElement("h1")
    elem.innerHTML="<h1 id=\"empty_heading\">The List is empty</h1><h2 class=\"card-subtitle mb-2 text-muted\">Add Items from the Home tab!</h2>"
    document.querySelector(".container").appendChild(elem);
}
else{
    var elem=document.createElement("h1")
    elem.innerHTML="<h1 id=\"heading\">Your Items</h1>"
    document.querySelector(".container").appendChild(elem);


if(localStorage.getItem("completed")==null){
    var check_completed=[];
}
else{
    var check_completed=JSON.parse(localStorage.getItem("completed")); 
}

if (localStorage.getItem("item")!=null){

    var itemstr=localStorage.getItem('item');
    var items=JSON.parse(itemstr);
    
    for(var i=0;i<items.length;i++){
        temp_sno=(i+1).toString();
        temp_title=(items[i][0]).toString();
        temp_des=items[i][1];

        var box=document.createElement("div")
        box.setAttribute("class","card bg-light mb-3");
        box.style.width="18rem";
        var header=document.createElement("div")
        header.classList.add("card-header");
        header.textContent=temp_sno;
        var body=document.createElement("div");
        body.classList.add("card-body");
        var card_title=document.createElement("h5");
        card_title.classList.add("card-title");
        card_title.textContent=temp_title;
        var desp=document.createElement("p");
        desp.classList.add("card-text");
        desp.textContent=temp_des;
        

        var button1=document.createElement("div")
        button1.classList.add("button")
        button1.innerHTML="<button type=\"button\" class=\"btn btn-success\" onclick=\"switchclass("+temp_sno+")\">Active</button>";

        var button2=document.createElement("div")
        button2.classList.add("button")
        button2.innerHTML="<button type=\"button\" class=\"btn btn-danger\" onclick=\"del("+temp_sno+")\">Delete</button>";

             

        if (localStorage.getItem("completed")!=null){
            if(check_completed.includes(parseInt(temp_sno))){
                box.classList.remove("bg-light")
                box.classList.add("text-white")
                box.classList.add("bg-success")
                button1.innerHTML= "<button type=\"button\" class=\"btn btn-success\" onclick=\"switchclass("+temp_sno+")\">Completed</button>";
            }
        }   

        box.setAttribute("id",temp_sno);
        body.appendChild(card_title);
        body.appendChild(desp);
        body.appendChild(button1);
        body.appendChild(button2);
        box.appendChild(header); 
        box.appendChild(body); 
        
        document.querySelector(".container").appendChild(box);
        
    }
}
function del(index){
    index=parseInt(index);
    if (localStorage.getItem("completed")!=null){
        if(check_completed.includes(index)){
            check_completed.splice(check_completed.indexOf(index),1);
            localStorage.setItem('completed',JSON.stringify(check_completed));
        }
    }
    for(var i=0;i<check_completed.length;i++){
        if (check_completed[i]>index){
                check_completed[i]--;
        }
    }
    localStorage.setItem('completed',JSON.stringify(check_completed));
    items.splice(index-1,1);
    localStorage.setItem('item',JSON.stringify(items));
    window.location.reload();
}
function switchclass(id){
    
    element=document.getElementById(id);
    element.classList.remove("bg-light")
    element.classList.add("text-white")
    element.classList.add("bg-success")
    text=element.querySelector(".btn");
    text.textContent="Completed";
    check_completed.push(parseInt(id));
    localStorage.setItem('completed',JSON.stringify(check_completed));
}

function clean(){
    localStorage.clear();
}
}
