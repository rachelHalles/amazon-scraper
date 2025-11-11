thonimport requests
from bs4 import BeautifulSoup

def parse_amazon_data(config):
    products = []

    for keyword in config['keywords']:
        url = f"https://www.amazon.com/s?k={keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        product_elements = soup.find_all('div', {'data-asin': True})
        for product_element in product_elements:
            product = {
                'title': product_element.find('span', {'class': 'a-text-normal'}).text,
                'url': f"https://www.amazon.com/dp/{product_element['data-asin']}",
                'price': product_element.find('span', {'class': 'a-price-whole'}).text if product_element.find('span', {'class': 'a-price-whole'}) else 'N/A',
                'reviewsCount': product_element.find('span', {'class': 'a-size-base'}).text if product_element.find('span', {'class': 'a-size-base'}) else 'N/A',
                'rating': product_element.find('span', {'class': 'a-icon-alt'}).text if product_element.find('span', {'class': 'a-icon-alt'}) else 'N/A',
                'seller': {
                    'name': product_element.find('span', {'class': 'a-size-small'}).text if product_element.find('span', {'class': 'a-size-small'}) else 'N/A',
                    'url': f"https://www.amazon.com/gp/help/seller/at-a-glance.html?seller={product_element['data-asin']}"
                },
                'images': [img['src'] for img in product_element.find_all('img', {'class': 's-image'})],
                'categories': ['Amazon Products']  # Static category for now
            }
            products.append(product)
    
    return products