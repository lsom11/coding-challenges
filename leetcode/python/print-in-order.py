class Foo(object):
    def __init__(self):
        self.second_cv = threading.Event() 
        self.third_cv = threading.Event()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_cv.set()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.second_cv.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_cv.set()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        self.third_cv.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()