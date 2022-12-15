Feature: Working with metadata tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And   There is a project by the name of "working with metadata project"
        And   There is a dataset by the name of "working with metadata dataset"

    @testrail-C
    Scenario Outline: Run "Data Versioning" "<Section name>"
        When I prepared test working with metadata "<Section name>"
        Then I run test working with metadata "<Section name>"
        And  There is an item with annotations of type "image"

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
        | section12    |
        #| section13    |
        #| section14    |
        | section15    |
