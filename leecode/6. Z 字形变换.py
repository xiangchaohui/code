s = "PAYPALISHIRING"

numRows=4
n = len(s)
col_num = int(n / (numRows - 1))
last_num = n % (numRows-1)

data = []
jo = 1
for i in range(col_num):
    for j in range(numRows - 1):
        str1 = s[i * (numRows - 1):(i + 1) * (numRows - 1)] + ' '
    if jo == 1:
        data.append(str1)
        jo = -jo
    else:
        data.append(str1[::-1])
        jo = -jo

str1 = s[(i+1) * (numRows - 1):(i+2)* (numRows - 1) + last_num] + ''.join(' ' for i in range(numRows - last_num))
if jo == 1:
    data.append(str1)
else:
    data.append(str1[::-1])

data_str = ['' for i in range(numRows)]
for i in data:
    for j in range(numRows):
        data_str[j] = data_str[j] + i[j]

str1 = ''.join(i for i in data_str)
str1 = ''.join([i for i in str1 if i != ' '])

print(str1)