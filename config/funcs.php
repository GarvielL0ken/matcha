<?php
    function redirect_to_page($page)
    {
        header('Location: ' . $page);
    }

    function output_a($href, $string, $type= null)
    {
        $html = '<a href= "' . $href . '">';
        if (!$type)
            $html .= $string;
        if ($type == 'img')
            $html .=  '<img src= "../resources/' . $string . '.png" alt= "' . $string . '" width= "50" height= "50">';
        $html .= '</a>';
        return ($html);
    }
?>