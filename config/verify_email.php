<?php
	session_start();
	if ($_POST['submit'] == "Verify Email")
	{
		$results = get_results('hashes', '*', array('verification', $_POST['hash']));
		if (!$results)
		{
			$page = '../site/verify_email.php?action="display_message"';
			$resend_link = '<a href= "./verify_email.php?action=resend_link">here</a>';
			$verify_link = '<a href= "./verify_email.php?action=verify_email">here</a>';
			$error_msg = 'Verification failed. Request another verifition email ' . $resend_link . 
							'<br> or copy and paste the hash into the textbox provided ' . $verify_link . 
							'<br>The hash can be found in the most recent verification email';
			redirect_to_page($page, $error_msg);
		}
		$id_user = $results[0]['id_user'];
		update_record('users', array('verified' => true), array('id_user', $id_user));
		remove_hash('verification', $_POST['hash']);
	}
	if ($_POST['submit'] == 'Send Link')
	{
		$email = $_POST['email'];
		$results = get_results('users', 'id_user, username', array('email', $email));
		if (!$results)
		{
			$page = '../site/verfiy_email.php?action=resend_link';
			$error_msg = 'No Account with that email address was found';
			$user_data = array('email' => $email);
			redirect_to_page($page, $error_msg, $user_data);
		}
		$id_user = $results[0]['id_user'];
		$username = $results[0]['username'];
		$hash = generate_hash();
		send_verification_email($username, $email, $hash);
		$data = array('id_user' => $id_user, 'verification' => $hash);
		update_record('hashes', $data, array('id_user', $id_user));
		$error_msg = 'Another email has been sent<br>If no email was recieved click <a href= "./verify_email?action=resend_link">here</a>';
		redirect_to_page('../site/verify_email?action=verify_email', $error_msg, array('email' => $email));
	}
?>