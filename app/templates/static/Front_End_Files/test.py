
burglary_one = """Crime: burglary-residence-no-force      Date: 9/4/2018 14:05      Address: 229 S IRVING ST
Crime: burglary-business-no-force      Date: 9/17/2018 15:14      Address: 3325 W ALAMEDA AVE
Crime: burglary-residence-by-force      Date: 9/27/2018 14:53      Address: 520 N LOWELL BLVD
Crime: burglary-residence-by-force      Date: 9/26/2018 18:03      Address: 505 N KING ST"""

arson_one = """Crime: aronresidence-no-force      Date: 9/4/2018 14:05      Address: 229 S IRVING ST
Crime: burglary-business-no-force      Date: 9/17/2018 15:14      Address: 3325 W ALAMEDA AVE
Crime: burglary-residence-by-force      Date: 9/27/2018 14:53      Address: 520 N LOWELL BLVD
Crime: burglary-residence-by-force      Date: 9/26/2018 18:03      Address: 505 N KING ST"""

neighboorhood_one = {}
neighboorhood_two = {}
neighboorhood_three = {}

neighboorhood_one["burglary"] = burglary_one
neighboorhood_one["arson"] = arson_one


data = {}
data["neighboorhood_one"] = neighboorhood_one
