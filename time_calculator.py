import math


def many_days_later(start_day, added_days):
  days_dict = {
    "sunday": 1,
    "monday": 2,
    "tuesday": 3,
    "wednesday": 4,
    "thursday": 5,
    "friday": 6,
    "saturday": 7
  }
  start_day = start_day.lower()

  for days_name, num in days_dict.items():
    start_day = start_day.replace(days_name.lower(), str(num))
  start_day = int(start_day)
  start_day += int(added_days)
  if start_day > 6:
    weeks = math.floor(start_day / 7)
    start_day -= 7 * weeks
  start_day = str(start_day)
  for days_name, num in days_dict.items():
    start_day = start_day.replace(str(num), days_name.capitalize())
  return start_day


def add_time(start, added, start_day=""):
  extra_hour = 0

  start_time = start.split(":")
  hh = int(start_time[0])
  mm_ampm = start_time[1].split(" ")
  mm = int(mm_ampm[0])
  ampm = mm_ampm[1]
  if ampm == "PM":
    hh += 12

  start_time = str(hh) + ":" + str(mm)

  added_time = added.split(":")
  added_hh = int(added_time[0])
  added_mm = int(added_time[1])

  mm += added_mm
  if mm >= 60:
    mm -= 60
    extra_hour = 1
  mm_string = str(mm)
  if len(str(mm)) < 2:
    mm_string = "0" + str(mm)

  total_hh = hh + added_hh + extra_hour
  days_added = 0
  if total_hh > 23:
    days_added = math.floor(total_hh / 24)
    total_hh = total_hh - (days_added * 24)

  if total_hh == 12:
    ampm = "PM"
  elif total_hh > 12:
    ampm = "PM"
    total_hh -= 12
  elif total_hh == 0:
    ampm = "AM"
    total_hh += 12
  else:
    ampm = "AM"
  days_later = ""
  if days_added == 1:
    days_later = " (next day)"
  elif days_added > 1:
    days_later = " (" + str(days_added) + " days later)"
  if start_day != "":
    new_time_string = str(
      total_hh) + ":" + mm_string + " " + ampm + ", " + many_days_later(
        str(start_day), str(days_added)) + days_later
  else:
    new_time_string = str(total_hh) + ":" + mm_string + " " + ampm + days_later
  return new_time_string
