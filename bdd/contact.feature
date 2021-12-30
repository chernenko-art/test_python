Scenario Outline: Add new user
  Given a user list
  Given a user with <firstname>, <lastname> and <middlename>
  When I add the user to the list
  Then the new user list is equal to the old list with the added user

  Examples:
  | firstname  | lastname  | middlename  |
  | Ivan       | Ivanov    | Ivanovich   |
  | Ivan1      | Ivanov1   | Ivanovich1  |

Scenario Outline: Delete a user
  Given a non-empty user list
  Given a random user from the list
  When I delete the user from the list
  Then the new user list is equal to the old list without the deleted user

Scenario: Modify a user
  Given a non-empty user list
  Given a random user from the list
  When I modify the user from the list
  Then the new user list is equal to the old list with modified user