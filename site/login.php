<?php
    $page = "Login";
    require_once "header.php";
?>
<html>
    <body>
        <form action= '../config/login.php' method= 'post'>
            <pre>Username: <input required type= 'text' name= 'username'></pre>
            <pre>Password: <input required type= 'password' name= 'passwd'></pre>
            <input type= 'submit' name= 'submit' value= 'Submit'>
        </form>
        <pre>Don't have an account? <a href= 'registration.php?act'>Create one</a></pre>
    </body>
</html>