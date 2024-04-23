# Define the JavaScript code as a string
javascript_code = """
document.querySelector('.confirm-button').addEventListener('click', function() {
    showSuccessMessage(); // Show success message
});

function showSuccessMessage() {
    var successMessage = document.getElementById('success-message');
    successMessage.style.display = 'block'; // Show the success message
}
"""

# Write the JavaScript code to a .js file
with open('script.js', 'w') as f:
    f.write(javascript_code)
