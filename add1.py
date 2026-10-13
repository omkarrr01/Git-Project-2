<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

```
<header>
    <h1>Student Registration Portal</h1>
    <p>Welcome! Register here to get started.</p>
</header>

<nav>
    <a href="#home">Home</a>
    <a href="#register">Register</a>
    <a href="#about">About Us</a>
</nav>

<main>
    <section id="home" class="welcome">
        <h2>Welcome to Our Portal</h2>
        <p>A simple platform for student registration.</p>
    </section>

    <section id="register" class="form-container">
        <h2>Student Registration Form</h2>

        <form>
            <label for="name">Full Name:</label>
            <input type="text" id="name" placeholder="Enter your name" required>

            <label for="email">Email Address:</label>
            <input type="email" id="email" placeholder="Enter your email" required>

            <label for="course">Select Course:</label>
            <select id="course" required>
                <option value="">Choose a course</option>
                <option value="BBA">BBA</option>
                <option value="BCA">BCA</option>
                <option value="MCA">MCA</option>
                <option value="MBA">MBA</option>
            </select>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" placeholder="Enter phone number">

            <button type="submit">Register Now</button>
        </form>
    </section>

    <section id="about" class="about">
        <h2>About Us</h2>
        <p>Our portal provides a simple and user-friendly
        interface for student registration.</p>
    </section>
</main>

<footer>
    <p>&copy; 2026 Student Registration Portal. All rights reserved.</p>
</footer>
```

</body>
</html>

