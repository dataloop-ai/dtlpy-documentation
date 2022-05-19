Feature: PDF Viewer modality

  Background: Initiate Platform Interface
    Given Platform Interface is initialized as dlp and Environment is set according to git branch
    And There is a project by the name of "filter-by-status"
    And There is a dataset by the name of "filter-by-status"
    And There are "10" items
    When convert "yesterday" to timestamp
    And convert "tomorrow" to timestamp

  @testrail-C4525503
  Scenario: Run "test_sdk_filter_by_status" completed items
    When I prepared test sdk filter by status "completed"
    Then I run test sdk filter by status "completed"
    And I validate test sdk filter by status "completed"

  @testrail-C4525503
  Scenario: Run "test_sdk_filter_by_status" discarded items
    When I prepared test sdk filter by status "discard"
    Then I run test sdk filter by status "discard"
    And I validate test sdk filter by status "discard"

  @testrail-C4525503
  Scenario: Run "test_sdk_filter_by_status" approved items
    When I prepared test sdk filter by status "approved"
    Then I run test sdk filter by status "approved"
    And I validate test sdk filter by status "approved"
