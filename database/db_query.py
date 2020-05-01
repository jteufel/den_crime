import json

#alot of these fucntions still need to be thoroughly tested/debugged

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

def DB_Test(conn,cmd):

    result = conn.execute(cmd).fetchall()
    print(result)

def DB_Close(conn):

    conn.close()

def Build_JSON(conn,db_name):

    #Build a nested dict of crime statistics from database, to be converted to json

    json_data = {}

    neighborhoods = DB_GetNeighborhoods(conn,db_name)
    crimes = DB_GetCrimes(conn,db_name)
    years = DB_GetYears(conn,db_name)

    for neighborhood in neighborhoods:

        crime_dict = {}
        allcrimes_dict = {}

        for crime in crimes:
            years_dict = {}

            for year in years:
                years_dict.update({year:DB_Query_Crime_ByYear(conn,db_name,crime,neighborhood,year)})

            years_dict.update({"all years":DB_Query_Crime_AllYears(conn,db_name,crime,neighborhood,year)})
            crime_dict.update({crime:years_dict})

        for year in years:
            allcrimes_dict.update({year:DB_Query_AllCrimes_ByYear(conn,db_name,neighborhood,year)})

        allcrimes_dict.update({"all years":DB_Query_AllCrimes(conn,db_name,neighborhood)})
        crime_dict.update({crime:years_dict, "all crimes": allcrimes_dict})

        json_data.update({neighborhood:crime_dict})

    return json_data

def Write_JSON(dict,file_name):

    query_json = json.dumps(dict)
    f = open(file_name,"w")
    f.write(query_json)
    f.close()


def DB_GetNeighborhoods(conn,db_name):

    cmd = """SELECT DISTINCT NEIGHBORHOOD_ID
          FROM %s; \n""" % (db_name)

    result = conn.execute(cmd)


def DB_GetCrimes(conn,db_name):

    cmd = """SELECT DISTINCT OFFENSE_CATEGORY_ID
          FROM %s; \n""" % (db_name)

    result = conn.execute(cmd)


def DB_GetYears(conn,db_name):

    cmd = """SELECT DISTINCT EXTRACT(YEAR FROM FIRST_OCCURRENCE_DATE)
          FROM %s; \n""" % (db_name)

    result = conn.execute(cmd)


def DB_Query_Crime_ByYear(conn,db_name,crime,neighborhood,year):

    cmd = """SELECT COUNT(*)
          FROM %s
          WHERE OFFENSE_CATEGORY_ID = %s AND
          NEIGHBORHOOD_ID = %s AND
          EXTRACT(YEAR FROM FIRST_OCCURRENCE_DATE) = %s; \n""" % (db_name,crime,neighborhood,year)

    result = conn.execute(cmd)


def DB_Query_Crime_AllYears(conn,db_name,crime,neighborhood):

    cmd = """SELECT COUNT(*)
          FROM %s
          WHERE OFFENSE_CATEGORY_ID = %s AND
          NEIGHBORHOOD_ID = %s; \n""" % (db_name,crime,neighborhood)

    result = conn.execute(cmd)


def DB_Query_AllCrimes_ByYear(conn,db_name,neighborhood,year):

    cmd =  """SELECT COUNT(*)
           FROM %s
           WHERE NEIGHBORHOOD_ID = %s AND
           EXTRACT(YEAR FROM FIRST_OCCURRENCE_DATE) = %s; \n""" % (db_name,neighborhood,year)

    result = conn.execute(cmd)


def DB_Query_AllCrimes_AllYears(conn,db_name,neighborhood):

    cmd =  """SELECT COUNT(*)
           FROM %s
           WHERE NEIGHBORHOOD_ID = %s; \n""" % (db_name,neighborhood,year)

    result = conn.execute(cmd)
