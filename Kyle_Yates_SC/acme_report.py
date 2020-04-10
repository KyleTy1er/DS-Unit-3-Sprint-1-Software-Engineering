from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'UNSCENTED_CANDLE']


def generate_products(num_products=30):
    products = []
    for item in range(num_products):
      noun = sample(NOUNS,1)
      adjective = sample(ADJECTIVES,1)
      prod_name = (adjective[0] + " ", noun[0])
      item_flammability = uniform(0.0, 2.5)
      item_price = randint(5, 100)
      item_weight = randint(5, 100)
      product = Product(prod_name, price=item_price, 
                        weight=item_weight,
                        flammability=item_flammability)
      
      products.append(product)

    return products


def inventory_report(products):
  print ("ACME CORPORATION OFFICIAL INVENTORY REPORT")

  total_item_price = 0
  total_item_weight = 0
  total_item_flammability = 0


  for product in products:
      total_item_price = total_item_price + product.price
      total_item_weight = total_item_weight + product.weight
      total_item_flammability = total_item_flammability + product.flammability

  print('Unique product names:',len(products))
  print('Average price:',total_item_price/len(products))
  print ('Average weight:',total_item_weight/len(products))
  print ('Average flammability:',total_item_flammability/len(products))
  pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
  inventory_report(generate_products())