<?php
class document
{  
  public $name;
  public $urls = array();
  
  public $genre = array();
  public $artists = array();
  public $location;
  public $date;
  
  public $description;
  public $tags = array();
    
  function add_url($value) {
    array_push($this->urls, $value);
  }
  
  function add_genre($value) {
    array_push($this->artists, $value);
  }
  
  function add_artist($value) {
    array_push($this->artists, $value);
  }
  function add_tag($value) {
    array_push($this->tags, $value);
  }
}
?>