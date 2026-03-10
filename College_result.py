# Teachers enter marks, calculate GPA and display results for students.

class Result:

    def __init__(self):
        self.name = input("Enter student name: ")
        self.marks = []
        self.total_subjects = int(input("Enter total number of subjects: "))

    def input_marks(self):
        for i in range(self.total_subjects):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(mark)

    def calculate_gpa(self):
        total_marks = sum(self.marks)
        gpa = total_marks / self.total_subjects
        return gpa

    def display_result(self):
        gpa = self.calculate_gpa()
        print("\n----- Student Result -----")
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("GPA:", gpa)


# Create Object
result = Result()

# Call Methods
result.input_marks()
result.display_result()