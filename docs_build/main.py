from build_tutorials import build_tutorials
from build_readme_file import build_readme
from check_links import check_links
from build_redocly import build_redocly

if __name__ == "__main__":
    check_links()
    build_tutorials()
    build_readme()
    build_redocly()
