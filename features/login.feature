Feature: Login functionality
  As a user of SauceDemo
  I want to log in with valid and invalid credentials
  So that I can access the system securely

  Background:
    Given I am on the login page

  Scenario: Successful login with valid credentials
    When I log in with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the inventory page

  Scenario: Unsuccessful login with invalid credentials
    When I log in with username "bad_user" and password "bad_pass"
    Then I should see an error message

  Scenario: Login with empty credentials
    When I log in with username "" and password ""
    Then I should see an error message
