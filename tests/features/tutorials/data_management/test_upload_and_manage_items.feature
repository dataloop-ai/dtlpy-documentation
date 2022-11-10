Feature: Test upload and manage items tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And   There is a project by the name of "test upload and manage items project"
        And   There is a dataset by the name of "test upload and manage items dataset"
        And   There is an item of type "image"

    @testrail-C
    Scenario Outline: Run "Data Versioning" "<Section name>"
        When I prepared test upload and manage items "<Section name>"
        Then I run test upload and manage items "<Section name>"

    Examples:
        | Section name |
#        | section1     |
#        | section2     |
#        | section3     |
#        | section4     |
        | section5     |

