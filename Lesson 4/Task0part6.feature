# Created by Windy at 11/8/2023
Feature: Main page UI tests
  # Enter feature description here

  Scenario: Header has correct amount of links
    Given Open target main page
    Then Verify header is present
    And Verify header has 5 links