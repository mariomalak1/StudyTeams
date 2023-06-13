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