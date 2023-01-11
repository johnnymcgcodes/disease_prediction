function showVal(newVal, name){
    if (newVal == 1){
        newVal = "Yes"
    } else{
        newVal = "No"
    }
    let id_name = name + "Val"
    document.getElementById(id_name).innerHTML=newVal;

}

function showCheckVal(checkbox, name){
    checkbox = document.getElementById(checkbox)
    console.log("Here")
    let newVal;
    if (checkbox.checked == 1){
        newVal = "Yes"
        checkbox.value = 1
        document.getElementById(name+"ID").value = 1
    } else{
        newVal = "No"
    }
    let id_name = name + "Val"
    document.getElementById(id_name).innerHTML=newVal;

}
function showRangeVal(newVal, name){
    let id_name = name + "Val"
    document.getElementById(id_name).innerHTML=newVal;

}
function showAlteredRangeVal(newVal, name){
    let adjusted_val = 18 + (newVal-1)*10
    let topRange = adjusted_val + 9
    let id_name = name + "Val"
    document.getElementById(id_name).innerHTML=adjusted_val +" to "+topRange;

}

function showCheckedVal(checkbox, name){
    checkbox = document.getElementById(checkbox)
    let newVal;
    if (checkbox.checked == 1){
        newVal = "Yes"
    } else{
        newVal = "No"
    }
    let id_name = name + "Val"
    document.getElementById(id_name).innerHTML=newVal;

}