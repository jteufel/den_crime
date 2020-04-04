import pandas as pd

# adds neighboorhood as id in svg

nb_name = "NBHD_NAME"
csvpath = "/Users/justinteufel/Desktop/statistical_neighborhoods.csv"
svgpath = "/Users/justinteufel/Desktop/statistical_neighborhoods.svg"
newsvgpath = "/Users/justinteufel/Desktop/statistical_neighborhoods_new.svg"

df  = pd.read_csv(csvpath)

neighboorhoods = list(df[nb_name])

f = open(svgpath,"r+")
fn = open(newsvgpath,"w")
count = 0

all_lines = []


for lines in f.readlines():

    if "<path d" in lines:
        repl_string = '<path id="' + str(neighboorhoods[count]) + '" d'
        #print(repl_string)
        all_lines.append(lines.replace("<path d", repl_string))
        count+=1

    else:
        all_lines.append(lines)


fn.writelines(all_lines)
print(all_lines)


f.close()
fn.close()
