import price_info

print("Test_price_info")


def test_total_cost_shopping():
    # Arrange
    # Based on the dictionaries in price_info.py:
    # apple: 5 * 1.20 = 6.00
    # orange: 5 * 1.40 = 7.00
    # watermelon: 1 * 6.50 = 6.50
    # pineapple: 2 * 2.70 = 5.40
    # pear: 10 * 0.90 = 9.00
    # papaya: 1 * 2.95 = 2.95
    # pomegranate: 2 * 4.95 = 9.90
    # Total = 46.75
    expected_result = 46.75

    # Act
    result = price_info.total_cost_shopping()

    # Assert
    assert result == expected_result


def test_cost_of_fruits():
    # Arrange
    fruit_name = 'apple'
    quantity = 10
    expected_result = 12.0

    # Act
    result = price_info.cost_of_fruits(fruit_name, quantity)

    # Assert
    assert result == expected_result
