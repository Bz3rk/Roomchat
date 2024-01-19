document.addEventListener('DOMContentLoaded', function() {
    // Check if the form was submitted on a previous page load
    if (sessionStorage.getItem('formSubmitted')) {
        document.body.style.opacity = 1;  // Remove opacity
        document.body.style.animation = 'none';  // Disable the animation
        sessionStorage.removeItem('formSubmitted');  // Clear the flag
    }

    document.getElementById('myForm').addEventListener('submit', function() {
        // Set a flag in sessionStorage to indicate that the form was submitted
        sessionStorage.setItem('formSubmitted', 'true');
    });
});
