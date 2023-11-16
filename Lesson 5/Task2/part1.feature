# Created by Windy at 11/16/2023
Feature: Product search and Color selection
  # Enter feature description here

    Scenario: Verify user can search for clothing and see the options
    Given Open target main page "https://www.target.com"
    When Verify user can search
    Then Verify product is loaded
    Then Verify user can see options