# Created by Windy at 11/28/2023
Feature: Verify that a user can open Terms and Conditions from sign in page
  # Enter feature description here

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page "https://www.target.com/account"
    When Store original windows
    Then Click on Target terms and conditions
    Then Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    Then User can close new window and switch back to original