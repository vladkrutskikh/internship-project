# Created by vladkrutskikh at 23.04.2025
@web
Feature: Test secondary deals page for going through the pagination

  Scenario: The User can open the Secondary deals page and go through the pagination 2
    Given Open main page Reely
    Given Log in to the page
    When For MOB click on the Secondary option at the left side menu
    Then Verify the right page Secondary deals opens
    When For MOB go to the final page using the pagination button
    When For MOB go back to the first page using the pagination button