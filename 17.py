# Problema 17
import time
start_time = time.time()
units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
t10_19 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
sum = 0

for i in range(1, 1000 + 1):
    num_let = ''
    num = str(i)
    if len(num) == 4:
        num_let += units[int(num[0])-1] + 'thousand'
    if len(num) >= 3:
        if int(num[len(num)-3]) > 0:
            num_let += units[int(num[len(num)-3])-1] + 'hundred'
            if int(num[len(num)-2]) or int(num[len(num)-1]):
                num_let += 'and'
    if len(num) >= 2:
        if int(num[len(num)-2]) > 1:
            num_let += tens[int(num[len(num)-2])-2]
        else:
            if int(num[len(num)-2]) != 0:
                num_let += t10_19[int(num[len(num) - 1])]
    if len(num) >= 1:
        if not(1 >= int(num[len(num) - 2]) > 0 and len(num) >= 2) and int(num[len(num) - 1]) != 0:
            num_let += units[int(num[len(num) - 1])-1]
    sum += len(num_let)
print(sum)
print("Execution time: ", time.time() - start_time, "s")
