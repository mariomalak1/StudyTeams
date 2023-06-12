function get_value_create_request() {
    let search_bar = document.getElementById("topics_search");
    let val = search_bar.value;
    console.log("mario")
    console.log(val)
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "/topics?topic=" + val, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                return JSON.parse(xhr.responseText);
            } else {
                console.log(JSON.parse(xhr.responseText))
                return xhr.status;
            }
        }
    };
    xhr.send(JSON.stringify(val));
}