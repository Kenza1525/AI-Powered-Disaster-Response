#!/bin/bash

# Set the directory containing the .tsv files
TSV_DIR="$HOME/Principles_project/CrisisKAN/datasets/CrisisMMD_v2.0/crisismmd_datasplit_all"

# Ensure the directory exists
if [ ! -d "$TSV_DIR" ]; then
    echo "Error: Directory $TSV_DIR does not exist."
    exit 1
fi

# Find all .tsv files and process each one
for file in "$TSV_DIR"/*.tsv; do
    # Check if the file exists before processing
    if [ ! -f "$file" ]; then
        echo "No .tsv files found in $TSV_DIR."
        exit 1
    fi

    # Extract filename
    filename=$(basename -- "$file")
    
    # Temporary output file
    temp_output="${TSV_DIR}/${filename}.tmp"

    # Run the Python script
    echo "Processing: $file -> Overwriting"
    python3 regex_tweet.py "$file" "$temp_output"

    # If processing is successful, overwrite the original file
    if [ -f "$temp_output" ]; then
        mv "$temp_output" "$file"
        echo "Successfully overwritten: $file"
    else
        echo "Error: Processing failed for $file"
    fi
done

echo "All .tsv files have been processed and overwritten."
