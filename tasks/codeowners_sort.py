#!/usr/bin/env python
"""Sort the CODEOWNERS file for lexicographic order.

Usage:

    pdm run codeowners_sort
"""

import os

from pathlib import Path


PROJECT_ROOT = Path(os.getenv("PDM_PROJECT_ROOT", "."))

if __name__ == "__main__":
    # We can leverage PDM_PROJECT_ROOT here.
    codeowners_file = PROJECT_ROOT / Path(".github/CODEOWNERS")
    content = codeowners_file.read_text()
    new_content = []
    for line in content.splitlines():
        # Ignore commented lines
        if line.startswith("#"):
            new_content.append(line)
            continue
        # Ignore blank lines
        if len(line) == 0:
            new_content.append(line)
            continue
        # The path is the rule at the first field, members are everything after
        rule, *members = line.split()
        # Remake the line with the rule and the sorted members
        new_line = " ".join([rule, *sorted(members)])
        new_content.append(new_line)
    # Rejoin all the lines, separated by newlines that were stripped
    new_text = "\n".join(new_content)
    # Add new line at end of file if it doesn't exist
    if not new_text.endswith("\n"):
        new_text += "\n"
    # Finally write the file.
    codeowners_file.write_text(new_text)
