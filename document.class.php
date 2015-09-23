<?php
class document
{
  public $description;
  public $metadata; // key-value dictionary
  public $tags = array();
  
  function add_metadata($name, $value) {
    $this->metadata[$name] = $value;
  }
  
  function add_tag($value) {
    array_push($this->tags, $value);
  }
}
?>