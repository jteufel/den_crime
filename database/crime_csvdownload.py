import csv
import requests

def request(file_url):

    return requests.get(file_url, stream = True)


def csv_write(file_name,request_object):

    try:
        with open(file_name,"wb") as csv:
            for chunk in request_object.iter_content(chunk_size=1024):

                 # writing one chunk at a time to pdf file
                 if chunk:
                     csv.write(chunk)

        print("CSV write successful")
        return

    except:

        print("Error in writing CSV")
        return


if __name__ == "__main__":

    file_url = "https://www.denvergov.org/media/gis/DataCatalog/crime/csv/crime.csv"
    r = request(file_url)

    print(r)
    #csv_write("crime.csv",r)
