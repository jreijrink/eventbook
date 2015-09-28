<?php

require_once('document.class.php');
//USE THE DATABASE CLASS FOR SQL HANDLING
require_once('database.class.php');
require_once('classifier.class.php');
require_once('decomposition.class.php');

findDocuments();

//------------------- FUNCTIONS ---------------

function findDocuments() {
  //Find documents and metadata from various sources
  
  //for loop through each source
    // for each document found in the source:
      $doc = new document;
      //How to save document found in the current source
      $doc->add_url("http://eventful.com/event/1");
      $doc->name = "dancefestival";
      $doc->add_artist("who");
      $doc->description = "bla bla ...";
            
      $doc = decomposeDocument($doc);
      $doc = multiLabelClassification($doc);
            
      foreach ($doc->tags as $tag) {
          echo "$tag <br>";
      }
      
      $doc = clusterDocument($doc);
      $doc = findDuplicate($doc);
      saveToIndex($doc);
}

function decomposeDocument($doc) {
  $decomposition = new decomposition;
  $doc = $decomposition->decompose($doc);
  
  return $doc;
}

function multiLabelClassification($doc) {
  $classifier = new classifier;
  $doc = $classifier->classify($doc);
  
  echo "TEST";
  
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