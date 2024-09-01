import pandas as pd
import requests


google_sheet_url = "https://docs.google.com/spreadsheets/d/1WuEWpM4Eb_Rh2YMLcirVKd5rKoMftIb1wcvu2VqFofc/gviz/tq?tqx=out:csv&sheet=FormResponses1"
form_data = pd.read_csv(google_sheet_url, header=None)

right_answers = [1, 2, 2]
reviews = ['§2', '§10', '§14']

column_1 = form_data.columns[0]
column_2 = form_data.columns[1]
column_3 = form_data.columns[2]
column_4 = form_data.columns[3]
column_5 = form_data.columns[4]
column_6 = form_data.columns[5]


def send_sms(api_key, phone_number, message_content, brand_name, no_sms_flag):
    api_url = 'https://nando.ge/api.php'

    # Data to be sent in the POST request
    post_data = {
        'brand_name': brand_name,
        'apikey': api_key,
        'destination': phone_number,
        'content': message_content,
        'no_sms': no_sms_flag
    }


    try:
        response = requests.post(api_url, data=post_data)


        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"



for index, row in form_data.iterrows():
    things_to_review = []

    try:
        if int(row[column_3]) != right_answers[0]:
            things_to_review.append(reviews[0])
    except ValueError as ve:
        print(f"ValueError for row {index} in column {column_3}: {ve}")

    try:
        if int(row[column_4]) != right_answers[1]:
            things_to_review.append(reviews[1])
    except ValueError as ve:
        print(f"ValueError for row {index} in column {column_4}: {ve}")

    try:
        if int(row[column_5]) != right_answers[2]:
            things_to_review.append(reviews[2])
    except ValueError as ve:
        print(f"ValueError for row {index} in column {column_5}: {ve}")

    # API Key and other necessary variables
    api_key = 'c8214ac78ae915da714d50f02449aaf9e02904d4d4b7c3f10d63be97a652b32e'
    brand_name = 'MatMartivad'
    phone_number = str(row[column_6])  # Ensure the phone number is a string
    message_content = f'ტესტის ქულა: {row[column_2]}. რეკომენდაცია - გაიმეოროს პარაგრაფ(ი)ები: {", ".join(things_to_review)}'
    no_sms_flag = 'false'

    print(f"text {index}: {message_content}")

    report = send_sms(api_key, phone_number, message_content, brand_name, no_sms_flag)
    print(report)
