# Write a function to be tested
def add(a, b):
    return a-b

# Write the test
def test_add():
    #Assert is a keyword used to make a statement of expectation
    assert add(2, 3)==5
    assert add('space', 'sheep')=='spacesheep'