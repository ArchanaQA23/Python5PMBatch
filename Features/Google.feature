
Feature: Check the gmail link
  Scenario: Checking the gmail link functionality

    Given User launches the url
    When User check the title
    And User click on Gmail link
    Then User should see the gmail page
    Then User should be connected
