# Python Standard Library Imports
import pathlib

# Third Party Imports
import pytest

# Pysarch Imports
from pysarch.parse import extract_git_commits


@pytest.fixture
def git_log_file() -> str:
    path_to_git_log_output = pathlib.Path("tests") / "test_git_log_output.txt"
    assert path_to_git_log_output.exists()
    with open(path_to_git_log_output, "r") as fileHandle:
        git_log_text = fileHandle.read()
    return git_log_text


def test_can_compute_number_of_commits(git_log_file):
    commit_header_lines = extract_git_commits(git_log_file)
    assert len(commit_header_lines) == 88


def test_can_compute_number_of_entities(git_log_file):
    pass
