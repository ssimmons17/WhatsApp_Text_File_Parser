
import re
import csv


# Regex to parse text
chat_date_reg = '[0-9]+/[0-9]+/[0-9]+'
chat_time_reg = '[0-9]+:[0-9]+:[0-9]+ [A|P]M'
chat_message_body = ': \w.+'
# whats_app_regex = r"(?P<date>[0-9]+/[0-9]+/[0-9]+)\,\s(?P<time>[0-9]+:[0-9]+:[0-9]+ [A|P]M)] \w+\s\w*:\s(" \
# r"?P<message>\w.+)"

# whats_app_regex = '(?P<date>[0-9]/[0-9]/[0-9]*),\s(?P<time>[0-9]:[0-9]*:[0-9]*\s[A|P]M)]\s(?P<name>\w+\s\w+)'

whats_app_regex = '(?P<date>[0-9]/[0-9]/[0-9]*),\s(?P<time>[0-9]:[0-9]*:[0-9]*\s[A|P]M)]\s(?P<name>\w+\s\w+):\s(?P<message>.*)'


# Lists to hold regex matches for dates, times, names, messages inside of WhatsApp chat file
whats_app_dates = []
whats_app_times = []
whats_app_names = []
whats_app_messages = []
whats_app_attachments = []


# function to open the _chats.txt file and read each line
def open_text_file(filepath):
    with open(filepath, 'r') as chat_file:
        chat_lines = chat_file.readlines()
        return chat_lines


# parse chat file with regex
def parse_chat_file(filepath):
    lines_to_be_parsed = open_text_file(filepath)
    for line in lines_to_be_parsed:
        matches = re.search(whats_app_regex, line)
        chat_dates = matches.group('date').strip()
        chat_times = matches.group('time').strip()
        names = matches.group('name').strip()
        messages = matches.group('message').strip()

        # append data to global lists
        whats_app_dates.append(chat_dates)
        whats_app_times.append(chat_times)
        whats_app_names.append(names)
        whats_app_messages.append(messages)

        rows = zip(whats_app_dates, whats_app_times, whats_app_names, whats_app_messages)
        csv_conversion(rows)
    print("Data has been parsed to CSV")


# function to export parsed chats.txt items to csv file
def csv_conversion(rows):
    csv_headers = ['Date', 'Time', 'Name', 'Message']
    with open('WhatsApp.csv', 'w', encoding='utf-8', newline='') as whatsapp_csv:
        writer = csv.writer(whatsapp_csv)
        writer.writerows([csv_headers])
        for row in rows:
            writer.writerow(row)
        whatsapp_csv.close()


parse_chat_file('/home/stephen/Downloads/WhatsApp Chat - Tripp Eason/_chat.txt')
