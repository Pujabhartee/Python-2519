# Tution Discount Calculations
student_name = input("Enter name of the student: ")
student_grade_level = int(input("Enter the grade level of the student (1-12): "))
student_topper_status = input("Is the student is academically good (Yes/No): ")
match student_grade_level:
    case 1 | 2 | 3:
        student_base_fee = float(input("Enter the base tution fee for grade level 1-3: "))
    case 4 | 5 | 6:
        student_base_fee = float(input("Enter the base tution fee for grade level 4-6: "))
    case 7 | 8:
        student_base_fee = float(input("Enter the base tution fee for grade level 7-8: "))
    case 9 | 10:
        student_base_fee = float(input("Enter the base tution fee for grade level 9-10: "))
    case _:
        student_base_fee = float(input("Enter the base tution fee for grade level 11-12: "))

if student_grade_level >= 9:
    if student_topper_status == "Yes":
        discount_rate = 0.20
    else:
        discount_rate = 0.10
elif student_grade_level >= 6:
    discount_rate = 0.05
else:
    discount_rate = 0.00

if student_grade_level == 12:
    add_discount_rate = 0.05
elif student_grade_level == 10:
    add_discount_rate = 0.03
else:
    add_discount_rate = 0.00


total_dicount_rate = discount_rate + add_discount_rate
total_discount_amount = student_base_fee * total_dicount_rate
final_tution_fee = student_base_fee - total_discount_amount

print("------------------------------")
print(f"Student Name: {student_name} ---- Grade level: {student_grade_level} ---- Base tuttion fee: {student_base_fee}")
print(f"Academic topper status: {student_topper_status}")
print(f"Total discount percentage: {int(total_dicount_rate*100)}% --- Total discount amount: {total_discount_amount}")
print(f"Final tution fee after discount: {final_tution_fee}")
print("------------------------------")     