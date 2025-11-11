thonimport json

def export_to_json(data, filename):
    """Export the extracted data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)