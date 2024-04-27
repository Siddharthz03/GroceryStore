<?php
// Start session to store user data
session_start();

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if both username and password are provided
    if (!empty($_POST['username']) && !empty($_POST['password'])) {
        // Retrieve username and password from the form
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Check if username and password are correct (you would validate against a database here)
        // For demonstration, let's assume valid username/password is "admin"/"12345"
        if ($username === "admin" && $password === "12345") {
            // Set session variables to remember user login status
            $_SESSION['username'] = $username;

            // Redirect to the dashboard or any other page upon successful login
            header("Location: ./interface.html");
            exit();
        } else {
            // If username/password is incorrect, display an error message
            echo "<script>alert('Invalid username or password');</script>";
        }
    } else {
        // If both username and password are not provided, display an error message
        echo "<script>alert('Please provide both username and password');</script>";
    }
}
?>
