Feature: Data versioning tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch

    @testrail-C4528883
    @project.delete
    Scenario: Run "Data Versioning"
        When I prepared test data versioning introduction
            |Section |
            |Section1|

        Then I run test data versioning introduction
        And  I validate test data versioning faas introduction

    @testrail-C4528883
    @project.delete
    Scenario: Run "Merge Datasets"
        When I prepared test faas introduction
        Then I run test faas introduction
        And  I validate test faas introduction