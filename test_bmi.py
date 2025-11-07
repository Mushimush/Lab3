import Lab2.calculate_bmi as bmi

# The AAA pattern in Testing

# The Three Phases

# 1. Arrange 
# Set up the test conditions
# Prepare the input data and prerequisites

# 2. Act
# Call the function/method you want to test
# This is usually a single line

# Assert
# Verify the results
# Check the actual output matches the expected output
# Use assertions to confrm correctness

def test_bmi_normal_weight():
    #Arrange 
    height = 1.73
    weight = 57
    #Act
    result = bmi.calculate_bmi(height, weight)
    #Assert
    assert result == 0

def test_bmi_over_weight():
    #Arrange
    height = 1.73
    weight = 80
    #Act
    result = bmi.calculate_bmi(height, weight)
    #Assert
    assert result == 1

def test_bmi_under_weight():
    #Arrange
    height = 1.73
    weight = 50
    #Act
    result = bmi.calculate_bmi(height, weight)
    #Assert
    assert result == -1
