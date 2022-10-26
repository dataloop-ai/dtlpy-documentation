Feature: Manage datasets tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch

    @testrail-C4528884
    @project.delete
    Scenario: Sanity
        Given I prepared project by the name of "manage datasets project"


    @testrail-C4528884
    @project.delete
    Scenario Outline: Upload & Manage Annotations "<Section name>"
        When I prepared test upload and manage annotations "<Section name>"
        Then I run test upload and manage annotations "<Section name>"
        And  I validate test upload and manage annotations "<Section name>"

    Examples:
        | Section name |
        | section1     |
        | section2     |

    Feature: Data versioning tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And   There is a project by the name of "data versioning project"
        And   There is a dataset by the name of "data versioning dataset"
        And   There is an item with annotations of type "image"



