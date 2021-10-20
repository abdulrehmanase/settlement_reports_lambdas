from utils import *
import pytz

def settlement_request_query(start_time, end_time):

    SettlementRequest_query_sql = ("""SELECT sr.created_at,CONCAT(au.first_name,'',au.last_login)as rider_name,r.nic,r.e_wallet_number,sr.amount ,sr.status,CONCAT(au.first_name,'',au.last_name)as agent_name  FROM settlement_request sr INNER JOIN rider r 
                                    ON (sr.rider_id = r.id) INNER JOIN auth_user au 
                                    ON (r.user_id = au.id) WHERE (sr.created_at 
                                    BETWEEN '{}' AND '{}' AND sr.status 
                                    IN ("IP", "S", "F", "R"))""".format(start_time, end_time))
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute( SettlementRequest_query_sql)
    settlement_query = cursor.fetchall()
    return settlement_query


def convert_to_localtime(utctime, fmt='%d/%m/%Y %H:%M:%S %p'):
    if utctime is None:
        return utctime
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(pytz.timezone('Asia/Karachi'))
    return localtz.strftime(fmt)