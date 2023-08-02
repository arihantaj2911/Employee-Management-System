print("Enter a Character")
c=input()
if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
    print("Vowel")
elif((c>='A' and c<='Z') or (c>='a' and c<='z')):
    print("Consonant")
else:
    print("Invalid Input")
    
