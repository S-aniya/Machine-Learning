import pandas as pd
#Create a Pandas Series from a list
s=pd.Series([10,20,30,40,50])
print(s)

#Create a DataFrame from a dictionary:
data={
    "Name":["saniya","palak","pista"],
    "Marks":[90,91,92],
    "Attendance":[87,78,98]
}
df =pd.DataFrame(data)
print(df)

#Create a DataFrame with custom row and column labels
sd=pd.DataFrame(
    data,index=["s1","s2","s3"]
    ,columns=["Name","Attendance","Marks"]#if columns name doesn't exist earlier, then will show error
)
print(sd)

#Read a CSV file into a DataFrame:
df=pd.read_csv('student.csv.csv')
df.head()