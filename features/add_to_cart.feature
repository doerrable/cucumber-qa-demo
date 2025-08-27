Feature: Add items to shopping cart
  As a logged-in user
  I want to add and remove products from my shopping cart
  So that I can manage my purchases

  Background:
    Given I am logged in with username "standard_user" and password "secret_sauce"

  Scenario: Add a single item to the cart
    When I add the "Sauce Labs Backpack" to the cart
    Then the shopping cart badge should show "1"

  Scenario: Add multiple items to the cart
    When I add the "Sauce Labs Backpack" to the cart
    And I add the "Sauce Labs Bike Light" to the cart
    And I add the "Sauce Labs Onesie" to the cart
    Then the shopping cart badge should show "3"

  Scenario: Remove an item from the cart
    When I add the "Sauce Labs Bike Light" to the cart
    And I remove the "Sauce Labs Bike Light" from the cart
    Then the shopping cart badge should not be visible
