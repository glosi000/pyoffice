import os
import re


def get_files_from_wildcard(string):
    """
    Identify the files in a folder containing a wildcard.
    For now only 

    """
    wildcards = ('?', )

    if not any([w in string for w in wildcards]):
        return string

    path = os.path.foldername(string)
    files = os.listdir(path)

    matching_files = []
    pattern = rf'{string}'.replace('?', '.\.')
    if '?' in string:
        if re.match(pattern, file):
            matching_files.append(file)
        
