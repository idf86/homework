# Created by Windy at 11/8/2023
Feature: User can open Target Circle
  # Enter feature description here

    Scenario: Verify user can access Target Circle page and see five benefits boxes
    Given Open target main page
    When Verify user can click on the Target Circle link
    Then Verify "1% earnings" header is present
    And Verify "Hundreds of deals" header is present
    And Verify "Birthday gift" header is present
    And Verify "Community support votes" header is present
    And Verify "Target Circle Partnerships" header is present