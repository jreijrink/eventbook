<?php

require_once('document.class.php');
//USE THE DATABASE CLASS FOR SQL HANDLING
require_once('database.class.php');

$query = $_GET["query"];

$query = checkSpelling($query);
$query = decomposeQuery($query);
$query = applySearchHistory($query);
$results = retrieveFromIndex($query);

//Create the results page


//------------------- FUNCTIONS ---------------

function checkSpelling($query) {
  return $query;
}

function decomposeQuery($query) {
  return $query;
}

function applySearchHistory($query) {
  return $query;
}

function retrieveFromIndex($query) {
  $results = array(); // Array of documents
  
  $cache = retrieveFromCache($query);
  if($cache != null) {
    return $cache;
  } else {
    return $results; 
  }
}

function retrieveFromCache($query) {
  return null;
}

?>

<h1>This is the request page</h1>