
command = input("Type encrypt for encryption and decrypt for decryption:")
text = input("enter the text:\n").upper()
n = int((input("enter the shift key:\n")))
converted_n = int(n)
lis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z"]
lis2 = []
lis3 = []
lis4 = []

for n in text:
    lis2.extend(n)
for i, y in enumerate(lis):
    for j, z in enumerate(lis2):
     if y == z:
      lis3.append(i)
for o in lis3:
     if command == "encrypt":
       encrypted_index = int((o + converted_n) % 26)
lis4.append(lis[encrypted_index])
if command == "decrypt":
    decrypted_index = int((o - converted_n) % 26)
lis4.append(lis[decrypted_index])
for g in lis4:
    print(g, end=" ")