Feature: Data versioning tutorial

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch

    @testrail-C4528883
    Scenario: Sanity
        Given I prepared a project by the name of "data version project"
        And   I prepared a dataset by the name of "data version dataset"
        And   I prepared a dataset by the name of "data version dataset"
        And   I prepared an item with annotations of type "image"

    @testrail-C4528883
    Scenario: Run "Data Versioning"
        When I prepared test data versioning introduction
            | Section name |
            | section1     |
        Then I run test data versioning introduction
            | Section name |
            | section1     |
        And  I validate test data versioning faas introduction
            | Section name |
            | section1     |

    @testrail-C4528883
    Scenario: Run "Merge Datasets"
        When I prepared test data versioning introduction
            | Section name |
            | section2     |
        Then I run test data versioning introduction
            | Section name |
            | section2     |
        And  I validate test data versioning faas introduction
            | Section name |
            | section2     |