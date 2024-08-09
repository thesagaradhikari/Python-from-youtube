<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$servername = "localhost";
$username = "sagar";
$password = "sagar"; // Your MySQL password
$dbname = "hotel_management";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if POST data is set
if(isset($_POST['guest_name'], $_POST['room_type'], $_POST['checkin_date'], $_POST['checkout_date'])) {
    $guest_name = $_POST['guest_name'];
    $room_type = $_POST['room_type'];
    $checkin_date = $_POST['checkin_date'];
    $checkout_date = $_POST['checkout_date'];

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO bookings (guest_name, room_type, checkin_date, checkout_date) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $guest_name, $room_type, $checkin_date, $checkout_date);

    // Execute the statement
    if ($stmt->execute()) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
} else {
    echo "All fields are required.";
}

// Close the connection
$conn->close();
?>
