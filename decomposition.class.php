<?php
require_once('porterStemmer.class.php');

class decomposition
{	
	public function decompose($doc) {
		echo "DECOMPOSE <br/>";
		echo $doc->description;
		echo "<br/>";
		
		// Remove capital letters
		$doc->description = strtolower($doc->description);
		
		// Remove punctuation
		$doc->description = preg_replace("/[^a-zA-Z 0-9]+/", " ", $doc->description);
		
		// Stemming words
		$newstring = "";
		$words = explode(" ",$doc->description);
		foreach ($words as $word) {
			$newstring .= porterStemmer::Stem($word);
			$newstring .= " ";
		}
		$doc->description = $newstring;
		echo $doc->description;
		echo "<br/>";
		
		// Remove duplicates
		$doc->description = implode(' ',array_unique(explode(' ', $doc->description)));
		echo $doc->description;
		echo "<br/>";
		
		//$doc = removeRedundantWords($doc);
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