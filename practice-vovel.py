vowels={
    "A":0,
    "E":0,
    "I":0,          
    "O":0,
    "U":0,      
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
with open(r"C:\Users\CHAUDHARY SOHAIL\OneDrive\Documents\python-pract\p.py") as file:
    content=file.read()
    for char in content:
        if char in vowels:
            vowels[char]+=1
for vowel,count in vowels.items():
    print(f"{vowel}: {count}")

    match=0
science=0       
english=0
list1=["math","science","english"]
print("Enter marks for 3 subjects:")    
for i in range(0,3):
    marks= int(input(f"enter you marks of subject {list1[i]}: "))
    if i==0:
        math =marks
    elif i==1:
        science=marks
    else:
        english=marks
total=math+science+english
average=total/3
print("---------------------")
print(f"Total your Marks: {total}")
print(f"Total Marks average : {average}")

print("Overall grade:")
print("---------------------")
if average>=90 and average<=100:            
    print("Grade: A+")
elif average>=80 and average<90:
    print("Grade: A")
elif average>=70 and average<80:
    print("Grade: B")
elif average>=60 and average<70:
    print("Grade: C")
elif average>=50 and average<60:
    print("Grade: D")
elif average<50:
    print("Grade: F")
else:
    print("Invalid average marks")