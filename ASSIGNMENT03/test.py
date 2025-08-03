from LinearProbing import LinearProbingTable 

def run_tests():
    print("test")
    table = LinearProbingTable(capacity=4)

    print("✅ Test 1: Insert")
    assert table.insert("a", 1) == True
    assert table.insert("b", 2) == True
    assert table.insert("c", 3) == True
    assert table.insert("a", 99) == False  # duplicate key
    assert len(table) == 3
    print("Passed.")

    print("✅ Test 2: Search")
    assert table.search("a") == 1
    assert table.search("b") == 2
    assert table.search("x") == None
    print("Passed.")

    print("✅ Test 3: Modify")
    assert table.modify("a", 10) == True
    assert table.modify("b", 20) == True
    assert table.modify("x", 100) == False
    assert table.search("a") == 10
    assert table.search("b") == 20
    print("Passed.")

    print("✅ Test 4: Remove")
    assert table.remove("b") == True
    assert table.remove("x") == False
    assert table.search("b") == None
    assert len(table) == 2
    print("Passed.")

    print("✅ Test 5: Rehashing on Delete")
    table.insert("d", 4)
    table.insert("e", 5)
    table.insert("f", 6)  # Should trigger resize (capacity 8)
    assert table.search("d") == 4
    assert table.search("e") == 5
    assert table.search("f") == 6
    assert len(table) == 5
    print("Passed.")

    print("✅ Test 6: Capacity")
    cap = table.capacity()
    assert cap >= 8
    print(f"Current capacity is {cap}")
    print("Passed.")

    print("🎉 All tests passed!")

if __name__ == "__main__":
    run_tests()