# NavAssist
A Python script to help create a JSON layer for the MITRE Navigator

## Summary
This script can be used to help create a JSON file compatible the MITRE Navigator application.
An organisation can provide a list of MITRE ATT&CK Technique IDs within a CSV file and run this
script against it. The output JSON file can be uploaded to Navigator to provide a heatmap of
your current countermeasure coverage.

The script looks for a list of MITRE Technique IDs under a column in the CSV called 'TechID' and will output 2 files:
 id_count.csv - A CSV containing a count of each ID
 NavLayer.json - A JSON file that can be used to upload to the MITRE Navigator

## Requirements
Pandas

## Usage
NavAssist.py -i inputfile.csv
