import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_with_10_or_more_elements():
    """Test that arrays with 10+ elements return 1"""

    # ARRANGE
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # ACT
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    # ASSERT - Testing ONE concept: size limit
    assert result == 1

def test_bubble_sort_with_empty_array():
    """Test that empty array is handled correctly"""

    # ARRANGE
    input_arr = []

    # ACT
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    # ASSERT - Testing ONE concept: empty array handling
    assert result == 0


def test_bubble_sort_with_non_integers():
    """Test that non-integer values return 2"""

    # ARRANGE
    input_arr = [64, 34, "hello", 12, 22, 11, 90]

    # ACT
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    # ASSERT - Testing ONE concept: non-integer handling
    assert result == 2
    