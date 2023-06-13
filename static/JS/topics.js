function makeAjaxRequest(url, method) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            return xhr;
        }
    };
    xhr.send();
    return xhr;
}

function put_topics_in_select(){
    console.log("mariooo")
    let select_eleemnt = document.getElementById('room_topic');
    let xhr = makeAjaxRequest("/all_topics_json/", "GET");
    console.log(xhr);
    let json_response = JSON.parse(xhr.responseText)
    let Option = document.createElement('option');
    Option.text = 'Select your topic';
    Option.value = 0;
    select_eleemnt.add(Option);
    if(xhr.status === 200){
        for (const jsonResponseKey in json_response) {
            Option = document.createElement('option');
            Option.text = jsonResponseKey;
            Option.value = jsonResponseKey;
            select_eleemnt.add(Option);
        }
    }
}
