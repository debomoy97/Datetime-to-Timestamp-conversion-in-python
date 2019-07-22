from datetime import datetime
time = input()
tex=[
      '%b %d, %Y, %H:%M %p IST', #Jul 03, 2019, 16:09 PM IST
      '%m/%d/%y %H:%M:%S', #09/19/18 13:55:26
      '%d %b %Y, %H:%M', #9 Jul 2019, 12:45
      '%m-%d-%Y',#09-19-2018
      '%d-%b-%Y %H:%M:%S', #20-JUN-1990 08:03:00
      '%a %b %d %H:%M:%S %Y', #Wed Sep 19 14:55:02 2018
      '%d-%B-%Y %A', #10-Dezember-2018 Montag
      '%B %d, %Y', #July 3, 2019
      '%b %d, %Y', #Jul 03, 2019
      '%d %b %Y, %H%M hrs IST', #9 Jul 2019, 1245 hrs IST
      '%Y-%m-%d %H:%M:%S.%f', #2019-07-15 17:01:38.0
      '%d-%m-%Y', #15-05-2019
      '%d-%b-%Y' #17-Jul-2019
      ]
for j in range(len(tex)):
    try:
        d = datetime.strptime(time.strip(),tex[j])
        #d = datetime.strptime(time.strip(),tex[3])
        break
    except ValueError:
        continue

stamp = datetime.timestamp(d)

print(stamp)
