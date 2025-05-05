# Contribution Guidelines for Dataloop.ai Documentation Repository

Thank you for your interest in contributing to the Dataloop.ai documentation repository!
We are excited to work with you to create high-quality content that helps our developer community use Dataloop.ai
effectively.
To ensure that your contributions are successful, please follow the guidelines below.

## Forking the Repository

To contribute to the Dataloop.ai documentation repository, you will need to create a fork of the repository on Github.
To do this, follow these steps:

* Go to the Dataloop.ai documentation repository on Github.
* Click the "Fork" button in the upper right corner of the page.
* Select your Github account as the location to fork the repository.

## Adding Content

### Naming Conventions

* File names should be only with underscore and lowercase letters e.g. `lower_case_with_underscores`

### Tutorials Auto-Build

The tutorials in this repo are auto generated from text and scripts is separate files.
This gives us the possibility to:

1. Run tests on the code snippets (keep them up-to-date)
2. Build the docs into multiple formats (Md files and Jupyter Notebooks)
3. Control the structure of the tutorials and hierarchy (using the skeleton.json on each chapter and index.json for the
   directory structure)

#### Adding Tutorials

The raw tutorials should be located in "tutorials_templates" under "docs_build".
Each tutorial should contain a markdown file that includes the python code snippets within the \```python ``` symbols.


#### Build

Run the `python docs_build/main.py` to collect all tutorials form the "docs_build/tutorials_templates" and build the final
"tutorials" directory.

*NOTE buildimg the tutorials from the template directory will OVERWRITE the `tutorials` folder with the changes from the
template!*

## Passing Tests

Before your pull request can be merged into the main repository, it must pass a series of tests.
These tests ensure that the content is formatted correctly and that there are no syntax errors. To run the tests, follow
these steps:

* Navigate to your fork of the repository in GitHub.
* Click on the "Actions" tab.
* Click on the latest workflow run.
* Check the status of the tests. If they have passed, you can proceed to the next step.

## Creating a Pull Request

After you have created a fork of the repository, you can make changes to the content and submit a pull request (PR) for
review.
To create a pull request, follow these steps:

Make changes to the content in your fork of the repository.

* Commit your changes to your fork.
* Create a new pull request in GitHub by navigating to the original repository and clicking on the "New pull request"
  button.
* Select your fork as the source of the pull request and the original repository as the destination.
* Add a title and description to the pull request, describing the changes you have made.

## Final

Thank you for your contributions to the Dataloop.ai documentation repository! We appreciate your efforts to help our
community learn and grow.



