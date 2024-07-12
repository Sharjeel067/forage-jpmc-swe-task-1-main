import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, float(quote['top_bid']['price']))
      self.assertEqual(ask_price, float(quote['top_ask']['price']))
      self.assertEqual(price, float(quote['top_bid']['price']))  # Assuming price is set to bid_price

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, float(quote['top_bid']['price']))
      self.assertEqual(ask_price, float(quote['top_ask']['price']))
      self.assertEqual(price, float(quote['top_bid']['price']))  # Assuming price is set to bid_price


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    # Test cases for getRatio
    # Case where price_a and price_b are equal
    self.assertEqual(getRatio(100, 100), 1.0)

    # Case where price_a is greater than price_b
    self.assertEqual(getRatio(120, 100), 1.2)

    # Case where price_b is greater than price_a
    self.assertEqual(getRatio(100, 120), 0.8333333333333334)

    # Case where price_b is 0
    self.assertEqual(getRatio(100, 0), float('inf'))  # Assuming getRatio handles division by zero

    # Case where price_a is 0
    self.assertEqual(getRatio(0, 120), 0.0)  


if __name__ == '__main__':
    unittest.main()
