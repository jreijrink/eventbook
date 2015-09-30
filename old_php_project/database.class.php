<?php
class database
{
	private $conn;
  
  public function __construct()
  {
    $this->Connect();
  }
  
  private function Connect()
  {
    $servername = "localhost";
    $username = "root";
    $password = "";
    $database = "test";

    // Create connection
    $this->conn = new mysqli($servername, $username, $password);

    // Check connection
    if ($this->conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }
	
	$this->conn->select_db($database);
  }
  
  public function CloseConnection()
  {
    $this->conn->close();
  }
  
  //This is how you make a DB function, see miner for usage
  public function TestFunction()
  {
    /* Create table doesn't return a resultset */
    if ($this->conn->query("INSERT INTO `document`(`name`, `url`) VALUES ('first', 'http://google.com/first')") === TRUE) {
      printf("Document successfully created.");
    } else {
      printf("Document query failed.");
    }

    /* Select queries return a resultset */
    if ($result = $this->conn->query("SELECT * FROM `document`")) {
        printf("Select returned %d rows.", $result->num_rows);

        /* free result set */
        $result->close();
    } else {
      printf("Second query failed.");
    }
  }
}
?>