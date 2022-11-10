Feature: Upload and manage annotations

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch

    @testrail-C
    Scenario: Sanity
        Given There is a project by the name of "upload and manage annotations project"
        And   There is a dataset by the name of "upload and manage annotations dataset"
        And   There is an item with annotations of type "image"

    @testrail-C
    Scenario Outline: Run "Data Versioning" "<Section name>"
        When I prepared test upload and manage annotations "<Section name>"
        Then I run test upload and manage annotations "<Section name>"

    Examples:
        | Section name |
        | section1     |
#        | section2     |
#        | section3     |
#        | section4     |
#        | section5     |
#        | section5a    |
#        | section5b    |
#        | section6     |
#        | section7     |
#        | section8     |
#        | section9     |
#        | section10    |
#        | section11    |
#        | section12    |
#        | section13    |
#        | section14    |
#        | section15    |
#        | section16    |
#        | section17    |
#        | section18    |
#        | section19    |
