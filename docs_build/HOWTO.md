# This Doc Repo
The tutorials in this repo are auto generated from text and scripts is separate files.
This gives us the possibility to:
1. Run tests on the code snippets (keep them up-to-date)
2. Build the docs into multiple formats (Md files and Jupyter Notebooks)
3. Control the structure of the tutorials and hierarchy

## Adding Tutorials
The raw tutorials should be located in "tutorials_templates".
Each tutorial has the following structure:
1. mds.py - contain all the text
2. scripts.py - contain all the scripts
3. skeleton.json - contain the instructions to interleave the text and scripts

For each directory, there's an index.json to build the structure of the chpaters inside this dir

## Build
Run the `collect_tutorials.py` to collect all tutorials form the "tutorials_templates" and build the final "tutorials" directory.


