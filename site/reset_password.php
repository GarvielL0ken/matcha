<?php
    $page = "Reset Password";
    require_once "header.php";
?>
<html>
    <body>
        <form action= '../config/reset_password.php' method= 'post'>
            <?php
                if ($_GET['action'] == 'send_link')
                {
                    print('<pre>Enter your email address and a link will be sent to reset your password</pre>
                           <pre>Email: <input required type= "text" name= "email"></pre>
                           <input type= "submit" name= "submit" value= "Submit">');
                }
                else if ($_GET['action'] == 'reset_password')
                {
                    if (isset($_GET['hash']))
                    {
                        print('<pre>New password: <input required type= "password" name= "new_password"></pre>
                        <pre>Confirm password: <input required type= "password" name= "confirm_pasword"></pre>
                        <input type= "submit" name= "submit: value= "Submit">');
                    }
                    else
                    {
                        print('<pre>A hash is required to reset a password</pre>
                               <pre>If an email was sent to your account then it will contain a hash</pre>
                               <pre>If no email was recieved <a href= "./reset_password.php?action=send_link">click here</a> to resend the email</pre>');
                    }
                }
            ?>
        </form>
    </body>
</html>