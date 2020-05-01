from db_build import *
import json
import schedule
import time

def DB_Update(file_url,columns,db_name,ht_file):

        #connect to sql database on google cloud and insert new values
        conn = DB_Connect()

        #retrieve the last 500 entries from online csv
        df = Get_New_Data(columns,500,file_url)

        #convert date/times to proper format
        df.FIRST_OCCURRENCE_DATE, df.LAST_OCCURRENCE_DATE = pd.to_datetime(df.FIRST_OCCURRENCE_DATE),pd.to_datetime(df.LAST_OCCURRENCE_DATE)

        #load in the current hash table
        OFFENSE_ID_ht = json.load(ht_file)

        #check each row to see if it already exists in the database (by checking the hash)
        #this loop still needs to be tested
        OFFENSE_IDs,idxs = list(df.OFFENSE_ID),list(df.index)

        for i,idx in zip(OFFENSE_IDs,idxs):
            if i in OFFENSE_ID_ht:
                break;
            else:
                #Insert row into database
                DB_Insert(df.loc(idx),conn,db_name)
                OFFENSE_ID_ht.update({i:idx})

        #create new hash table with new ID's
        Create_JSON_ht(OFFENSE_ID_ht,ht_file)

        DB_Close(conn)

if __name__ == "__main__":

    file_url = "https://www.denvergov.org/media/gis/DataCatalog/crime/csv/crime.csv"
    columns = ["OFFENSE_ID","OFFENSE_TYPE_ID","OFFENSE_CATEGORY_ID","FIRST_OCCURRENCE_DATE","LAST_OCCURRENCE_DATE","NEIGHBORHOOD_ID","INCIDENT_ADDRESS"]
    db_name = "crimes"
    ht_file = "/Users/justinteufel/Desktop/dencrime_app/scripts/OFFENSE_ID_ht.json"

    #timer script taken from stack stackoverflow: https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day

    #schedule.every().day.at("12:00").do(DB_Update,file_url,columns,db_name,ht_file)

    #while True:
        #schedule.run_pending()
        #time.sleep(60) # wait one minute
