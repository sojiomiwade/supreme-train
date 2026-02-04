#!/bin/bash

##############################################################
# get a random go file, for which there is no python file
##############################################################
# Check if a directory argument was provided; default to current directory (.)
target_dir="${1:-.}"

if [[ ! -d "$target_dir" ]]; then
    echo "Error: '$target_dir' is not a directory."
    exit 1
fi

# Initialize an empty array to store our matches
orphaned_go_files=()

echo "Listing .go files without matching .py files in: $target_dir"
echo "----------------------------------------------------------"

for go_file in "$target_dir"/*.go; do
    # Skip if no .go files exist
    [[ -e "$go_file" ]] || continue

    base_path="${go_file%.go}"

    if [[ ! -f "${base_path}.py" ]]; then
        filename=$(basename "$go_file")
        echo "$filename"
        # Add the filename to our array for later selection
        orphaned_go_files+=("$filename")
    fi
done

# Print a random file if any were found
if [[ ${#orphaned_go_files[@]} -gt 0 ]]; then
    echo "----------------------------------------------------------"
    # Generate a random index based on the array length
    random_index=$(( RANDOM % ${#orphaned_go_files[@]} ))
    echo "Randomly selected file: ${orphaned_go_files[$random_index]}"
else
    echo "No matching files found to pick from."
fi
