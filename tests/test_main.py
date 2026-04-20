import unittest
from src.main import calculate_total_cost


class TestCalculateTotalCost(unittest.TestCase):
    
    def test_empty_list(self):
        """Test that empty list returns 0.0"""
        result = calculate_total_cost([])
        self.assertEqual(result, 0.0)
    
    def test_single_item_no_discount(self):
        """Test single item under discount threshold"""
        items = [{'price': 10.0, 'quantity': 2}]
        # subtotal = 20, no discount, tax = 1.6, total = 21.6
        result = calculate_total_cost(items)
        self.assertAlmostEqual(result, 21.6, places=2)
    
    def test_single_item_with_discount(self):
        """Test single item over discount threshold"""
        items = [{'price': 60.0, 'quantity': 2}]
        # subtotal = 120, discount = 108, tax = 8.64, total = 116.64
        result = calculate_total_cost(items)
        self.assertAlmostEqual(result, 116.64, places=2)
    
    def test_multiple_items_no_discount(self):
        """Test multiple items under discount threshold"""
        items = [
            {'price': 15.0, 'quantity': 2},
            {'price': 25.0, 'quantity': 1},
            {'price': 10.0, 'quantity': 3}
        ]
        # subtotal = 30 + 25 + 30 = 85, no discount, tax = 6.8, total = 91.8
        result = calculate_total_cost(items)
        self.assertAlmostEqual(result, 91.8, places=2)
    
    def test_multiple_items_with_discount(self):
        """Test multiple items over discount threshold"""
        items = [
            {'price': 50.0, 'quantity': 1},
            {'price': 30.0, 'quantity': 2},
            {'price': 20.0, 'quantity': 1}
        ]
        # subtotal = 50 + 60 + 20 = 130, discount = 117, tax = 9.36, total = 126.36
        result = calculate_total_cost(items)
        self.assertAlmostEqual(result, 126.36, places=2)
    
    def test_exactly_100_threshold(self):
        """Test subtotal exactly at discount threshold"""
        items = [{'price': 50.0, 'quantity': 2}]
        # subtotal = 100, no discount (not > 100), tax = 8, total = 108
        result = calculate_total_cost(items)
        self.assertAlmostEqual(result, 108.0, places=2)
    
    def test_just_over_100_threshold(self):
        """Test subtotal just over discount threshold"""
        items = [{'price': 50.5, 'quantity': 2}]
        # subtotal = 101, discount = 90.9, tax = 7.272, total = 98.172
        result = calculate_total_cost(items)
        self.assertAlmostEqual(result, 98.172, places=3)
    
    def test_zero_price_items(self):
        """Test items with zero price"""
        items = [
            {'price': 0.0, 'quantity': 5},
            {'price': 10.0, 'quantity': 1}
        ]
        # subtotal = 0 + 10 = 10, no discount, tax = 0.8, total = 10.8
        result = calculate_total_cost(items)
        self.assertAlmostEqual(result, 10.8, places=2)
    
    def test_zero_quantity_items(self):
        """Test items with zero quantity"""
        items = [
            {'price': 100.0, 'quantity': 0},
            {'price': 20.0, 'quantity': 2}
        ]
        # subtotal = 0 + 40 = 40, no discount, tax = 3.2, total = 43.2
        result = calculate_total_cost(items)
        self.assertAlmostEqual(result, 43.2, places=2)


if __name__ == '__main__':
    unittest.main()