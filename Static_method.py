class student(object):
    fees_balance = 0
    def __init__(self):
        self.fees = 3000
        student.fees_balance+=1

    @staticmethod

    def fees_info():
        print student.fees_balance,"$ balance fee"


student.fees_info()        
fee1=student()
student.fees_info()
fee2=student()
student.fees_info()
