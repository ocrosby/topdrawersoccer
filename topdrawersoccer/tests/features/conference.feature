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
    And the list should contain 25 conferences
    And the list should contain a conference named "Horizon League"

  @e2e @conference @dii @men
  Scenario: DII Men's Conferences
    When I retrieve the list of DII Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 23 conferences
    And the list should contain a conference named "Gulf South"

  @e2e @conference @diii @men
  Scenario: DIII Men's Conferences
    When I retrieve the list of DIII Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 49 conferences
    And the list should contain a conference named "Great Northeast"
    And the list should not contain a conference named "Great South"

  @e2e @conference @naia @men
  Scenario: NAIA Men's Conferences
    When I retrieve the list of NAIA Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 29 conferences
    And the list should contain a conference named "Kentucky Intercollegiate"

  @e2e @conference @njcaa @men
  Scenario: NJCAA Men's Conferences
    When I retrieve the list of NJCAA Men's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 58 conferences
    And the list should contain a conference named "MACJC"

  @e2e @conference @di @women
  Scenario: DI Women's Conferences
    When I retrieve the list of DI Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 31 conferences
    And the list should contain a conference named "SEC"

  @e2e @conference @dii @women
  Scenario: DII Women's Conferences
    When I retrieve the list of DII Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 24 conferences
    And the list should contain a conference named "PSAC"

  @e2e @conference @diii @women
  Scenario: DIII Women's Conferences
    When I retrieve the list of DIII Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 50 conferences
    And the list should contain a conference named "Great South"

  @e2e @conference @naia @women
  Scenario: NAIA Women's Conferences
    When I retrieve the list of NAIA Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 29 conferences

  @e2e @conference @njcaa @women
  Scenario: NJCAA Women's Conferences
    When I retrieve the list of NJCAA Women's conferences
    Then there should be no errors
    And the list should not be empty
    And the list should contain 59 conferences

  @e2e @conference @lookup
  Scenario: Lookup Men's Conference By ID 1044
    When I retrieve the Women's conference with ID 1044
    Then there should be no errors
    And the conference should be found
    And the conference should have the ID 1044
    And the conference should have the name "SEC"
    And the conference should have division DI
    And the conference should be a Women's conference
    And the conference should have the url "https://www.topdrawersoccer.com/college-soccer/college-conferences/conference-details/women/sec/cfid-1044"


  @e2e @conference @lookup
  Scenario: Lookup Conference By ID 123
  When I retrieve the Men's conference with ID 123
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

  @e2e @conference @schools @lookup
  Scenario: Retrieve Schools for Men's Conference by Conference Name - Big Ten
    When I retrieve schools for the "Men's" conference with name "Big Ten"
    Then there should be no errors
    And there should be 11 schools in the list
    And the list should contain a school named "Indiana"
    And the list should contain a school named "Washington"
    And the list should contain a school named "Penn State"
    And the list should contain a school named "Michigan"
    And the list should contain a school named "Maryland"
    And the list should contain a school named "Rutgers"
    And the list should contain a school named "Michigan State"
    And the list should contain a school named "Ohio State"
    And the list should contain a school named "UCLA"
    And the list should contain a school named "Wisconsin"
    And the list should contain a school named "Northwestern"


  @e2e @conference @schools @lookup
  Scenario: Retrieve Schools for Men's Conference by Conference ID - 22
    When I retrieve schools for the "Men's" conference with ID 22
    Then there should be no errors
    And there should be 8 schools in the list
    And the list should contain a school named "Jacksonville"
    And the list should contain a school named "Central Arkansas"
    And the list should contain a school named "Bellarmine"
    And the list should contain a school named "FGCU"
    And the list should contain a school named "North Florida"
    And the list should contain a school named "Lipscomb"
    And the list should contain a school named "Stetson"
    And the list should contain a school named "Queens (N.C.)"

