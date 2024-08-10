# Created by omar at 8/7/24
# See: https://www.topdrawersoccer.com/college-soccer/college-conferences/di/divisionid-1
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
    And the list should contain a conference named "Horizon League"

  @e2e @conference @dii @men
  Scenario: DII Men's Conferences
    When I retrieve the list of DII Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 22 conferences
    And the list should contain a conference named "Gulf South"

  @e2e @conference @diii @men
  Scenario: DIII Men's Conferences
    When I retrieve the list of DIII Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 48 conferences
    And the list should contain a conference named "Great Northeast"
    And the list should not contain a conference named "Great South"

  @e2e @conference @naia @men
  Scenario: NAIA Men's Conferences
    When I retrieve the list of NAIA Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 28 conferences
    And the list should contain a conference named "Kentucky Intercollegiate"

  @e2e @conference @njcaa @men
  Scenario: NJCAA Men's Conferences
    When I retrieve the list of NJCAA Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 57 conferences
    And the list should contain a conference named "MACJC"

  @e2e @conference @di @women
  Scenario: DI Women's Conferences
    When I retrieve the list of DI Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 30 conferences
    And the list should contain a conference named "SEC"

  @e2e @conference @dii @women
  Scenario: DII Women's Conferences
    When I retrieve the list of DII Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 23 conferences
    And the list should contain a conference named "PSAC"

  @e2e @conference @diii @women
  Scenario: DIII Women's Conferences
    When I retrieve the list of DIII Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 49 conferences
    And the list should contain a conference named "Great South"

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


  @e2e @conference @lookup
  Scenario: Lookup Men's Conference By Name - Big Ten
    When I retrieve the Men's conference with name "Big Ten"
    Then there should be no errors
    And the conference should be found
    And the conference should have the ID 7
    And the conference should have the name "Big Ten"
    And the conference should have division DI
    And the conference should be a Men's conference
    And the conference should have the url "https://www.topdrawersoccer.com/college-soccer/college-conferences/conference-details/men/big-ten/cfid-7"


  @e2e @conference @lookup
  Scenario: Lookup Women's Conference By Name - Big Ten
    When I retrieve the Women's conference with name "Big Ten"
    Then there should be no errors
    And the conference should be found
    And the conference should have the ID 7
    And the conference should have the name "Big Ten"
    And the conference should have division DI
    And the conference should be a Women's conference
    And the conference should have the url "https://www.topdrawersoccer.com/college-soccer/college-conferences/conference-details/women/big-ten/cfid-7"


  Scenario: Retrieve Schools for Conference by Conference Name

  Scenario: Retrieve Schools for Conference by Conference ID
    When I retrieve the schools for the conference with ID 22
    Then there should be no errors
    And there should be 12 schools in the list
    And the list should contain a school named "Libscomb"
    And the list should contain a school named "North Florida"
    And the list should contain a school named "Central Arkansas"
    And the list should contain a school named "FGCU"
    And the list should contain a school named "Eastern Kentucky"
    And the list should contain a school named "Bellarmine"
    And the list should contain a school named "Austin Peay"
    And the list should contain a school named "Jacksonville"
    And the list should contain a school named "North Alabama"
    And the list should contain a school named "Stetson"
    And the list should contain a school named "Queens (N.C.)"
    And the list should contain a school named "West Georgia"

