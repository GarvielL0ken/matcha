<?php
    function redirect_to_page($page)
    {
        header('Location: ' . $page);
    }

    function output_a($href, $string)
    {
        $html = '<a href= "' . $href . '">' . $string . '</a>';
        return ($html);
    }
?>