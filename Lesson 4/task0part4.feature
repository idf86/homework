# Created by Windy at 11/7/2023
Feature: SignIn tests
  # Enter feature description here
  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee
    And Verify coffee in search result url


  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea
    And Verify tea in search result url


  Scenario: User can search for christmas lights
    Given Open target main page
    When Search for christmas lights
    Then Verify search worked for christmas lights
    And Verify christmas+lights in search result url


  Scenario: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search worked for <expected_product>
    And Verify <expected_url> in search result url
    Examples:
    |product          |expected_product     |expected_url     |
    |coffee           |coffee               |coffee           |
    |tea              |tea                  |tea              |
    |mug              |mug                  |mug              |
    |christmas lights |christmas lights     |christmas+lights |
