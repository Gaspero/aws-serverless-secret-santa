Feature: Adding user to database
  In order to join the Secret Santa game,
  I want to create a new user with my creds.
   
  Scenario: New user successfully created
    Given POST request is sent to the service
      And the name is TestUser
      And the email is test-user@email.com
     When request is executed
     Then response id is provided
      And response name is TestUser
      And response email is test-user@email.com
      And response code is 200
        
  Scenario: Wrong API method is called
    Given GET request is sent to the service
      And the name is TestUser
      And the email is test-user@email.com
     When request is executed
     Then response code is 400