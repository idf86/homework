# Created by Windy at 11/6/2023
Feature: Searching and clicking
  # Enter feature description here

  Scenario: User can open the target website and verify cart
    Given Open target main page "https://www.target.com"
    When Click on cart
    Then Verify "Cart is empty" message
    When Click Sign In link
    Then Verify user can see Sign In header