<?php
    function insert_new_record($table, $data)
    {
        $conn = connect_to_db();
        $keys = array_keys($data);
        print_r($keys);
        $stmt = $conn->prepare('INSERT INTO ' . $table . ' (' . $fields . ') VALUES (' . $values . ')');
        $stmt->execute($data);
    }

    function is_in_db($table, $column, $value)
    {
        $conn = connect_to_db();
        $stmt = $conn->prepare('SELECT ' . $column . ' FROM ' . $table . ' WHERE ' . $column . ' = :value');
        $stmt->execute(array('value' => $value));
        $results = $stmt->fetchAll();
        if (!$results)
            return (0);
        return (1);
    }
?>