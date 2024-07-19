import pytest
import os

path = str(os.getcwd())
tests = os.listdir(path)
remove = [i for i in tests if i.title() in ['Starttests.Py', '__Pycache__', '.Pytest_Cache']]
for i in remove:
    tests.remove(i)

def run_tests():
    for i in tests:
        test = str(path + "\\" + i)
        if pytest.main([test]) == 1:
            print(f"{i.title()} Tests failed.")
        else:
            print(f"{i.title()} Tests passed.")

if __name__ == '__main__':
    run_tests()
    print("Ran tests for ", tests)
