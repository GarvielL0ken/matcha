<?php
    function insert_new_record($table, $data)
    {
        $conn = connect_to_db();
        $keys = array_keys($data);
        print_r($keys);
        $stmt = $conn->prepare('INSERT INTO ' . $table . ' (' . $fields . ') VALUES (' . $values . ')');
        $stmt->execute($data);
    }

    function get_num_users()
    {
        $conn = connect_to_db();
        $stmt = $conn->prepare('SELECT COUNT(`id_user`) FROM users');
        $stmt->execute();
        $results = $stmt->fetchAll();
        return($results[0]['id_user'])
    }

    function get_results($table, $columns, $comparator, $value)
    {
        $conn = connect_to_db();
        $stmt = $conn->prepare('SELECT ' . $columns . ' FROM ' . $table . ' WHERE ' . $comparator . ' = :value');
        $stmt->execute(array('value' => $value));
        $results = $stmt->fetchAll();
        return ($results);
    }

    function is_in_db($table, $column, $value)
    {
        $results = get_results($table, $column, $column, $value);
        if (!$results)
            return (0);
        return (1);
    }

    function update_record($table, $arr_data, $comparator, $value)
    {
        $conn = connect_to_db();
        $sql = 'UPDATE ' . $table . ' SET ';
        foreach (array_keys($data) in $key)
            $sql .= $key . ' = :' . $arr_data[$key] . ', ';
        $sql = substr($sql, 0, -2);
        $sql .= ' WHERE ' . $comparator ' = :' $value;
        $stmt = $conn->prepare($sql);
        $stmt->execute($arr_data);
    }
?>