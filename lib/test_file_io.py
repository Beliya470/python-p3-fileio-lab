# File: test_file_io.py

from file_io import write_file, append_file, read_file
import os

def test_write_read_file(tmp_path):
    file_name = tmp_path / "test_logfile.txt"
    file_content = "Log 1: 5 bananas added"
    
    # Write to the file
    write_file(file_name, file_content)
    
    # Read from the file
    content = read_file(file_name)
    
    assert content == file_content

def test_append_read_file(tmp_path):
    file_name = tmp_path / "test_logfile.txt"
    file_content = "Log 1: 5 bananas added"
    append_content = "Log 2: 3 bananas subtracted"
    
    # Write to the file first
    write_file(file_name, file_content)

    # Append to the file
    append_file(file_name, append_content)
    
    # Read from the file
    expected_content = file_content + "\n" + append_content
    content = read_file(file_name)
    
    assert content == expected_content

def test_write_file(tmp_path):
    """Test write_file()"""
    file_name = tmp_path / "test_file.txt"  # .txt extension added here
    file_content = "This is a test content."
    write_file(file_name, file_content)
    with open(file_name, 'r') as f:  # No need to append .txt again
        assert f.read() == file_content


# Since tmp_path automatically handles cleanup, we don't need explicit removal.
