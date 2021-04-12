# Problema 19
import time
start_time = time.time()
days = ['M', 'T', 'W', 'Th', 'F', 'St', 'S']
numberDays = 0
pos = 1 # 1 de gener de 1901 era dimarts
count = 0

for year in range(1901, 2000 + 1):
    for month in range(1, 12 + 1):
        if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
            numberDays = 31
        if (month == 4) or (month == 6) or (month == 9) or (month == 11):
            numberDays = 30
        if month == 2:
            if (str(year)[2] and str(year)[3]) == 0:
                if year % 400 == 0:
                    numberDays = 29
            else:
                if year % 4 == 0:
                    numberDays = 29
                else:
                    numberDays = 28
        # Començant pel dia 1 de cada mes anem sumant de setmana en setmana fins que el dia calculat siga superior al
        # nombre de dies del mes en qüestió. Després calculem la diferència entre l'últim dia calculat dins del mes i el
        # dia final del mes (offset). En funció del dia de la setmana en que va començar el mes (pos) i el offset
        # calculem el dia que comença el mes següent
        i = 1
        while i < numberDays:
            i += 7
        i -= 7
        offset = numberDays - i
        if pos + offset + 1 >= 7:
            if (pos + offset + 1) - 7 >= 7:
                dayLetters = days[(pos + offset + 1) - 7 - 7]
                pos += offset + 1 - 7 - 7
            else:
                dayLetters = days[(pos + offset + 1) - 7]
                pos += offset + 1 - 7
        else:
            dayLetters = days[pos + offset + 1]
            pos += offset + 1
        if dayLetters == 'S':
            count += 1
print(count)
print("Execution time: ", time.time() - start_time, "s")
