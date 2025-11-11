thonimport json
import os
from extractors.amazon_parser import parse_amazon_data
from outputs.exporters import export_to_json

def main():
    # Load configuration settings
    with open('src/config/settings.example.json', 'r') as file:
        config = json.load(file)

    # Get data based on provided configuration
    products = parse_amazon_data(config)

    # Export the scraped data to a JSON file
    export_to_json(products, 'data/sample.json')

if __name__ == '__main__':
    main()