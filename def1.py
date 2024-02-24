inc = float(input("ระบุรายได้ (บาท): "))
if inc >= 15000 and inc < 20000:
    type = "บัตร Sliver"
elif inc < 100000:
    type = "บัตร Gold"
else:
    type = "บัตร Platinum"
print(f"สามารถทำ{type} ได้")
