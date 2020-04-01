import unittest
'''
单元测试
'''
def add_and_multiply(x,y):
    addition = x + y
    mutiple = multiply(x,y)
    return (addition,mutiple)

def multiply(x,y):
    return 2*x*y

class Test_add_and_multiply(unittest.TestCase):
    def test_one(self):
        x=3
        y=5
        addition,mutiple = add_and_multiply(x,y)
        self.assertEqual(8,addition)
        self.assertEqual(15,mutiple)

if __name__ == '__main__':
    unittest.main()






