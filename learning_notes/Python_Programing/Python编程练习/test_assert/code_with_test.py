
def rle(testString):
    result = ""
    if testString == "":
        return result
    
    previous_char = testString[:1]
    count = 1
    
    for char in testString[1:]:
        if char == previous_char:
            count += 1
        else:
            result = result + previous_char + str(count)
            previous_char = char
            count = 1
    result = result + previous_char + str(count)
    
    return result

def Assert(actual,expected, message):
    if(actual ==  expected):
        print("PASSED: ", message, ": Actual %s == Expected %s" % (actual, expected));
    else:
        print("FAILED: ", message, ": Actual %s != Expected %s" % (actual, expected));

def doTestsPass():
    Assert(rle("aaa"),        "a3",           "Example 1" );
    Assert(rle("aabbc"),      "a2b2c1",       "Example 5" );

if __name__ == "__main__":
    doTestsPass()