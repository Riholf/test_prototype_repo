function postRequest()
{

    var text = document.getElementById("input_text").value
    console.log(text)
    var summaryLength = document.getElementById("input_summary").value

    const url = "http://localhost:8000/summarization/";
    const Text = {
        text: text
    };
    const SummaryLength = summaryLength

    const otherParameters = {
        headers: {
            "content-type": "application/json; charset=UTF-8"
        },
        body: JSON.stringify(Text),
        method: "POST"
    };

    fetch(url + "?summary_length=" + SummaryLength, otherParameters)
    .then(response => response.json())
    .then(response => {console.log(response);
        return response;
    })
    .then(response => {document.getElementById("response").innerHTML = response;
});
}