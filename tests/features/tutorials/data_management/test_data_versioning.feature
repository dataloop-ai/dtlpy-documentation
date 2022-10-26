Feature: Data versioning tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And   There is a project by the name of "data versioning project"
        And   There is a dataset by the name of "data versioning dataset"
        And   There is an item with annotations of type "image"

    @testrail-C4528883
    Scenario Outline: Run "Data Versioning"
        When I prepared test data versioning "<Section name>"
        Then I run test data versioning "<Section name>"
        And  I validate test data versioning "<Section name>"

    Examples:
        | Section name |
        | section1     |
        | section2     |