# Created by omar at 8/7/24
Feature: Conference
  As a user
  I want to see the conference information
  So that I can be informed about the structure of college soccer

  @e2e @conference @di @men
  Scenario: DI Men's Conferences
    When I retrieve the list of DI Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 24 conferences

  @e2e @conference @dii @men
  Scenario: DII Men's Conferences
    When I retrieve the list of DII Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 22 conferences

  @e2e @conference @diii @men
  Scenario: DIII Men's Conferences
    When I retrieve the list of DIII Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 48 conferences

  @e2e @conference @naia @men
  Scenario: NAIA Men's Conferences
    When I retrieve the list of NAIA Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 28 conferences

  @e2e @conference @njcaa @men
  Scenario: NJCAA Men's Conferences
    When I retrieve the list of NJCAA Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 57 conferences

  @e2e @conference @di @women
  Scenario: DI Women's Conferences
    When I retrieve the list of DI Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 30 conferences

  @e2e @conference @dii @women
  Scenario: DII Women's Conferences
    When I retrieve the list of DII Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 23 conferences

  @e2e @conference @diii @women
  Scenario: DIII Women's Conferences
    When I retrieve the list of DIII Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 49 conferences

  @e2e @conference @naia @women
  Scenario: NAIA Women's Conferences
    When I retrieve the list of NAIA Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 28 conferences

  @e2e @conference @njcaa @women
  Scenario: NJCAA Women's Conferences
    When I retrieve the list of NJCAA Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 58 conferences

  @e2e @conference @lookup
  Scenario: Lookup Conference By ID 1044
    When I retrieve the conference with ID 1044
    Then there should be no errors
    And the conference should be found
    And the conference should have the ID 1044
    And the conference should have the name "SEC"
    And the conference should have division DI
    And the conference should be a Women's conference
    And the conference should have the url "https://www.topdrawersoccer.com/college-soccer/college-conferences/conference-details/women/sec/cfid-1044"


  @e2e @conference @lookup
  Scenario: Lookup Conference By ID 123
  When I retrieve the conference with ID 123
  Then there should be no errors
  And the conference should be found
  And the conference should have the ID 123
  And the conference should have the name "California Pacific"
  And the conference should have division NAIA
  And the conference should be a Men's conference
  And the conference should have the url "https://www.topdrawersoccer.com/college-soccer/college-conferences/conference-details/men/california-pacific/cfid-123"
