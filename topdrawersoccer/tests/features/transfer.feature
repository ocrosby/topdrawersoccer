# Created by omar at 8/7/24
Feature: Transfer
  As a user
  I want to see the transfer information
  So that I can know the latest transfer news

  Scenario: Colleges
    When I retrieve the list of transfer colleges
    Then there should be no errors
    And the list should not be empty

  Scenario: Outgoing Colleges
    When I retrieve a list of outgoing transfer colleges
    Then there should be no errors
    And the list should not be empty

  Scenario: Incoming Colleges
    When I retrieve a list of incoming transfer colleges
    Then there should be no errors
    And the list should not be empty

  Scenario: Players
    When I retrieve the list of transfer players
    Then there should be no errors
    And the list should not be empty

    