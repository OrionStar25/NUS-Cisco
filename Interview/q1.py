s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "




s = s.lower()
new_string = ''


for c in s:
   if c.isalnum():
       new_string += c


if new_string == new_string[::-1]:
   print(True)
else:
   print(False)