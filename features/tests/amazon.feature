# Created by Marina at 4/24/19
Feature: Solution search

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon page
    And Click Help on Amazon page
    When Input Cancel order into Amazon more solutions field
    And Click the Go button
    Then Cancel Items or Orders text is present