# colors = ["red","green","blue","black","white"]

# for i in colors:
#     print(i)
    
# text_th = "สวัสดีครับ"
# for i in text_th:
#     print(f"{i} , end = " "")
exe="========================="
print(exe)
print("เครื่่องคิดเลข")
# รับตัวเลข
a = int(input("ใส่ตัวเลขแรก : "))
b = int(input("ใส่ตัวเลขที่สอง : "))
print(exe)
# แสดงตัวเลือกการคำนวณ
print("\nเลือกการดำเนินการ : ")
print("1.บวก (+)")
print("2.ลบ (-)")
print("3.คูณ (*)")
print("หาร (/)")
print("ยกกำลัง (**)")
# รับตัวเลือก
choice = input("กรุณาเลือก 1/2/3/4/5 : ")
print(exe)
if choice == '1':
    result = a + b 
    print(f"ผลลัพธ์ : {a}+{b} = {result}")
elif choice == '2':
    result = a - b 
    print(f"ผลลัพธ์ : {a}-{b} = {result}")
elif choice == '3':
    result = a * b
    print(f"ผลลัพธ์ : {a}*{b} = {result}")
elif choice == '4':
    if b == 0:
        print("ข้อผิดพลาด : ไม่สามารถหารด้วย 0 ได้")
    else:
        result = a / b
        print(f"ผลลัพธ์ : {a}/{b} = {result}")
elif choice == '5':
    result = a ** b
    print(f"ผลลัพธ์ : {result}")
    





    
