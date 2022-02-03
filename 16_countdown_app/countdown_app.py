from datetime import datetime

user_input = input("Enter your goal with a deadline seperated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till_deadline = deadline_date - today_date
hours_till_deadline = int(time_till_deadline.total_seconds() / 60 / 60)

print(f"Time remaining for your goal {goal} is {time_till_deadline.days} days or {hours_till_deadline} hours.")