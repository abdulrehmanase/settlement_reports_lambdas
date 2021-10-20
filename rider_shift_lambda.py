from utils import *
from sql import *

DATETIME = 'Date/Time'
RIDER_NAME = 'Rider Name'
RIDER_CNIC = 'Rider CNIC'
ACCOUNT_NUMBER = 'Account No.'
AGENT_NAME = 'Agent Name'
AMOUNT = 'Amount'
STATUS = 'Status'

DATE_FORMAT = '%Y-%m-%d %H:%M'


def settlement_requests(start_date, end_date):
    data = get_dates(start_date,  end_date)
    start_time, end_time = data['start_time'], data['end_time']
    s_requests = settlement_request_query(start_time, end_time)
    print('asdasd',s_requests[0][0])
    p=convert_to_localtime(s_requests[0][0], DATE_FORMAT)
    print('p',p)
    s_requests_data = [{
        DATETIME: convert_to_localtime(s_request[0], DATE_FORMAT),
        RIDER_NAME: s_request[1],
        RIDER_CNIC: s_request[2],
        ACCOUNT_NUMBER: s_request[3],
        AGENT_NAME: s_request[6] if s_request[6] else '',
        AMOUNT: s_request[4],
        STATUS: s_request[5]
    } for s_request in s_requests]
    header = [DATETIME, RIDER_NAME, RIDER_CNIC, ACCOUNT_NUMBER, AGENT_NAME, AMOUNT, STATUS]
    file_name = 'Settlements Requests Report'
    zip_file = create_csv(file_name, s_requests_data, header)
    attachments = [{'name': file_name + '.zip', 'content': zip_file.getvalue()}]
    title = 'Settlements Requests Report  -  {} - {}'.format(start_date, end_date)

settlement_requests("2019-10-10", "2020-10-10")

