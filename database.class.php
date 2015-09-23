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

    // Create connection
    $this->conn = new mysqli($servername, $username, $password);

    // Check connection
    if ($this->conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }
  }
  
  public function CloseConnection()
  {
    $this->conn->close();
  }
  
  //This is how you make a DB function, see miner for usage
  public function TestFunction()
  {
    /* Create table doesn't return a resultset */
    if ($this->conn->query("CREATE TEMPORARY TABLE myCity LIKE City") === TRUE) {
      printf("Table myCity successfully created.");
    } else {
      printf("First query failed.");
    }

    /* Select queries return a resultset */
    if ($result = $this->conn->query("SELECT Name FROM City LIMIT 10")) {
        printf("Select returned %d rows.", $result->num_rows);

        /* free result set */
        $result->close();
    } else {
      printf("Second query failed.");
    }
  }
}
?>