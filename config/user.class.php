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
		public	$likes;

		function __construct($username)
		{
			$arr_keys = array('id_user', 'first_name', 'last_name', 'username', 'email', 'gender',
								'profile_pictures', 'bio', 'info_completed');

			$results = get_results('users', '*', array('username', $username));
			if (isset($results[0]['gender']))
				$results[0]['gender'] = get_results('genders', 'name', array('id_gender', $results[0]['gender']));
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

			$results = get_results_extended('likes', '*', 'id_user_1 = :id_user OR id_user_2 = :id_user', array('id_user' => $this->id_user));
			$this->likes = array();
			foreach ($results as $result)
			{
				if ($result['id_user_1'] == $this->id_user)
				{
					$id_user = $result['id_user_2'];
					$this_like = $result['like_user_1'];
					$user_like = $result['like_user_2'];
				}
				else
				{
					$id_user = $result['id_user_1'];
					$this_like = $result['like_user_2'];
					$user_like = $result['like_user_1'];
				}
				$like = array('id_user' => $id_user, 'this_like' => $this->like, 'user_like' => $user_like);
			}
		}

		function to_string($mode, $user= NULL)
		{
			$html = '';
			if ($mode == 'display' || $mode == 'view')
			{
				$html .= '<pre><h1>' . $this->username . ' : ' . $this->fame_rating . 'smegols</h1></pre>';
				$html .= '<pre><h2>' . $this->first_name . ' ' . $this->last_name . '</h2></pre>';
				$html .= '<pre><h3>' . $this->gender . '</h3></pre>';
				$html .= '<pre><h3>' . $this->age . '</h3></pre>';
				$html .= '<pre>' . $this->bio . '</pre>';
				$html .= '<pre>' . $this->email . '</pre>';
				if ($mode == 'view')
				{
					foreach ($this->likes as $like)
					{
						if ($like['id_user'] == $user->id_user)
						{
							if ($like['user_like'])
							{
								$image = 'like';
								$alt = 'unlike';
							}
							else
							{
								$image = 'unlike';
								$alt = 'like';
							}
						}
					}
					$html .= '<div id= "like" onclick= "change_like_status()">
									<img src= "../resources/' . $image . '.png" alt= "' . $alt .  '" width= "50" height= "50">
								</div>';
					$html .= '<form action= "../config/beef.php" method= "GET">';
					$html .= output_input(0, 'submit', 'block', 'Block');
					$html .= '</form>';
				}
			}
			elseif ($mode == 'edit')
			{
				$html .= '<pre>  Username :' . output_input(1, 'text', 'username', $this->username) . '</pre>';
				$html .= '<pre>First Name :' . output_input(1, 'text', 'first_name', $this->first_name) . '</pre>';
				$html .= '<pre> Last Name :' . output_input(1, 'text', 'last_name', $this->last_name) . '</pre>';
				$html .= '<pre>    Gender :' . output_input(1, 'text', 'gender', $this->gender) . '</pre>';
				$html .= '<pre>       Age :' . output_input(1, 'text', 'gender', $this->age) . '</pre>';
				$html .= '<pre>       Bio :' . output_input(1, 'textarea', 'bio', $this->bio) . '</pre>';
				$html .= '<pre>Email Address: ' . output_input(1, 'email', 'email', $this->email) . '</pre>';
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