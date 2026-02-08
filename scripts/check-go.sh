#!/bin/bash

# Ensure a directory is provided and ends with /go or /go/
input_dir="${1%/}" # Strip trailing slash for consistency

if [[ "$input_dir" != */go ]]; then
    echo "Error: Target directory must end in '/go' (e.g., /path/to/project/go)"
    exit 1
fi

# Define the python sibling directory by replacing the trailing /go with /python
python_dir="${input_dir%/go}/py"

if [[ ! -d "$python_dir" ]]; then
    echo "Warning: Python sibling directory '$python_dir' does not exist."
    # We continue anyway, as this just means NO .go file will have a .py match
fi

orphaned_go_files=()

echo "Checking .go files in: $input_dir"
echo "Looking for matches in: $python_dir"
echo "----------------------------------------------------------"

for go_file in "$input_dir"/*.go; do
    [[ -e "$go_file" ]] || continue

    # Get the filename only (e.g., "foo.go")
    filename=$(basename "$go_file")
    # Get the filename without extension (e.g., "foo")
    base_name="${filename%.go}"

    # Check if the .py version exists in the /python/ directory
    if [[ ! -f "$python_dir/${base_name}.py" ]]; then
        echo "$filename"
        orphaned_go_files+=("$filename")
    fi
done

# Print a random file if any were found
if [[ ${#orphaned_go_files[@]} -gt 0 ]]; then
    echo "----------------------------------------------------------"
    random_index=$(( RANDOM % ${#orphaned_go_files[@]} ))
    echo "Randomly selected file: ${orphaned_go_files[$random_index]}"
else
    echo "No .go files found without a corresponding .py file."
fi
