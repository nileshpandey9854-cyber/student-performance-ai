
// Get the form
const form = document.querySelector("form");

// Get all input fields
const inputs = document.querySelectorAll("input");

// Form submit validation
form.addEventListener("submit", function (event) {

    let valid = true;

    inputs.forEach(function (input) {

        const value = Number(input.value);

        // Check empty values
        if (input.value === "") {
            valid = false;
            input.style.borderColor = "red";
        }

        // Check negative values
        else if (value < 0) {
            valid = false;
            input.style.borderColor = "red";
        }

        else {
            input.style.borderColor = "";
        }
    });


    // Stop form submission if invalid
    if (!valid) {
        event.preventDefault();

        alert("Please enter valid values in all fields.");
    }
});


// Remove red border when user starts typing
inputs.forEach(function (input) {

    input.addEventListener("input", function () {
        input.style.borderColor = "";
    });

});


// Reset form
form.addEventListener("reset", function () {

    inputs.forEach(function (input) {
        input.style.borderColor = "";
    });

});

