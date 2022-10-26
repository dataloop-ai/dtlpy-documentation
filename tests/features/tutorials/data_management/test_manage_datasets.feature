Feature: Manage datasets tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And   There is a project by the name of "data versioning project"

    @testrail-C4528884
    Scenario Outline: Run "Upload & Manage Annotations" "<Section name>"
        When I prepared test upload and manage annotations "<Section name>"
        Then I run test upload and manage annotations "<Section name>"
        And  I validate test upload and manage annotations "<Section name>"

    Examples:
        | Section name |
        | section1     |
        | section2     |
        | section3     |
        | section4     |
        | section5     |




