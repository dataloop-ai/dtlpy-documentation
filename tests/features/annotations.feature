Feature: Project Entity repo services

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch
        And There is a project by the name of "test annotations examples"

    Scenario: Run "copy annotations"
        When I Run Script "examples/annotations/copy_annotations.py" | to_project |
        Then I succeed

