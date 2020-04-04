import pandas as pd
import sqlalchemy
import io
import requests
import json

def DB_Connect():
    #connect to mySQL DB and return connection object

        username = "jteufel"
        passwd = "Teuferl1"
        host = "35.247.106.154"
        dbname = "dencrime_db"

        db_string = "mysql://{0}:{1}@{2}/{3}".format(username, passwd, host, dbname)
        print("Connection string is", db_string)

        try:
            engine = sqlalchemy.create_engine(db_string)
            conn = engine.connect()
            return conn

        except Exception as exp:

            print("Create engine failed:", exp)
            return

def DB_Insert(df,conn,db_name):

    columns = tuple(df.columns.values)
    columns_str = str(columns).replace("'","")
    cmd = ""

    for index,new_row in df.iterrows():

        row_list = [new_row[col] for col in columns]
        row_list = str(tuple(row_list)).replace("nan","NULL").replace("NaT","NULL")

        cmd = cmd + "INSERT INTO %s %s VALUES %s; \n" % (db_name,columns_str,row_list)

    result = conn.execute(cmd)

def DB_Test(conn,cmd):

    result = conn.execute(cmd).fetchall()
    print(result)

def DB_Close(conn):

    conn.close()

def Create_JSON_ht(dict,file_name):

    offense_id_json = json.dumps(dict)
    f = open(file_name,"w")
    f.write(offense_id_json)
    f.close()

def Get_New_Data(columns,row_count,file_url):

    #return dataframe with data csv url
    #https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url

    r = requests.get(file_url).content #get content from http request
    decoded_file = io.StringIO(r.decode('utf-8'))
    df = pd.read_csv(decoded_file,nrows = row_count, usecols = columns) # add new csv lines(crimes) to dataframe

    return df


if __name__ == "__main__":

    file_url = "https://www.denvergov.org/media/gis/DataCatalog/crime/csv/crime.csv"
    columns = ["OFFENSE_ID","OFFENSE_TYPE_ID","OFFENSE_CATEGORY_ID","FIRST_OCCURRENCE_DATE","LAST_OCCURRENCE_DATE","NEIGHBORHOOD_ID","INCIDENT_ADDRESS"]
    db_name = "crimes"
    ht_file = "/Users/justinteufel/Desktop/dencrime_app/scripts/OFFENSE_ID_ht.json"
    OFFENSE_ID_ht = {}

    #get the first 10000 entries from the online csv
    df = Get_New_Data(columns,10000,file_url)

    #convert date/times to proper format
    df.FIRST_OCCURRENCE_DATE, df.LAST_OCCURRENCE_DATE = pd.to_datetime(df.FIRST_OCCURRENCE_DATE),pd.to_datetime(df.LAST_OCCURRENCE_DATE)

    #create hash table for offense ids
    OFFENSE_IDs,idxs = list(df.OFFENSE_ID),list(df.index)
    for i in range(0,len(OFFENSE_IDs)): OFFENSE_ID_ht.update({OFFENSE_IDs[i]:idxs[i]})
    Create_JSON_ht(OFFENSE_ID_ht,ht_file)

    #connect to sql database on google cloud and insert new values
    conn = DB_Connect()
    DB_Insert(df,conn,db_name)
    DB_Close(conn)
