#calender month
terminate = False
while not terminate:

  month = int(input('enter month 1-12(-1 to quit):'))

  if month == -1:
    terminate = True
  else:
      while month<1 or month>12:
        month = int(input('invalid input - enter month 1-12 :'))

      year = int(input('enter year(yyyy) :'))

      while year < 1800 or year > 2099:
       year = int(input('invalid year- enter year (1800 - 2099):'))

      #detemine to leap year
      if (year%4==0) and (not(year%100 ==0) or (year%400 == 0)):
             leap_year = True
      else:
             leap_year = False

      #determine num of days in month
      if month in (1,3,5,7,8,10,12):
          num_days_in_month = 31
      elif month in (4,6,9,11):
          num_days_in_month = 30
      elif leap_year: #febuaury
          num_days_in_month = 29
      else:
          num_days_in_month = 28

      #detetmine the day of the week
      century_digits = year//100
      year_digits = year%100

      valve = year_digits + (year_digits//4)
      if century_digits == 18:
          valve = valve+2
      elif century_digits == 20:
          valve = valve + 6

      if month == 1 and not leap_year:
          valve = valve + 1
      elif month == 2:
          if leap_year:
              valve = valve+3
          else:
              valve = valve+4
      elif month == 3 or month == 11:
         valve  = valve+4
      elif month == 5:
          valve = valve +2
      elif month == 6:
          valve = valve+5
      elif month ==8:
          valve = valve +3
      elif month == 9 or month ==12:
          valve = valve + 6
      elif month == 10:
          valve = valve+1

      day_of_week = (valve+1)%7  # 1- sun ,2-mon ,,,,,,0-sat
      #determine month name
      if month==1:
         month_name = 'january'
      elif month==2:
         month_name = 'february'
      elif month==3:
          month_name = 'march'
      elif month==4:
          month_name = 'april'
      elif month==5:
          month_name = 'may'
      elif month==7:
          month_name = 'june'
      elif month==8:
          month_name = 'july'
      elif month==9:
          month_name = 'august'
      elif month==10:
          month_name = 'september'
      elif month==11:
          month_name = 'november'
      elif month==12:
          month_name = 'december'


      print('\n', ' ' + month_name,year)

      #display rows of dates
      if day_of_week == 0:
          starting_col = 7
      else:
          starting_col = day_of_week

      current_col = 1
      column_widht = 4
      blank_char = ' '
      blank_column = format(blank_char,str(column_widht))

      while current_col<=starting_col:
          print(blank_column,end='')
          current_col = current_col+1

      current_day = 1

      while current_day<=num_days_in_month:
          if current_day<10:
              print(format(blank_char,'3') + str(current_day),end='')
          else:
              print(format(blank_char,'2') + str(current_day),end='')

          if current_col<= 7:
                  current_col = current_col +1
          else:
               current_col = 1
               print()

          current_day = current_day +1

      print('\n')