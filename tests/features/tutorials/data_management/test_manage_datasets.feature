Feature: Manage datasets tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch

    @testrail-C4528884
    @project.delete
    Scenario: Sanity
        Given I prepared project by the name of "manage datasets project"


    @testrail-C4528884
    @project.delete
    Scenario: Upload & Manage Annotations
        When I prepared test upload and manage annotations
            | Section name |
            | section1     |
        Then I run test upload and manage annotations
            | Section name |
            | section1     |
        And  I validate test upload and manage annotations
            | Section name |
            | section1     |