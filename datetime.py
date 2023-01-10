from datetime import datetime

date_time_str_test = "22/12/01"

date_time_obj_test = datetime.strptime(date_time_str_test, '%y/%m/%d').date()

print(date_time_obj_test)
