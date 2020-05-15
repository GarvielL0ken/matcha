<?php
	require_once 'database.php';
	require_once 'setup.php';
	require_once 'db_funcs.php';

	class User 
	{
		public	$id_user;
		public	$first_name;
		public	$last_name;
		public	$username;
		public	$email;
		public	$gender;
		public	$profile_pictures;
		public	$bio;
		public	$info_conpleted;

		function __construct($username)
		{
			`gender`			INT				DEFAULT NULL,
			`profile_picture`	VARCHAR(100)	DEFAULT NULL,
			`bio`				VARCHAR(256)	DEFAULT NULL,
			`last_online`		VARCHAR(128)		DEFAULT NULL,
			`passwd`			VARCHAR(128)	NOT NULL,
			`verified`			BOOLEAN			NOT NULL		DEFAULT FALSE,
			`info_completed`	BOOLEAN			NOT NULL		DEFAULT FALSE);

			$arr_keys = array('id_user', 'first_name', 'last_name', 'username', 'email', 'gender'
								'profile_pictures', 'bio', 'info_completed');

			$results = get_results('users', '*', array('username' => $username));
			if (isset($results[0]['gender']))
				$results[0]['gender'] = get_results('genders', 'name', array('id_gender' => $results[0]['gender']));
			else
				$results[0]['gender'] = NULL;
			if (isset($results[0]['profile_picture']))
				$results[0]['profile_pictures'][0] = $results[0]['profile_picture'];
			else
				$results[0]['profile_pictures'] = NULL;
			
			foreach ($arr_keys as $key)
			{
				if (isset($results[0][$key]))
					$this->{$key} = $results[0][$key];
			}
		}

		function to_string($mode)
		{
			$html = '';
			if ($mode == 'display')
			{
				$html .= '<pre><h1>' . $this->username . '</h1></pre>';
				$html .= '<pre><h2>' . $this->first_name . ' ' . $this->last_name . '</h2></pre>';
				$html .= '<pre><h3>' . $this->gender . '</h3></pre>';
				$html .= '<pre><h3>' . $this->age . '</h3></pre>';
				$html .= '<pre>' . $this->bio . '</pre>';
				$html .= '<pre>' . $this->email . '</pre>';
			}
			elseif ($mode == 'edit')
			{
				$html .= '<pre>  Username :' . output_input(1, 'text', 'username', $this->username) . '</pre>';
				$html .= '<pre>First Name :' . output_input(1, 'text', 'first_name', $this->first_name) . '</pre>';
				$html .= '<pre> Last Name :' . output_input(1, 'text', 'last_name', $this->last_name) . '</pre>';
				$html .= '<pre>Email Address: ' . output_input(1, 'text', 'email', $this->email) . '</pre>';
			}
		}

		function update_online_status($mode)
		{
			if ($mode)
				$value = "Last seen: " . date("d/m/Y") . " at " . date("H:i");
			else
				$value = "Online";
			update_record('users', array('last_online' => $value), array('id_user' => $this->id_user));
		}
	}
?>