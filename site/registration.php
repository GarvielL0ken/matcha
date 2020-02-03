<?php
    $page = "Registration";
    require_once "header.php";
    session_start();
?>
<html>
    <form action= '../config/new_user.php' method= "post">
        <?php
            print(output_field('First Name:       ', 'text'       , 'first_name'  , 'John'));
            print(output_field('Last Name:        ', 'text'       , 'last_name'   , 'Doe'));
            print(output_field('Username:         ', 'text'       , 'username'    , 'J.D0e$'));
            print(output_field('Email Address:    ', 'text'       , 'email'       , 'jdoey@doemail.com'));
            print(output_field('Password:         ', 'password'   , 'passwd'));
            print(output_field('Confirm Password: ', 'password'   , 'confirm_passwd'));
        ?>
        <input type= 'submit' name= 'submit' value= 'Submit'>
        <?php print_error_msg()?>
    </form>
</html>