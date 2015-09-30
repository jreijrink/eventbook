<?php

//USE THE DATABASE CLASS FOR SQL HANDLING
require_once('database.class.php');

$suggestions = createSuggestions();

//Create the main search page along with the suggestions


//------------------- FUNCTIONS ---------------

function createSuggestions() {
  return null;
}

?>

<html lang="en">
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="css/index.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <title>Eventbook</title>
  </head>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-md-6 col-md-offset-3">
          <img class="center-block" src="img/logo.jpg" width="272" height="92" alt="Eventbook" id="fblogo" title="Eventbook">
          <form class="form-search" action="request.php" id="form" method="get">
            <div class="input-group stylish-input-group">
              <input type="text" class="form-control" placeholder="Search query" name="query" id="query" autofocus>
              <span class="input-group-addon">
                  <button type="submit">
                      <span class="glyphicon glyphicon-search"></span>
                  </button>  
              </span>
            </div>
          </form>
          <a href="miner.php">Or open the miner page..</a>
        </div>
      </div>
    </div>
  </body>
</html>