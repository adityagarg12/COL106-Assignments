from heap import Heap
import random

def test_heap():
    print("Testing Min-Heap:")
    # Test Min-Heap
    min_heap = Heap(lambda x, y: x < y, [4, 10, 3, 5, 1])
    
    # Initial heap should be [1, 4, 3, 10, 5] if min-heap property is correct
    assert min_heap.top() == 1, "Test Failed: Top element should be 1"
    
    # Insert elements and check the top
    min_heap.insert(0)
    assert min_heap.top() == 0, "Test Failed: Top element should be 0 after inserting 0"
    
    # Extract elements and ensure the heap maintains the min-heap property
    assert min_heap.extract() == 0, "Test Failed: Extracted element should be 0"
    assert min_heap.top() == 1, "Test Failed: Top element should be 1 after extraction"
    
    assert min_heap.extract() == 1, "Test Failed: Extracted element should be 1"
    assert min_heap.extract() == 3, "Test Failed: Extracted element should be 3"
    assert min_heap.extract() == 4, "Test Failed: Extracted element should be 4"
    assert min_heap.extract() == 5, "Test Failed: Extracted element should be 5"
    assert min_heap.extract() == 10, "Test Failed: Extracted element should be 10"
    
    # Edge case: extracting from an empty heap should raise an error
    # min_heap.extract()
        # assert False, "Test Failed: Extracting from empty heap should raise an error"
    # except IndexError:
        # print("Test Passed: Empty heap extraction raised IndexError as expected.")
    
    # Test inserting into an empty heap
    min_heap.insert(2)
    assert min_heap.top() == 2, "Test Failed: Top element should be 2 after inserting into empty heap"
    min_heap.insert(1)
    assert min_heap.top() == 1, "Test Failed: Top element should be 1 after inserting 1"
    print("Min-Heap tests passed.\n")

    print("Testing Max-Heap:")
    # Test Max-Heap
    max_heap = Heap(lambda x, y: x > y, [4, 10, 3, 5, 1])
    
    # Initial heap should be [10, 5, 3, 4, 1] if max-heap property is correct
    assert max_heap.top() == 10, "Test Failed: Top element should be 10"
    
    # Insert elements and check the top
    max_heap.insert(15)
    assert max_heap.top() == 15, "Test Failed: Top element should be 15 after inserting 15"
    
    # Extract elements and ensure the heap maintains the max-heap property
    assert max_heap.extract() == 15, "Test Failed: Extracted element should be 15"
    assert max_heap.top() == 10, "Test Failed: Top element should be 10 after extraction"
    
    assert max_heap.extract() == 10, "Test Failed: Extracted element should be 10"
    assert max_heap.extract() == 5, "Test Failed: Extracted element should be 5"
    assert max_heap.extract() == 4, "Test Failed: Extracted element should be 4"
    assert max_heap.extract() == 3, "Test Failed: Extracted element should be 3"
    assert max_heap.extract() == 1, "Test Failed: Extracted element should be 1"
    
    # Edge case: extracting from an empty heap should raise an error
    # try:
    max_heap.extract()
        # assert False, "Test Failed: Extracting from empty heap should raise an error"
    # except IndexError:
    #     print("Test Passed: Empty heap extraction raised IndexError as expected.")
    
    # Test inserting into an empty heap
    max_heap.insert(20)
    assert max_heap.top() == 20, "Test Failed: Top element should be 20 after inserting into empty heap"
    max_heap.insert(10)
    assert max_heap.top() == 20, "Test Failed: Top element should still be 20"
    
    print("Max-Heap tests passed.\n")

    print("Testing Performance on Large Input:")
    # Test with large input (1000 elements)
    large_heap = Heap(lambda x, y: x < y, list(range(1000, 0, -1)))  # Min-heap
    
    assert large_heap.top() == 1, "Test Failed: Top element should be 1 for large input"
    
    for i in range(1, 1001):
        assert large_heap.extract() == i, f"Test Failed: Extracted element should be {i}"
    
    print("Large input test passed.\n")

# Run the tests
test_heap()


def validate_heap_property(heap, comparator):
    ''' 
    Validates that the heap property holds for all elements 
    '''
    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(heap) and comparator(heap[left], heap[i]):
            print(f"Heap property violated between index {i} ({heap[i]}) and left child {left} ({heap[left]})")
            return False

        if right < len(heap) and comparator(heap[right], heap[i]):
            print(f"Heap property violated between index {i} ({heap[i]}) and right child {right} ({heap[right]})")
            return False
    
    return True


def stress_test_heap():
    print("Running Complex and Intensive Heap Tests...")
    
    # 1. Random Inserts and Extracts
    print("Test 1: Random Inserts and Extracts on Min-Heap")
    random_values = [random.randint(0, 1000) for _ in range(1000)]
    min_heap = Heap(lambda x, y: x < y, random_values[:500])
    
    # Validate the heap after initialization
    assert validate_heap_property(min_heap._data, min_heap.comparator), "Heap property violated after initialization"

    # Insert 500 random elements and validate the heap property
    for val in random_values[500:]:
        min_heap.insert(val)
        assert validate_heap_property(min_heap._data, min_heap.comparator), "Heap property violated after insert"
    
    # Perform random extract operations and validate heap property
    for _ in range(400):
        extracted = min_heap.extract()
        assert validate_heap_property(min_heap._data, min_heap.comparator), "Heap property violated after extract"
    
    print("Test 1 passed.")
    
    # 2. Random Inserts, Extracts, and Duplicates
    print("Test 2: Handling Duplicates")
    duplicates = [random.randint(0, 50) for _ in range(500)]
    min_heap = Heap(lambda x, y: x < y, duplicates)
    
    # Validate heap property with duplicates
    assert validate_heap_property(min_heap._data, min_heap.comparator), "Heap property violated with duplicates"
    
    # Insert more duplicates and validate the heap
    for _ in range(100):
        duplicate_val = random.randint(0, 50)
        min_heap.insert(duplicate_val)
        assert validate_heap_property(min_heap._data, min_heap.comparator), "Heap property violated after inserting duplicates"
    
    # Extract and check for correct behavior with duplicates
    while len(min_heap._data) > 0:
        extracted = min_heap.extract()
        assert validate_heap_property(min_heap._data, min_heap.comparator), "Heap property violated during extraction of duplicates"
    
    print("Test 2 passed.")
    
    # 3. Max-Heap Random Inserts and Extracts
    print("Test 3: Random Inserts and Extracts on Max-Heap")
    random_values = [random.randint(0, 1000) for _ in range(1000)]
    max_heap = Heap(lambda x, y: x > y, random_values[:500])
    
    # Validate the heap after initialization
    assert validate_heap_property(max_heap._data, max_heap.comparator), "Heap property violated after initialization"

    # Insert 500 random elements and validate the heap property
    for val in random_values[500:]:
        max_heap.insert(val)
        assert validate_heap_property(max_heap._data, max_heap.comparator), "Heap property violated after insert"
    
    # Perform random extract operations and validate heap property
    for _ in range(400):
        extracted = max_heap.extract()
        assert validate_heap_property(max_heap._data, max_heap.comparator), "Heap property violated after extract"
    
    print("Test 3 passed.")
    
    # 4. Edge Case: Single Element
    print("Test 4: Edge Case with Single Element")
    single_heap = Heap(lambda x, y: x < y, [10])
    assert single_heap.top() == 10, "Top element should be 10"
    
    # Insert and extract single element
    single_heap.insert(20)
    assert single_heap.top() == 10, "Top element should still be 10 after inserting 20"
    
    extracted = single_heap.extract()
    assert extracted == 10, "Extracted element should be 10"
    assert single_heap.top() == 20, "Top element should now be 20"
    
    extracted = single_heap.extract()
    assert extracted == 20, "Extracted element should be 20"
    
    print("Test 4 passed.")
    
    print("All stress tests passed.")
    
# Run stress tests
stress_test_heap()
