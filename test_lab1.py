def increment_by_one(i):
    return i + 1
    
def test_answer_increment():
    assert increment_by_one(1) == 2

def decrement_by_one(i):
    return i - 1

def test_answer_decrement():
    assert decrement_by_one(2) == 1