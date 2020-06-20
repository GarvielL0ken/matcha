<?php
	require_once 'setup.php';

	function get_results($table, $columns, $comparator)
	{
		$conn = connect_to_db();
		$stmt = $conn->prepare('SELECT ' . $columns . ' FROM ' . $table . ' WHERE ' . $comparator[0] . ' = :value');
		$stmt->execute(array('value' => $comparator[1]));
		$results = $stmt->fetchAll();
		if (!isset($results))
			return (NULL);
		if (!isset($results[0]))
			return (NULL);
		return ($results);
	}

	function get_results_extended($table, $columns, $condition, $values)
	{
		$conn = connect_to_db();
		$stmt = $conn->prepare('SELECT ' . $columns . ' FROM ' . $table . ' WHERE ' . $condition);
		$stmt->execute($values);
		$results = $stmt->fetchAll();
		if (!isset($results))
			return (NULL);
		if (!isset($results[0]))
			return (NULL);
		return ($results);
	}

	function insert_new_record($table, $data)
	{
		$conn = connect_to_db();
		$keys = array_keys($data);
		$fields = '';
		$values = '';
		foreach ($keys as $field)
		{
			$fields .= $field . ', ';
			$values .= ':' . $field . ', '; 
		}
		$fields = rtrim($fields, ', ');
		$values = rtrim($values, ', ');
		$sql = 'INSERT INTO ' . $table . ' (' . $fields . ') VALUES (' . $values . ')';
		$stmt = $conn->prepare($sql);
		$stmt->execute($data);
	}

	function is_in_db($table, $column, $value)
	{
		$results = get_results($table, $column, array($column, $value));
		if (!$results)
			return (0);
		return (1);
	}

	function remove_hash($field, $hash)
	{
		$results = get_results('hashes', '*', array($field, $hash));
		$num_hashes = 0;
		$id_user = $results[0]['id_user'];
		$results[0]['id_user'] = NULL;
		foreach ($results[0] as $db_hash)
		{
			if ($db_hash)
				$num_hashes++;
		}
		if ($num_hashes > 1)
			update_record('hashes', array($field => NULL), array('id_user', $id_user));
		else
			delete_record('hashes', array('id_user', $id_user));
	}
	
	function update_record($table, $data, $comparator)
	{
		if (!is_in_db($table, $comparator[0], $comparator[1]))
		{
			insert_new_record($table, $data);
			return (1);
		}
		$conn = connect_to_db();
		$keys = array_keys($data);
		$field_value_pairs = '';
		foreach ($keys as $field)
			$field_value_pairs .= $field . ' = :' . $field . ', ';
		$field_value_pairs = rtrim($field_value_pairs, ', ');

		$sql = 'UPDATE ' . $table . ' SET ' . $field_value_pairs;
		$sql .= ' WHERE ' . $comparator[0] . ' = :value';
		$data['value'] = $comparator[1];
		$stmt = $conn->prepare($sql);
		$stmt->execute($data);
	}

	function get_user_id($username)
	{
		$results = get_results('users', 'id_user', array('username', $username));
		if (!$results)
			return (NULL);
		return ($results[0]['id_user']);
	}

	function delete_record($table, $comparator)
	{
		$conn = connect_to_db();
		$sql = 'DELETE  FROM ' . $table . ' WHERE ' . $comparator[0] . '= :value';
		$data = array('value' => $comparator[1]);
		$stmt->execute($data);
	}
?>