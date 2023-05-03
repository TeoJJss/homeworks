str1 = "John_doe&2023@app.newworld2k"
char=digit=symbol=0

for i in str1:
    if i.isalpha():
        char+=1
    elif i.isnumeric():
        digit+=1
    else:
        symbol+=1

print(f"Chars = {char}\nDigits = {digit}\nSymbol = {symbol}")