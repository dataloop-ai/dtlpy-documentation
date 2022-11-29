Feature: Download annotations one by one example

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And There is a project by the name of "download-items"

    @testrail-C4525172
    @tests_assets.delete
    Scenario: Run "download one by one"
        When I prepared download one by one example
        Then I run download one by one example
        And I validate download one by one example