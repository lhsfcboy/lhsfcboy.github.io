"""
连续标签数据汇总

"""




def summarize_data(data):
    result = []
    if not data:
        return result
    
    current_label = data[0][0]
    current_sum = data[0][1]
    
    for label, value in data[1:]:
        if label == current_label:
            current_sum += value
        else:
            result.append((current_label, current_sum))
            current_label = label
            current_sum = value
    
    result.append((current_label, current_sum))
    
    return result

def test_summarize_data():
    assert summarize_data([]) == [], "Test Case 1 Failed: Empty data should return empty list"
    assert summarize_data([('A', 1)]) == [('A', 1)], "Test Case 2 Failed: Single data point"
    assert summarize_data([('A', 1), ('B', 2), ('C', 3)]) == [('A', 1), ('B', 2), ('C', 3)], "Test Case 3 Failed: No consecutive duplicates"
    assert summarize_data([('A', 1), ('A', 2), ('A', 3)]) == [('A', 6)], "Test Case 4 Failed: All same label"
    assert summarize_data([('A', 1), ('A', 2), ('B', 1), ('A', 1)]) == [('A', 3), ('B', 1), ('A', 1)], "Test Case 5 Failed: Consecutive duplicates mixed with single occurrences"
    assert summarize_data([('A', 1), ('A', 2), ('A', 3), ('B', 1)]) == [('A', 6), ('B', 1)], "Test Case 6 Failed: Consecutive duplicates ending with a different label"
    assert summarize_data([('A', 1), ('A', 2), ('B', 1), ('B', 1), ('C', 1), ('A', 1), ('A', 1)]) == [('A', 3), ('B', 2), ('C', 1), ('A', 2)], "Test Case 7 Failed: Long list with various patterns"
    assert summarize_data([('A', 1), ('B', 1), ('B', 2), ('C', 1), ('A', 2), ('A', 1)]) == [('A', 1), ('B', 3), ('C', 1), ('A', 3)], "Test Case 8 Failed: Changing patterns"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_summarize_data()
