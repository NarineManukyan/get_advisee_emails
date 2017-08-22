import pandas as pd

advisee_data = pd.read_csv("webadviser_list.csv")
emails = []
emailable_list = ''
count = 0

for student in advisee_data['Name']:

    parts = student.split()
    last_name = parts[0].split(',')[0]
    first_name = parts[1]
    count+=1

    email = first_name + '.' + last_name + '@mymail.champlain.edu'
    emails.append({'first_name':first_name,'email': email})

    if(count == len(advisee_data)):
        emailable_list+=email
    else:
        emailable_list += email + ','

print("Here is an emailable list that you can copy and paste into your email")
print(emailable_list)
frame_emails = pd.DataFrame(emails)
frame_emails.to_csv('advisee_emails.csv')