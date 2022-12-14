Feature: Modalities

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And   There is a project by the name of "modalities project"
        And   There is a dataset by the name of "modalities dataset"

    @testrail-C
    Scenario Outline: Run "Modalities" "<Section name>"
        When I prepared test modalities "<Section name>"
        Then I run test modalities "<Section name>"

    Examples:
        | Section name |
        | section1     |
        | section2     |
        #| section3     | NOT RUNNABLE
        | section4     |
        #| section5     | CHECKED FROM section4
