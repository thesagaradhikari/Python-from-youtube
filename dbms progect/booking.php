<?php
// Connect to the database
$servername = "localhost";
$username = "sagar";
$password = "sagar"; // Your MySQL password
$dbname = "hotel_management";


$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the date from the form submission
$selected_date = $_POST['selected_date'];

// Prepare and execute the SQL query
$sql = "SELECT guest_name, room_type, checkin_date, checkout_date FROM bookings WHERE checkin_date <= ? AND checkout_date >= ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $selected_date, $selected_date);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    // Output the details of each booking
    while ($row = $result->fetch_assoc()) {
        echo "Guest: " . $row['guest_name'] . " | Room Type: " . $row['room_type'] . " | Check-in: " . $row['checkin_date'] . " | Check-out: " . $row['checkout_date'] . "<br>";
    }
} else {
    echo "No bookings found for this date.";
}

$stmt->close();
$conn->close();
?>
