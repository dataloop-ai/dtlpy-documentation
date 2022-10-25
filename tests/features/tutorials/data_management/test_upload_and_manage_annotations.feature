Feature: Upload and manage annotations

    Background: Initiate Platform Interface
        Given Platform Interface is initialized as dlp and Environment is set according to git branch

    @testrail-C4528884
    Scenario: Sanity
        Given I prepared project by the name of "upload and manage annotations project"
        And   I prepared dataset by the name of "upload and manage annotations dataset"
        And   I prepared an item of type "image"

    @testrail-C4528884
    Scenario: Upload & Manage Annotations
        When I prepared test upload and manage annotations
            | Section name |
            | section1     |
        Then I run test upload and manage annotations
            | Section name |
            | section1     |
        And  I validate test upload and manage annotations
            | Section name |
            | section1     |

    @testrail-C4528884
    Scenario: Upload User Metadata
        When I prepared test upload and manage annotations
            | Section name |
            | section2     |
        Then I run test upload and manage annotations
            | Section name |
            | section2     |
        And  I validate test upload and manage annotations
            | Section name |
            | section2     |

    @testrail-C4528884
    Scenario: Convert Annotations To COCO Format
        When I prepared test upload and manage annotations
            | Section name |
            | section3     |
        Then I run test upload and manage annotations
            | Section name |
            | section3     |
        And  I validate test upload and manage annotations
            | Section name |
            | section3     |

    @testrail-C4528884
    Scenario: Upload Entire Directory and their Corresponding Dataloop JSON Annotations
        When I prepared test upload and manage annotations
            | Section name |
            | section4     |
        Then I run test upload and manage annotations
            | Section name |
            | section4     |
        And  I validate test upload and manage annotations
            | Section name |
            | section4     |

    @testrail-C4528884
    Scenario: Upload Annotations To Video Item
        When I prepared test upload and manage annotations
            | Section name |
            | section5     |
        Then I run test upload and manage annotations
            | Section name |
            | section5     |
        And  I validate test upload and manage annotations
            | Section name |
            | section5     |

    @testrail-C4528884
    Scenario: Upload Annotations In VTT Format
        When I prepared test upload and manage annotations
            | Section name |
            | section5a    |
        Then I run test upload and manage annotations
            | Section name |
            | section5a    |
        And  I validate test upload and manage annotations
            | Section name |
            | section5a    |

    @testrail-C4528884
    Scenario: Upload Audio Annotation to an Audio File
        When I prepared test upload and manage annotations
            | Section name |
            | section5b    |
        Then I run test upload and manage annotations
            | Section name |
            | section5b    |
        And  I validate test upload and manage annotations
            | Section name |
            | section5b    |

    @testrail-C4528884
    Scenario: Set Attributes On Annotations
        When I prepared test upload and manage annotations
            | Section name |
            | section6     |
        Then I run test upload and manage annotations
            | Section name |
            | section6     |
        And  I validate test upload and manage annotations
            | Section name |
            | section6     |

    @testrail-C4528884
    Scenario: Range Attributes (Slider in UI)
        When I prepared test upload and manage annotations
            | Section name |
            | section7     |
        Then I run test upload and manage annotations
            | Section name |
            | section7     |
        And  I validate test upload and manage annotations
            | Section name |
            | section7     |

    @testrail-C4528884
    Scenario: CheckBox Attribute (Multiple choice)
        When I prepared test upload and manage annotations
            | Section name |
            | section8     |
        Then I run test upload and manage annotations
            | Section name |
            | section8     |
        And  I validate test upload and manage annotations
            | Section name |
            | section8     |

    @testrail-C4528884
    Scenario: Radio Button Attribute (Single Choice)
        When I prepared test upload and manage annotations
            | Section name |
            | section9     |
        Then I run test upload and manage annotations
            | Section name |
            | section9     |
        And  I validate test upload and manage annotations
            | Section name |
            | section9     |

    @testrail-C4528884
    Scenario: Yes/No Attribute
        When I prepared test upload and manage annotations
            | Section name |
            | section10    |
        Then I run test upload and manage annotations
            | Section name |
            | section10    |
        And  I validate test upload and manage annotations
            | Section name |
            | section10    |

    @testrail-C4528884
    Scenario: Show Annotations Over Image
        When I prepared test upload and manage annotations
            | Section name |
            | section11    |
        Then I run test upload and manage annotations
            | Section name |
            | section11    |
        And  I validate test upload and manage annotations
            | Section name |
            | section11    |

    @testrail-C4528884
    Scenario: To see the item itself with all annotations, use the Annotations option
        When I prepared test upload and manage annotations
            | Section name |
            | section12    |
        Then I run test upload and manage annotations
            | Section name |
            | section12    |
        And  I validate test upload and manage annotations
            | Section name |
            | section12    |

    @testrail-C4528884
    Scenario: Download Data, Annotations & Metadata
        When I prepared test upload and manage annotations
            | Section name |
            | section13    |
        Then I run test upload and manage annotations
            | Section name |
            | section13    |
        And  I validate test upload and manage annotations
            | Section name |
            | section13    |

    @testrail-C4528884
    Scenario: NOTE: The annotation option can also be a list to download multiple options
        When I prepared test upload and manage annotations
            | Section name |
            | section14    |
        Then I run test upload and manage annotations
            | Section name |
            | section14    |
        And  I validate test upload and manage annotations
            | Section name |
            | section14    |

    @testrail-C4528884
    Scenario: Filter by Item and/or Annotation
        When I prepared test upload and manage annotations
            | Section name |
            | section15    |
        Then I run test upload and manage annotations
            | Section name |
            | section15    |
        And  I validate test upload and manage annotations
            | Section name |
            | section15    |


    @testrail-C4528884
    Scenario: Filter by Annotations
        When I prepared test upload and manage annotations
            | Section name |
            | section16    |
        Then I run test upload and manage annotations
            | Section name |
            | section16    |
        And  I validate test upload and manage annotations
            | Section name |
            | section16    |

    @testrail-C4528884
    Scenario: Download Annotations in COCO/YOLO/VOC Format
        When I prepared test upload and manage annotations
            | Section name |
            | section17    |
        Then I run test upload and manage annotations
            | Section name |
            | section17    |
        And  I validate test upload and manage annotations
            | Section name |
            | section17    |

    @testrail-C4528884
    Scenario: Exporting Files with File Extension as Part of the Filename
        When I prepared test upload and manage annotations
            | Section name |
            | section18    |
        Then I run test upload and manage annotations
            | Section name |
            | section18    |
        And  I validate test upload and manage annotations
            | Section name |
            | section18    |

    @testrail-C4528884
    @project.delete
    Scenario: Download NdArray with Numpy
        When I prepared test upload and manage annotations
            | Section name |
            | section19    |
        Then I run test upload and manage annotations
            | Section name |
            | section19    |
        And  I validate test upload and manage annotations
            | Section name |
            | section19    |