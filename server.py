
from flask import Flask, render_template,request
import socket, threading
import time
from setup import main


app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")   
    if request.method == 'POST':
        host = request.form.get("domaininput")
        try:
            
            start_time = time.time()

            if host == 'localhost' or host == '127.0.0.1':
                return render_template("index.html", invalid_domain="Invalid Domain")
            host_ip = socket.gethostbyname(host)
            port = main(host_ip)
            total_time = time.time() - start_time
        except:
            return render_template("index.html", invalid_domain="Invalid Domain")
        
        return render_template("index.html", port=port,port_len=len(port),total_time=total_time,host_ip=host_ip,host_name=host)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

