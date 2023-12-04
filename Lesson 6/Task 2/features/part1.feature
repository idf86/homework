# Created by Windy at 12/4/2023
Feature: Target Cart Test
  # Enter feature description here

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open "https://www.target.com"
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown