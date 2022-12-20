Feature: Working with metadata tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And   There is a project by the name of "working with metadata project"
        And   There is a dataset by the name of "working with metadata dataset"
        And   There is an item with annotations of type "image"

    @testrail-C
    Scenario Outline: Run "Working with metadata" "<Section name>"
        When I prepared test working with metadata "<Section name>"
        Then I run test working with metadata "<Section name>"

    Examples:
        | Section name |
        | section1     |
        | section2     |
        | section3     |
        | section4     |
        | section5     |
        | section6     |
        | section7     |
        | section8     |
        | section9     |
        | section10    |
        | section11    |
        #| section12    | RUNNING FROM section11
        #| section13    | RUNNING FROM section11
        #| section14    | RUNNING FROM section11
        | section15    |
