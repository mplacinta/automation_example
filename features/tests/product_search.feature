# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for dresses
    Given Open Google page
    When Input dress into search field
    And Click on search icon
    Then Product results for dress are shown
    And First result contains dress