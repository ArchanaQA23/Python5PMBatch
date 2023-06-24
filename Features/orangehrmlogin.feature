
Feature: Check the login functionality for orange HRM Page
Background:
  Given User launches the url of orange hrm page

  Scenario: Login with valid credential

    When User enter the username "Admin" and password "admin123"
    And User clicks on login button
    Then user should successfully login  to the dashboard page
    Then User should be happy and delighted



  Scenario Outline:  Login functionality check with different creedentials

    When User enter the username "<username>" and password "<password>"
    And User clicks on login button
    Then user should successfully login  to the dashboard page
    Examples:
      | username | password |
      |admin12   |  898999  |
      |admin45   |  978999  |
      |Admin     | admin123 |


