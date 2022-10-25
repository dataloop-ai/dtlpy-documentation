Feature: Upload and manage annotations

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch

    @testrail-C4528884
    @project.delete
    Scenario: Sanity
        Given I prepared project by the name of "upload and manage annotations project"
        And   I prepared dataset by the name of "upload and manage annotations dataset"
        And


    @testrail-C4528884
    @project.delete
    Scenario: Upload & Manage Annotations
        When I prepared test upload and manage annotations introduction
            | Section name |
            | section1     |
        Then I run test upload and manage annotations introduction
            | Section name |
            | section1     |
        And  I validate test upload and manage annotations introduction
            | Section name |
            | section1     |

    @testrail-C4528884
    @project.delete
    Scenario: Upload User Metadata
        When I prepared test upload and manage annotations introduction
            | Section name |
            | section2     |
        Then I run test upload and manage annotations introduction
            | Section name |
            | section2     |
        And  I validate test upload and manage annotations introduction
            | Section name |
            | section2     |

    @testrail-C4528884
    @project.delete
    Scenario: Convert Annotations To COCO Format
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Upload Entire Directory and their Corresponding Dataloop JSON Annotations
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Upload Annotations To Video Item
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Upload Annotations In VTT Format
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Upload Audio Annotation to an Audio File
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Set Attributes On Annotations
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Range Attributes (Slider in UI)
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: CheckBox Attribute (Multiple choice)
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Radio Button Attribute (Single Choice)
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Yes/No Attribute
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Show Annotations Over Image
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: To see the item itself with all annotations, use the Annotations option.
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: The annotation option can also be a list to download multiple options
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Filter by Item and/or Annotation
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Filter by Annotations
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction


    @testrail-C4528884
    @project.delete
    Scenario: Download Annotations in COCO/YOLO/VOC Format
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Exporting Files with File Extension as Part of the Filename
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction

    @testrail-C4528884
    @project.delete
    Scenario: Download NdArray with Numpy
        When I prepared test upload and manage annotations introduction
        Then I run test upload and manage annotations introduction
        And  I validate test upload and manage annotations introduction