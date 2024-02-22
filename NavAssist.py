"""
Usage:
NavAssist.py -i inputfile.csv

Requirements:
Pandas

Summary:
This script can be used to help create a JSON file compatible the MITRE Navigator application.
An organisation can provide a list of MITRE ATT&CK Technique IDs within a CSV file and run this
script against it. The output JSON file can be uploaded to Navigator to provide a heatmap of
your current countermeasure coverage.

The script looks for a list of MITRE Technique IDs under a column in the CSV called 'TechID' and will output 2 files:
 id_count.csv - A CSV containing a count of each ID
 NavLayer.json - A JSON file that can be used to upload to the MITRE Navigator
"""

import argparse
import csv
import json
import pandas as pd
import sys

# provide input file
parser = argparse.ArgumentParser()
parser.add_argument("-i",
                    "--input",
                    action="store",
                    dest="input_fn",
                    required=True,
)
args = parser.parse_args()
print()

# read input file
df = pd.read_csv(args.input_fn)
df.TechID = df.TechID.str.split(', ')
df = df.explode('TechID', ignore_index=True)
print("Reading input file '" + args.input_fn + "'... DONE")

# count the number of MITRE Techniques in the provided input file
idCount = df["TechID"].value_counts()
print("Counting MITRE ATT&CK Techniques... DONE")

# output a count of Technique IDs to new CSV
idCount.to_csv("id_count.csv")
print("Outputting counted IDs to 'id_count.csv'... DONE")

# static ATT&CK Navigator layer JSON fields
LAYER_VERSION = "4.5"
NAV_VERSION = "4.9.1"
NAME = "MITRE Technique Map"
DESCRIPTION = ""
DOMAIN = "enterprise-attack"

# base ATT&CK Navigator layer
layer_json = {
    "versions": {
        "layer": LAYER_VERSION,
        "navigator": NAV_VERSION
    },
    "name": NAME,
    "description": DESCRIPTION,
    "domain": DOMAIN,
    "techniques": []
}

# parse csv file, calculate a score for each technique and add it to the layer
with open("id_count.csv", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        # score each technique based the number of occurances
        technique = {
            "techniqueID": row["TechID"],
            "score": (int(row["count"]))
        }

        layer_json["techniques"].append(technique)
    print("Creating MITRE Navigator JSON file... DONE")

# add a colour gradient to the layer
layer_json["gradient"] = {
    "colors": [
        "#ff6666",
        "#ffe766",
        "#8ec843"
    ],
    "minValue": 0,
    "maxValue": max([technique["score"] for technique in layer_json["techniques"]])
}
print("Applying colour gradient... DONE")

# output JSON
with open('NavLayer.json', 'w') as outputLayer:
    json.dump(layer_json, outputLayer)
    print("Outputting MITRE ATT&CK Navigator JSON file 'NavLayer.json... DONE")
    print()
    print("Complete... EXITING")
    print()
    sys.exit(0)
