
# student has features like name,roll and subjects with marks.There are 5 sub for every student with some marks .
# Stu has operation which will dispay % of the stu (use dict for sub and marks)

class Student:
    def __init__(self,nm,r,sub={}):
        self.name=nm
        self.roll_no=r
        self.subjects=sub

    def calc_Percentage(self):
        total_marks=sum(self.subjects.values())
        no_of_sub=len(self.subjects)
        percentage=total_marks/((no_of_sub)*100)*100
        return percentage
    
    def display_info(self):
        print(f"Name of student is : {self.name}")
        print(f"Roll of student is : {self.roll_no}")
        print(f"--Marks of student in each subject--")
        for subject,mark in self.subjects.items():
            print(f"{subject} : {mark}")
        print(f"Percentage of student = {self.calc_Percentage():.2f}%")

s1=Student("Abhi",101,{"Eng":65,"Maths":55,"Science":88,"Hindi":75})
s1.display_info()
print("<-------------------------------------------->")
s2=Student("Sanika",102,{"Eng":90,"Maths":75,"Science":88,"Hindi":85})
s2.display_info()
print("<-------------------------------------------->")
s3=Student("Sakshi",103,{"Eng":88,"Maths":75,"Science":80,"Hindi":67})
s3.display_info()


# Output

# Name of student is : Abhi
# Roll of student is : 101
# Eng : 65
# Maths : 55
# Science : 88
# Hindi : 75
# Percentage of student = 71.00%
# <-------------------------------------------->
# Name of student is : Shruti
# Roll of student is : 102
# Eng : 90
# Maths : 75
# Science : 88
# Hindi : 85
# Percentage of student = 87.00%
# <-------------------------------------------->
# Name of student is : Manasi
# Roll of student is : 103
# Eng : 88
# Maths : 75
# Science : 80
# Hindi : 67
# Percentage of student = 80.00%
