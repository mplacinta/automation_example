# Created by Marina at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can open shoes page
    Given Open Gojane page
    When Click on SHOES link
    Then Top navigation is All Shoes

  Scenario: User can open dresses page
    Given Open Gojane page
    When Click ont DRESSES link
    Then Top navigation is All Dresses

  Scenario: User can open clothing page
    Given Open Gojane page
    When Click on CLOTHING link
    Then Top navigation is All Clothes
