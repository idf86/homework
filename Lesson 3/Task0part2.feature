# Created by Windy at 11/5/2023
Feature: Search tests
  # Enter feature description here

  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search worked
    Then Verify search result url