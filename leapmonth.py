import sys

def main():
    if len(sys.argv) < 3:
        print('illigal inputs; usage: python leapmonth.py year month')
        return
    if not sys.argv[1].isdecimal() or not sys.argv[2].isdecimal():
        print('illigal inputs; usage: python leapmonth.py year month')
        return

    year = int(sys.argv[1])
    month = int(sys.argv[2])

    if year <= 1:
        print('illigal inputs; usage: python leapmonth.py year month')
        return
    if month <= 0 or 13 <= month:
        print('illigal inputs; usage: python leapmonth.py year month')
        return
    days = 0
    if month == 2:
        if year%400 == 0:
            days = 29
        elif year%4 == 0 and year%100 != 0:
            days = 29
        else:
            days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    else:
        days = 31
    print("Month of ", month, "/", year, " has ", days, " days.", sep="")

if __name__ == '__main__':
    main()
