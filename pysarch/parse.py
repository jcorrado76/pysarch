"""
Utilities for parsing git log information from plain text files
"""
# Python Standard Library Imports
import re

# the format used in the git log command used to generate the text file
GIT_LOG_FORMAT = "'[%h] %an %ad %s'"

# the regex to match the header line for each commit
COMMIT_FIRST_LINE_PATTERN = (
    r"\[(?P<hash>\w+)\] ([\w\s]+) (\d{4})-(\d{2})-(\d{2}) (.+)\n"
)


def extract_git_commits(git_log_text: str):
    # sourcery skip: inline-immediately-returned-variable
    """
    Extract the git commit header lines from a log file whose contents look like
    this:

    [d804759] Adam Petersen 2013-09-24 Documented tree map visualizations
    5	1	README.md
    -	-	doc/imgs/tree_map_sample.png

    [1bafb6d] Adam Petersen 2013-09-24 Release 0.3.1
    1	1	project.clj
    """
    matched_header_lines = re.findall(COMMIT_FIRST_LINE_PATTERN, git_log_text)
    return matched_header_lines
