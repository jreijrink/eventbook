<?php
class classifier
{
  public function classify($doc)
  {
    //When tag is found:
    $doc->add_tag("found tag");
    $doc->add_tag("another tag");
    
    return $doc;
  }
}
?>