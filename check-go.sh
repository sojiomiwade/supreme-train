#!/bin/bash

# Check if a directory argument was provided; default to current directory (.)
target_dir="${1:-.}"

# Ensure the provided path is a directory
if [[ ! -d "$target_dir" ]]; then
    echo "Error: '$target_dir' is not a directory."
    exit 1
fi

echo "Listing .go files without matching .py files in: $target_dir"
echo "----------------------------------------------------------"

# Loop through all .go files in the directory
for go_file in "$target_dir"/*.go; do
    
    # Handle the case where no .go files exist
    [[ -e "$go_file" ]] || continue

    # Get the base path without the .go extension
    # Example: path/to/foo.go -> path/to/foo
    base_path="${go_file%.go}"

    # Check if the corresponding .py file does NOT exist
    if [[ ! -f "${base_path}.py" ]]; then
        # Use 'basename' if you only want the filename, 
        # or just echo "$go_file" for the full path
        basename "$go_file"
    fi
done
