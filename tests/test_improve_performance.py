# tests/test_improve_performance.py
"""
Test Coderpad exercise that asks to improve the quality of the code so it runs in milliseconds
"""
import time
from coderpad.improve_performance import generate_random_list

def test_small_batch_generate_random_list():
    """
    Test that a small batch takes less than 100ms
    """
    start = time.time()
    generate_random_list(100)
    test_time = (time.time() - start) * 1000
    # print(f'Small test took {test_time:.1f} ms')
    assert test_time < 100, 'Too slow!'

def test_large_batch_generate_random_list():
    """
    Test that a large batch takes less than 100ms
    """
    start = time.time()
    generate_random_list(20000)
    test_time = (time.time() - start) * 1000
    # print(f'Large test took {test_time:.1f} ms')
    assert test_time < 100, 'Too slow!'
    