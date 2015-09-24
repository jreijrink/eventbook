<?php
class decomposition
{
	public function decompose($doc) {
		$doc = removeDuplicates($doc);

		$doc = removePunctuation($doc);
		
		$doc = removeRedundantWords($doc);
		
		$doc = stemming($doc);
		
		return $doc;
	}
  
	function removeDuplicates($doc) {
	  
		return $doc;
	}

	function removePunctuation($doc) {
	  
		return $doc;
	}

	function removeRedundantWords($doc) {
	  
		return $doc;
	}

	function stemming($doc) {
	  
		return $doc;
	}
}
?>