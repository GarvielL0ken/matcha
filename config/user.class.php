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

        function calculate_fame_rating()
        {
            if ($this->$nuw_users_viewed_by == 0)
                $like_to_view_ratio = 1;
            else 
                $like_to_view_ratio = $this->num_users_liked_by / $this->num_users_viewed_by;
            $view_to_users_ratio = $this->num_users_viewed_by / get_num_users();
            $fame_rating = ($like_to_view_ratio + $view_to_users_ratio) * 100;
            $this->fame_rating = $fame_rating;
            return ($this->fame_rating);
        }
    }
?>