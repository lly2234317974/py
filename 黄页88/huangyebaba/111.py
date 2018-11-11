import re
first="1342254531113534724922, 13422545311"
phone=re.findall("1\d{10}", first)
print(phone[0])
phone=['15466']
print(len(phone))