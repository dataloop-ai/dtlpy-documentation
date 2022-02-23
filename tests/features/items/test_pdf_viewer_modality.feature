Feature: PDF Viewer modality

  Background: Initiate Platform Interface
    Given Platform Interface is initialized as dlp and Environment is set according to git branch
    And There is a project by the name of "pdf-modality"


  @testrail-C4525502
  Scenario: Run "pdf_viewer_modality" on jpg file
    When I prepared pdf viewer modality example on "images/hamster.jpg"
    Then I run pdf viewer modality example
    And I validate pdf viewer modality example

  @testrail-C4525502
  Scenario: Run "pdf_viewer_modality" on png file
    When I prepared pdf viewer modality example on "pipeline_example.png"
    Then I run pdf viewer modality example
    And I validate pdf viewer modality example