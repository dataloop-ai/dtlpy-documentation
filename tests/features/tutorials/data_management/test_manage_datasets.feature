Feature: Manage datasets tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And   There is a project by the name of "manage datasets project"
        And   There is a dataset by the name of "manage datasets dataset"
        And   There is an item with annotations of type "image"

    @testrail-C4532885
    Scenario Outline: Run "Upload & Manage Annotations" "<Section name>"
        When I prepared test manage datasets "<Section name>"
        Then I run test manage datasets "<Section name>"

    Examples:
        | Section name |
        | section1     |
#        | section2     | #TODO: Solve Driver security issues
        | section3     |
        | section4     |
        | section5     |




