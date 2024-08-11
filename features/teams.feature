# Created by omar at 8/10/24
Feature: # Enter feature name here
  # Enter feature description here

  @e2e @team @women
  Scenario: All Women's Teams
    When I retrieve all "Women's" teams
    Then there should be no errors
    And the list should not be empty

  @e2e @team @men
  Scenario: All Men's Teams
    When I retrieve all "Men's" teams
    Then there should be no errors

  @e2e @team @men
  Scenario: Men's DI Teams by Conference ASUN
    When I retrieve "Men's" DI teams by conference "ASUN"
    Then there should be no errors
    And the list should contain teams
    And the list should contain 8 teams
    And the list should contain a team named "Stetson"

  @e2e @team @women @di
  Scenario: Women's DI Teams
    When I retrieve "Women's" DI teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams
    And the list should contain a team named "Austin Peay"

  @e2e @team @women @dii
  Scenario: Women's DII Teams
    When I retrieve "Women's" DII teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams
    And the list should contain a team named "Cal Poly Humboldt"
    And the list should not contain a team named "Austin Peay"

  @e2e @team @women @diii
  Scenario: Women's DIII Teams
    When I retrieve "Women's" DIII teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams


  @e2e @team @women @naia
  Scenario: Women's NAIA Teams
    When I retrieve "Women's" NAIA teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams


  @e2e @team @women @njcaa
  Scenario: Women's NJCAA Teams
    When I retrieve "Women's" NJCAA teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams


  @e2e @team @men @di
  Scenario: Men's DI Teams
    When I retrieve "Men's" DI teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams


  @e2e @team @men @dii
  Scenario: Men's DII Teams
    When I retrieve "Men's" DII teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams


  @e2e @team @men @diii
  Scenario: Men's DIII Teams
    When I retrieve "Men's" DIII teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams


  @e2e @team @men @naia
  Scenario: Men's NAIA Teams
    When I retrieve "Men's" NAIA teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams


  @e2e @team @men @njcaa
  Scenario: Men's NJCAA Teams
    When I retrieve "Men's" NJCAA teams
    Then there should be no errors
    And the list should not be empty
    And the list should contain teams


