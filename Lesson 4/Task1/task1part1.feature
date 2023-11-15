# Created by Windy at 11/8/2023
Feature: Target Circle and Cart
  # Enter feature description here

    Scenario: Verify user can access Target Circle page and add a product to the cart
    Given Open target main page "https://www.target.com"
    When Verify user can click on the Target Circle link
    Then Verify Earnings box
    Then Verify Deals box
    Then Verify Birthday box
    Then Verify Community box
    Then Verify Partnerships box
    Then Verify all boxes are present
    Then Verify user can search
    Then Verify product can be added to cart
    Then Verify user can checkout
    Then Verify user can see price of product