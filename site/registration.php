<?php
    $page = "Registration";
    require_once "header.php";
    session_start();
?>
<html>
    <form action= '../config/new_user.php' method= "post">
        <pre>First Name:       <input required type= "text" placeholder= "John" name= "first_name"></pre>
        <pre>Last name:        <input required type= "text" placeholder= "Doe" name= "last_name"></pre>
        <pre>Username:         <input required type= "text" placeholder= "J.D0e" name= "username"></pre>
        <pre>Email Address:    <input required type= "text" placeholder= "JDoe@gmail.com" name= "email"></pre>
        <pre>Password:         <input required type= "password" name= "passwd"></pre>
        <pre>Confirm password: <input required type= "password" name= "confirm_passwd"></pre>
        <input type= "submit" name= "submit" value= "Submit">
        <?php print_error_msg()?>
    </form>
</html>