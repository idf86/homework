# Created by Windy at 11/7/2023
Feature: SignIn tests
  # Enter feature description here

  Scenario: User can open SignIn page
    Given Open target main page
    When Click Sign In
    And From right side navigation menu, click SignIn
    Then Verify Sign In form opened