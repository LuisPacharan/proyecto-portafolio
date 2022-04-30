import pyodbc

server =  'SERVIDOR_IP O NOMBRE_DEL_SERVER'             
database = 'NOMBRE_ESQUEMA O BASE_DE_DATOS' 
username = 'USUARIO' 
password = 'PASSWORD' 

try: 

    conexion = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+';DATABASE='
    +database+';UID='+username+';PWD='+ password)

    print("conexion exitosa!")

except : 
    print("error al intentar conectarse!")

cursor = conexion.cursor()

#QUERY A EJECUTAR 
cursor.execute(
                 "SELECT * FROM TABLA;"
              ) 
row = cursor.fetchone() 
while row: 
    print(row)

cursor.close()
conexion.close()