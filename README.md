# NavAssist

A utility script to generate MITRE ATT&CK Navigator layers from CSV files containing technique IDs.

## Overview

NavAssist helps organizations visualize their security coverage by generating MITRE ATT&CK Navigator compatible JSON files. By processing a CSV file containing MITRE ATT&CK technique IDs, the script creates a heat map that can be uploaded to the MITRE Navigator web application, providing a visual representation of your security posture.

## Features

- Convert CSV files with MITRE ATT&CK technique IDs into Navigator-compatible layers
- Generate heat maps based on technique frequency 
- Apply color gradients to visualize coverage density
- Output both summary statistics (ID counts) and Navigator layer files

## Prerequisites

- Python 3.6+
- Pandas library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/NavAssist.git
   cd NavAssist
   ```

2. Install required dependencies:
   ```bash
   pip install pandas
   ```

## Usage

Run the script with an input CSV file containing a column named 'TechID' with MITRE ATT&CK technique IDs:

```bash
python NavAssist.py -i inputfile.csv
```

### Input Format

Your CSV file must contain a column named 'TechID' with MITRE technique IDs. Multiple technique IDs in a single row can be separated by commas.

Example input CSV:
```csv
Name,Description,TechID
Phishing Detection,Email filtering for phishing attempts,T1566, T1566.001, T1566.002
Macro Security,Disables macros in Office documents,T1204.002, T1059.005
```

### Outputs

The script generates two files:

1. `id_count.csv` - A CSV containing each technique ID and its frequency count
2. `NavLayer.json` - A JSON file that can be uploaded to MITRE ATT&CK Navigator

## Visualizing Results

To visualize your results:

1. Go to the [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
2. Click "Open Existing Layer"
3. Upload the generated `NavLayer.json` file
4. View your technique coverage heat map

## Example Output

The generated `id_count.csv` will look like:
```csv
TechID,count
T1566.001,12
T1204.002,8
T1059.005,6
T1566.002,5
T1566,3
```

The heat map in MITRE Navigator will show these techniques with different colors based on their frequency, helping you identify:
- Most common techniques your organization encounters or defends against
- Gaps in your security coverage
- Areas where you might have excessive or redundant controls

## How It Works

NavAssist performs the following operations:

1. Reads the input CSV file
2. Extracts and explodes any comma-separated technique IDs
3. Counts the frequency of each technique ID
4. Outputs the count to `id_count.csv`
5. Creates a MITRE Navigator layer JSON with each technique scored by frequency
6. Applies a color gradient from yellow to red based on scores
7. Outputs the final layer to `NavLayer.json`

## Customization

You can modify the script to customize:

- The color gradient in the `gradient` section of the JSON
- The layer name and description
- The scoring mechanism (currently based solely on frequency)

## Limitations

- The script expects a specific column name ('TechID') in the input CSV
- Currently only supports the Enterprise ATT&CK domain
- Heat map is based solely on frequency, not effectiveness or importance

## References

- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
- [ATT&CK Navigator on GitHub](https://github.com/mitre-attack/attack-navigator)

## License

[Insert your license information here]
