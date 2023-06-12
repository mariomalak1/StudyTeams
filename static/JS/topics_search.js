const form = document.getElementById("myForm");

// Add an event listener for the form submit event

form.addEventListener("submit",
    function get_value_create_request(event) {
        let search_bar = document.getElementById("topics_search");
        let val = search_bar.value;
        let link = "/topics?topic=" + val
        location.replace(link);
        event.preventDefault();
    }
)

form.addEventListener("submit", function(event) {
  // Prevent the form from being submitted
  event.preventDefault();

  // Perform any additional actions or validation here
});

    //     let xhr = new XMLHttpRequest();
    //
    // xhr.open("GET", , true);
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // xhr.onreadystatechange = function () {
    //     if (xhr.readyState === 4) {
    //         console.log(xhr.status);
    //     }
    // };
    // xhr.send(JSON.stringify(val));