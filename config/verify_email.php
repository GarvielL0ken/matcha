<?php
	session_start();
	if ($_POST['submit'] == "Verify Email")
	{
		$results = get_results('hashes', '*', array('verification', $POST['hash']));
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
		$num_hashes = 0;
		$results[0]['id_user'] = NULL;
		foreach ($results[0] as $hash)
		{
			if ($hash)
				$num_hashes++;
		}
		if ($num_hashes > 1)
			update_record('hashes', array('verification' => NULL), array('id_user', $id_user));
		else
			delete_record('hashes', array('id_user', $id_user));
	}
	if ($_POST['submit'] == 'Send Link')
	{
		$email = $_POST['email'];
		$results = get_results('users', 'id_user', array('email', $email));
		if (!$results)
		{
			$page = '../site/verfiy_email.php?action=resend_link';
			$error_msg = 'No Account with that email address was found';
			$user_data = array('email' => $email);
			redirect_to_page($page, $error_msg, $user_data);
		}

	}
?>