# Created by Windy at 12/5/2023
Feature: Cart update
  # Enter feature description here

  Scenario: Verify user can add a product to the cart
    Given Open target main page "https://www.target.com"
    When Verify user can search
    Then Verify product can be added to cart
    Then Verify user can checkout
    Then Verify user can see the product in the cart