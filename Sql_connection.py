# imports
import mysql.connector
import functools
import operator
from Text_to_Voice import speak_it

# configuration
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="BhSaPnPh02)#23",
    database = "aidb"
)

# logic
mycursor=mydb.cursor()

sqlformula="INSERT INTO respond (ques,ans) VALUES (%s, %s)"
sqlformula2 = "SELECT ans FROM respond WHERE ques = %s"

#fuction to convert string to tuple
def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str

#fuctions to input
def add_respond(u_input,p_output):
    a1 = (u_input, p_output)
    mycursor.execute(sqlformula,a1)
    mydb.commit()

#function to output
def get_respond(u_input):
    a2=(u_input,) #converting string to tuple
    mycursor.execute(sqlformula2,a2)
    myresult=mycursor.fetchone()
    str_myresult=convertTuple(myresult)
    return str_myresult


k = "are you happy?"
p_output = get_respond(k)
speak_it(p_output)
print(p_output)





