<?php
    class User 
    {
        public $first_name;
        public $last_name;
        public $username;
        public $gender;
        public $sexual_preferences;
        public $bio;
        public $tags;
        public $profile_pictures;
        public $age;
        public $fame_rating;
        public $online_status;
        public $users_viewed;
        public $users_liked;
        public $email;

        function __construct($data)
        {
            $arr_keys = array('first_name', 'last_name', 'username', 'gender', 
                              'sexual_preferences', 'bio', 'tags', 'profile_pictures', 'age', 
                              'fame_rating', 'online_status', 'users_viewed', 'users_liked', 'email');
            
            foreach ($arr_keys as $key)
            {
                if (isset($data[$key]))
                    $this->{$key} = $data[$key];
                else
                    $this->{$key} = null;
            }
        }
    }
?>