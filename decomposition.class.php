<?php
require_once('porterStemmer.class.php');

class decomposition
{	
	public function decompose($text) {
		echo "DECOMPOSITION <br/>";
		echo $text;
		echo "<br/>";
		
		// Remove capital letters
		$text = strtolower($text);
		
		// Replace contractions
		
		// Remove punctuation
		$text = preg_replace("/[^a-zA-Z 0-9]+/", " ", $text);
		
		//$doc = removeRedundantWords($doc);
		$redundantWords = array("the", "that", "to", "as", "there", "has", "and", "or", "is", "not", "a", "of", "but", "in", "by", "on", "are", "it", "if");
		foreach ($redundantWords as &$word) {
			$word = '/\b' . preg_quote($word, '/') . '\b/';
		}
		$text = preg_replace($redundantWords, '', $text);
		echo $text;
		echo "<br/>";
		
		// Stemming words
		$newtext = "";
		$words = explode(" ",$text);
		foreach ($words as $word) {
			$newtext .= porterStemmer::Stem($word);
			$newtext .= " ";
		}
		$text = $newtext;
		echo $text;
		echo "<br/>";
		
		// Remove duplicates
		$text = implode(' ',array_unique(explode(' ', $text)));
		echo $text;
		echo "<br/>";
		
		echo "END DECOMPOSITION <br/>";
		echo "<br/>";
		return $text;
	}
}
?>