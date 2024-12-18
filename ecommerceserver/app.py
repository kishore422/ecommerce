from flask import Flask,request
import pymysql
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import pathlib
import json
from datetime import date

import threading
lock = threading.Lock()

app = Flask(__name__)

UPLOAD_FOLDER = 'static/files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)
app.secret_key = 'any random string'

def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="ecommerce")
        return connection
    except:
        print("Something went wrong in database Connection")

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")

con = dbConnection()
cursor = con.cursor()

"----------------------------------------------------------------------------------------------------"

@app.route('/userRegister', methods=['GET', 'POST'])
def userRegister():
    if request.method == 'POST':
        data = request.get_json()
        
        username = data.get('username')
        email = data.get('email')
        mobile = data.get('mobile')
        password = data.get('password')
        
        cursor.execute('SELECT * FROM users WHERE username = %s', (username))
        count = cursor.rowcount
        if count == 1:        
            return "fail"
        else:
            sql1 = "INSERT INTO users(username, email, mobile, password) VALUES (%s, %s, %s, %s);"
            val1 = (username, email, mobile, password)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
    return "fail"

@app.route('/userLogin', methods=['GET', 'POST'])
def userLogin():
    if request.method == 'POST':
        data = request.get_json()
        
        username = data.get('username')
        password = data.get('password')
        
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        count = cursor.rowcount
        if count == 1:        
            return "success"
        else:
            return "fail"
    return "fail"

@app.route('/addProduct', methods=['GET', 'POST'])
def addProduct():
    if request.method == 'POST':
        print("POST")
        f1 = request.files["File"]
        pname = request.form["pname"]
        pcategory = request.form["pcategory"]
        pdate = request.form["pdate"]
        pprize = request.form["pprize"]
        description = request.form["description"]
        instruction = request.form["instruction"]
        username = request.form["user"]
        
        filename_secure1 = secure_filename(f1.filename)
        
        pathlib.Path(app.config['UPLOAD_FOLDER'], username).mkdir(exist_ok=True)
        f1.save(os.path.join(app.config['UPLOAD_FOLDER'],username,filename_secure1)) 
        
        sql1 = "INSERT INTO productdetails(uploader,filename,pname,pcat,pdate,pprize,description,instruction) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        val1 = (username,"static/files/"+username+"/"+filename_secure1,pname,pcategory,pdate,pprize,description,instruction)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
        
    return "fail"

@app.route('/loadAllProduct/<username>', methods=['GET', 'POST'])
def loadAllProduct(username):
    try:
        lock.acquire()
        cursor.execute('SELECT * FROM productdetails WHERE uploader = %s', ("admin"))
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        catlst = []
        for i in row:
            if i[4] not in catlst:
                catlst.append(i[4])
        
        jsonObj = json.dumps([row,catlst])         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/searchProduct/<username>/<prize>/<category>', methods=['GET', 'POST'])
def searchProduct(username,prize,category):
    try:
        
        if prize == 'None':
            lock.acquire()
            cursor.execute('SELECT * FROM productdetails WHERE uploader != %s and pcat = %s', (username,category))
            row = cursor.fetchall() 
            lock.release()           
            
        elif category == 'None':
            lock.acquire()
            cursor.execute('SELECT * FROM productdetails WHERE uploader != %s and pprize < %s', (username,int(prize)))
            row = cursor.fetchall() 
            lock.release()           
            
        else:   
            lock.acquire()
            cursor.execute('SELECT * FROM productdetails WHERE uploader != %s and pprize < %s and pcat = %s', (username,int(prize),category))
            row = cursor.fetchall() 
            lock.release()   
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/editProduct/<val>', methods=['GET', 'POST'])
def editProduct(val):
    try:   
        print(val)
        if val == 'all':            
            lock.acquire()
            cursor.execute('SELECT * FROM productdetails')
            row = cursor.fetchall() 
            lock.release()
        else:            
            lock.acquire()
            cursor.execute('SELECT * FROM productdetails WHERE uploader = %s', (val))
            row = cursor.fetchall() 
            lock.release()
            
        jsonObj = json.dumps(row)         
        return jsonObj            
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        print("POST")
        f1 = request.files["File"]
        idofp = request.form["id"]
        pname = request.form["pname"]
        pcategory = request.form["pcategory"]
        pdate = request.form["pdate"]
        pprize = request.form["pprize"]
        description = request.form["description"]
        instruction = request.form["instruction"]
        username = request.form["user"]
        
        print(username)
        
        filename_secure1 = secure_filename(f1.filename)
        
        pathlib.Path(app.config['UPLOAD_FOLDER'], username).mkdir(exist_ok=True)
        f1.save(os.path.join(app.config['UPLOAD_FOLDER'],username,filename_secure1)) 
        
        sql1 = "UPDATE productdetails SET filename = %s, pname = %s, pcat = %s, pdate = %s, pprize = %s, description = %s, instruction = %s WHERE id = %s;"
        val1 = ("static/files/"+username+"/"+filename_secure1,pname,pcategory,pdate,pprize,description,instruction,idofp)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"  
    
@app.route('/edit1', methods=['GET', 'POST'])
def edit1():
    if request.method == 'POST':
        print("POST")
        idofp = request.form["id"]
        pname = request.form["pname"]
        pcategory = request.form["pcategory"]
        pdate = request.form["pdate"]
        pprize = request.form["pprize"]
        description = request.form["description"]
        instruction = request.form["instruction"]
        username = request.form["user"]
        print(username)
                
        sql1 = "UPDATE productdetails SET pname = %s, pcat = %s, pdate = %s, pprize = %s, description = %s, instruction = %s WHERE id = %s;"
        val1 = (pname,pcategory,pdate,pprize,description,instruction,idofp)
        cursor.execute(sql1,val1)
        con.commit()
        return "success" 
    
@app.route('/deletePro', methods=['GET', 'POST'])
def deletePro():
    if request.method == 'POST':
        data = request.get_json()
        
        idofp = data.get('id')  
        sql1 = 'DELETE FROM productdetails WHERE id = %s;'
        val1 = (idofp)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
@app.route('/addToCart', methods=['GET', 'POST'])
def addToCart():
    if request.method == 'POST':
        data = request.get_json()
        
        idofp = data.get('id')
        uploader = data.get('uploader')
        file = data.get('file')
        name = data.get('name')
        cate = data.get('cat')
        date = data.get('date')
        prize = data.get('prize')
        quantity = data.get('quantity')
        buyer = data.get('buyer')
        
        cursor.execute('SELECT * FROM cartdata WHERE id = %s and buyer = %s', (idofp,buyer))
        count = cursor.rowcount
        if count == 1:   
            row = cursor.fetchone()
            lastquan = int(row[7])+int(quantity)
            
            sql1 = "UPDATE cartdata SET quantity = %s WHERE id = %s and buyer = %s;"
            val1 = (str(lastquan),idofp,buyer)
            cursor.execute(sql1,val1)
            con.commit()
            return "success" 
        else:
            sql1 = "INSERT INTO cartdata(id,uploader,filename,pname,pcat,pdate,pprize,quantity,buyer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
            val1 = (idofp, uploader, file, name,cate,date,prize,quantity,buyer)
            cursor.execute(sql1,val1)
            con.commit()
            return "success"
    return "fail"

@app.route('/cartProducts/<username>', methods=['GET', 'POST'])
def cartProducts(username):
    try:
        lock.acquire()
        cursor.execute('SELECT * FROM cartdata WHERE buyer = %s', (username))
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/removeCart', methods=['GET', 'POST'])
def removeCart():
    if request.method == 'POST':
        data = request.get_json()
        
        idofp = data.get('id') 
        uploader = data.get('uploader') 
        buyer = data.get('buyer')  
        
        sql1 = 'DELETE FROM cartdata WHERE id = %s AND uploader = %s AND buyer = %s;'
        val1 = (idofp,uploader,buyer)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
@app.route('/donePayment', methods=['GET', 'POST'])
def donePayment():
    if request.method == 'POST':
        data = request.get_json()
        
        username = data.get('username') 
        address = data.get('address') 
        
        today = date.today()

        
        cursor.execute('SELECT * FROM cartdata WHERE buyer = %s', (username))
        row = cursor.fetchall() 
        
        for i in row:
            sql1 = "INSERT INTO payment(pid, img, title, prize,quantity,date,buyer,shipaddress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            val1 = (i[0], i[2], i[3], i[6], i[7], str(today), username,address)
            cursor.execute(sql1,val1)
            con.commit()
        
        for i in row:
            sql1 = 'DELETE FROM cartdata WHERE id = %s AND uploader = %s AND buyer = %s;'
            val1 = (i[0],i[1],i[8])
            cursor.execute(sql1,val1)
            con.commit()
        
        return "success"

@app.route('/updateOrderStatus', methods=['GET', 'POST'])
def updateOrderStatus():
    if request.method == 'POST':
        print("POST")
        data = request.get_json()       
        
        idofp = data.get('id') 
        title = data.get('title')
        prize = data.get('prize') 
        quantity = data.get('quantity')
        buyer = data.get('buyer') 
        status = data.get('status')
                
        sql1 = "UPDATE payment SET status = %s WHERE pid = %s AND title = %s AND prize = %s AND quantity = %s AND buyer = %s;"
        val1 = (status,idofp,title,prize,quantity,buyer)
        cursor.execute(sql1,val1)
        con.commit()
        return "success" 
    
@app.route('/viewOrders/<val>', methods=['GET', 'POST'])
def viewOrders(val):
    try:   
        print(val)
        if val == 'all':            
            lock.acquire()
            cursor.execute('SELECT * FROM payment')
            row = cursor.fetchall() 
            lock.release()
        else:            
            lock.acquire()
            cursor.execute('SELECT * FROM payment WHERE buyer = %s', (val))
            row = cursor.fetchall() 
            lock.release()
            
        jsonObj = json.dumps(row)         
        return jsonObj            
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/viewUsers', methods=['GET', 'POST'])
def viewUsers():
    try:
        lock.acquire()
        cursor.execute('SELECT * FROM users')
        row = cursor.fetchall() 
        lock.release()
        # print(row)
        
        jsonObj = json.dumps(row)         
        return jsonObj
    except Exception as ex:
        print(ex)                 
        return ""
    
@app.route('/updateUser', methods=['GET', 'POST'])
def updateUser():
    if request.method == 'POST':
        data = request.get_json()
        
        idofu = data.get('id')
        username = data.get('username')
        email = data.get('email')
        mobile = data.get('mobile')
        password = data.get('password')
        
        sql1 = "UPDATE users SET username = %s,email = %s,mobile = %s,password = %s WHERE id = %s;"
        val1 = (username,email,mobile,password,idofu)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    return "fail"

@app.route('/deleteUser', methods=['GET', 'POST'])
def deleteUser():
    if request.method == 'POST':
        data = request.get_json()
        
        idofp = data.get('id')  
        sql1 = 'DELETE FROM users WHERE id = %s;'
        val1 = (idofp)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
# ----------------------------------------------------------------------------------------------------

@app.route('/getGraphData', methods=['GET', 'POST'])
def getGraphData():
    try:             
        lock.acquire()
        cursor.execute('SELECT * FROM payment')
        row = cursor.fetchall() 
        lock.release()
        
        lock.acquire()
        cursor.execute('SELECT * FROM users')
        row1 = cursor.fetchall() 
        lock.release()
        
        ordercount=0
        salescount=0
        
        quantilst=[]
        datelst = []
        
        for i in row:
            ordercount+=int(i[4])
            salescount+=int(i[3])
            if i[5] not in datelst:
                datelst.append(i[5])
                quantilst.append(int(i[4]))
            else:
                index = datelst.index(i[5])
                quantilst[index] = int(quantilst[index])+int(i[4])
                
        print("----------------------------------")
        print(ordercount)
        print(salescount)
        print(datelst)
        print(quantilst)
        print(len(row1))
        print("----------------------------------")
        
        finallst = [ordercount,salescount,datelst,quantilst,len(row1)]
            
        jsonObj = json.dumps(finallst)  
        print(jsonObj)
        return jsonObj            
    except Exception as ex:
        print(ex)                 
        return ""
    
if __name__ == "__main__":
    app.run("0.0.0.0")
    
