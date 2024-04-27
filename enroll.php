<?php
// Database connection
$conn = mysqli_connect("localhost", "username", "password", "database_name");

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Form submission handling
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize form inputs to prevent SQL injection
    $productName = mysqli_real_escape_string($conn, $_POST['productName']);
    $price = $_POST['price'];
    $manufactureDate = $_POST['mfg'];
    $expiryDate = $_POST['exp'];
    $limitingQuantity = $_POST['limitingQuantity'];
    $quantity = $_POST['quantity'];

    // Insert data into the database
    $sql = "INSERT INTO stocks (productName, price, manufactureDate, expiryDate, limitingQuantity, quantity)
            VALUES ('$productName', '$price', '$manufactureDate', '$expiryDate', '$limitingQuantity', '$quantity')";

    if (mysqli_query($conn, $sql)) {
        echo "Stock enrolled successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }
}

// Close database connection
mysqli_close($conn);
?>
