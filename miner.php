<?php

require_once('document.class.php');
//USE THE DATABASE CLASS FOR SQL HANDLING
require_once('database.class.php');

findDocuments();

//------------------- FUNCTIONS ---------------

function findDocuments() {
  //Find documents and metadata from various sources
  
  //for loop through each source
    // for each document found in the source:
      $doc = new document;
      //How to save document found in the current source
      $doc->add_metadata("artist", "who");
      $doc->description = "bla bla ...";
      
      $doc = decomposeDocument($doc);
      $doc = multiLabelClassification($doc);
      $doc = clusterDocument($doc);
      $doc = findDuplicate($doc);
      saveToIndex($doc);
}

function decomposeDocument($doc) {
  return $doc;
}

function multiLabelClassification($doc) {
  //When tag is found:
  $doc->add_tag("found tag");
  
  return $doc;
}

function clusterDocument($doc) {  
  return $doc;
}

function findDuplicate($doc) {  
  return $doc;
}

function saveToIndex($doc) {
  $db = new database;
  $db->TestFunction();
}

?>

<h1>This is the miner page</h1>