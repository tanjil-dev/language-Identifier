document.getElementById('predictionForm').onsubmit = function(event) {
        event.preventDefault();

        const text = document.querySelector('textarea[name="text"]').value;
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Get CSRF token

        fetch('/predict-language/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken  // Add CSRF token to the headers
            },
            body: new URLSearchParams({ 'text': text })
        })
        .then(response => response.json())
.then(data => {
    if (data.language) {
        // Set the result text
        document.getElementById('result1').innerHTML = `Predicted Language: ${data.language}`;
        document.getElementById('result2').innerHTML = `Confidence: ${data.confidence}`;
        // Show the modal
        var myModal = new bootstrap.Modal(document.getElementById('resultModal'));
        myModal.show();
    } else {
        // Display error message
        document.getElementById('result').innerHTML = 'Error: ' + data.error;

        // Show the modal
        var myModal = new bootstrap.Modal(document.getElementById('resultModal'));
        myModal.show();
    }
});

    };

    // Sample text that will be shown when the button is clicked
    const sampleText = "پاکستان دنیا کا ایک خوبصورت ملک ہے";

    // Toggle sample text in the result div
    document.getElementById("sampleTextBtn").addEventListener("click", function() {
        document.getElementById("result").textContent = sampleText;
    });

    // Copy the result text to clipboard
document.getElementById("copyResultBtn").addEventListener("click", function() {
    const resultText = document.getElementById("result").textContent;

    // Using the modern Clipboard API to copy text
    navigator.clipboard.writeText(resultText).then(function() {
        // Alert the user that the result was copied
        alert("Result copied to clipboard!");
    }).catch(function(error) {
        // Handle any error in copying
        console.error("Could not copy text: ", error);
    });
});


    // JavaScript to handle the form submission and API call
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent default form submission

        // Get form data
        const fullName = document.getElementById('fullName').value;
        const email = document.getElementById('email').value;
        const comment = document.getElementById('comment').value;

        // API URL (adjust according to your API endpoint)
        const apiUrl = '/api/contact/';

        // Send POST request via fetch API
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                fullName: fullName,
                email: email,
                comment: comment,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('message').innerHTML = '<div class="alert alert-success">Your message has been sent successfully!</div>';
            } else {
                document.getElementById('message').innerHTML = '<div class="alert alert-danger">There was an error sending your message. Please try again later.</div>';
            }
        })
        .catch(error => {
            document.getElementById('message').innerHTML = '<div class="alert alert-danger">Error: ' + error.message + '</div>';
        });
    });




