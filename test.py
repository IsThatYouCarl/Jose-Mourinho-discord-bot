import re
from audioplayer import AudioPlayer
import time

# s = 'yup36'
# lst = re.findall('\d+$', s)
# print(lst)

# list = ['projection', 'deflection', 'reflection']
# s = 'projection, deflection, reflection'
# pattern = re.compile('|'.join(re.escape(s) for s in list))
# re_text = pattern.findall(s)
# text = "".join(re_text)
# print(text)

# strings_to_search = ["apple", "banana", "orange"]

# input_string = "I like apples and oranges."

# pattern = re.compile('|'.join(re.escape(s) for s in strings_to_search))

# matches = pattern.findall(input_string)

# print(matches)


# list = ['projection', 'deflection', 'reflection']
# text = 'projection, deflection, reflection'
# pattern = re.compile('|'.join(re.escape(text) for text in list))
# re_text = pattern.findall(text)
# re_text_string = "".join(re_text)
# print(re_text_string)

# new_text = "spamsui4"
# lst = re.findall(r'\d+$', new_text)

# if lst:
#     last_digit = lst[0]
#     new_new_text = new_text.replace(last_digit, '')
#     for i in range(int(last_digit)):
#         print(new_new_text)
# else:
#     for i in range(8):
# #      
# message = 'spamcalma4'

# for text in ["yup", "calma", "respect", "nospeak", "shush", "sui", "ya"]:   
#     if message.startswith('spam') and text in message:
#         new_message = message.lower()
#         new_text = new_message.replace("spam", "").strip()
#         new_text = new_text.lower()        
#         lst = re.findall(r'\d+$', new_text)
            
#         if lst:
#             last_digit = lst[0]
#             new_new_text = new_text.replace(last_digit, '')
#             for i in range(int(last_digit)):                   
#                 print("printed in range of", i)
#                 print(i) 
             
#         else:
#             for i in range(5):                  
#                 print("printed in default range")
        
#     elif text in message:
#         print(text)

current_time = time.time()
seconds = 50
set_time = int(current_time) + seconds
while True:
    curr = time.time()
    if set_time == curr:
        print("Time is up")
        break
    

# curr = time.time()
# time = 50
# set_time = curr + time
# if curr == set_time:
#     print("Time is up")









# def get_seconds_and_reason(message):
#     request = message.replace("remind", "").strip()

#     time = request[:request.index("(")]

#     reason_parenthesis = request.replace(time, "").strip()
#     reason = reason_parenthesis.replace("(", "").replace(")", "")

#     hours_match = re.findall(r'(\d+)h', time)
#     if hours_match:
#         time = time.replace(f'{hours_match[0]}h', "")
#         hour = hours_match[0]
#     else:
#         hour = 0

#     minutes_match = re.findall(r'(\d+)m', time) 
#     if minutes_match:
#         time = time.replace(f'{minutes_match[0]}m', "")
#         minute = minutes_match[0]
#     else:
#         minute = 0

#     seconds_match = re.findall(r'(\d+)s', time)

#     if seconds_match:
#         time = time.replace(f'{seconds_match[0]}', "")
#         second = seconds_match[0]
#     else:
#         second = 0

#     seconds = int(hour)*3600 + int(minute)*60 + int(second)*1

#     return seconds, reason
  
# seconds, reason = get_seconds_and_reason("replace1h2m3s(wait)")
# print(f"you have to wait for {seconds} seconds for {reason}")


# if input == "start":
#     while True:
#         print("Hi")

# if input == "stop":
#     #I want to break the loop in the other if statement
