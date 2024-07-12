import os
import requests
import urllib3  
import json
import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

library_path = os.path.dirname(__file__)
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

class UgreenNAS:
    def __init__(self, ip, port, username, password, public_key):
        self.ip = ip
        self.port = port
        self.username = username

        self.password = self.encrypt_password(password, public_key)
        self.connection = None
        self.msg = None
        self.code = None
        self.static_token = None
        self.uid = None
        self.connect()

    def encrypt_password(self, password, public_key):
        public_key_path = os.path.join(library_path, public_key)
        with open(public_key_path, "rb") as key_file:
            public_key = RSA.import_key(key_file.read())
        encrypted_password = PKCS1_v1_5.new(public_key).encrypt(password.encode())
        encrypted_base64 = base64.b64encode(encrypted_password).decode('utf-8')
        return encrypted_base64

    def connect(self):
        url = f"http://{self.ip}:{self.port}/ugreen/v1/verify/login"
        payload = json.dumps({"keepalive": True, "username": self.username, "password": self.password})
        headers = { 'Content-Type': 'application/json', 'Cookie': 'HttpOnly' }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        data = json.loads(response.text)

        self.connection = (data["code"] == 200 and data["msg"] == "success")
        self.code = data["code"]
        self.msg = data["msg"]
        if self.connection: 
            self.static_token = data["data"]["static_token"]
            self.uid = data["data"]["uid"]

    def isConnect(self): return self.connection
    def isConnect(self): return self.connection, self.code, self.msg

    def getToken(self): return self.static_token

    def chekHandshake(self, token): 
        url = f"http://{self.ip}:{self.port}/ugreen/v1/verify/handshake?token={token}"
        response = requests.request("GET", url, verify=False)
        data = json.loads(response.text)
        return data["code"], data["msg"]

    def getUserImage(self):
        url = f"http://{self.ip}:{self.port}/ugreen/v1/user/headpic/stream/{self.uid}?token={self.static_token}"
        response = requests.request("GET", url, verify=False)
        return response.content
    
    def saveUserImage(self, file_path, file_name):
        path = file_path + file_name
        url = f"http://{self.ip}:{self.port}/ugreen/v1/user/headpic/stream/{self.uid}?token={self.static_token}"
        response = requests.request("GET", url, verify=False)
        with open(path, "wb") as f: f.write(response.content)
        return None
    
    def priorityLink(self):
        url = f"http://{self.ip}:{self.port}/ugreen/v1/user/priority_link?token={self.static_token}"
        response = requests.request("GET", url, verify=False)
        data = json.loads(response.text)
        if data["code"] == 200: return data["data"]
        else: return data["msg"]

    def sysInfo(self):
        url = f"http://{self.ip}:{self.port}/ugreen/v1/sysinfo/machine/common?token={self.static_token}"
        response = requests.request("GET", url, verify=False)
        data = json.loads(response.text)
        if data["code"] == 200: return data["data"]
        else: return data["msg"]
    
    def systemStatus(self):
        url = f"http://{self.ip}:{self.port}/ugreen/v1/desktop/components/data?id=desktop.component.SystemStatus&token={self.static_token}"
        response = requests.request("GET", url, verify=False)
        data = json.loads(response.text)
        if data["code"] == 200: return data["data"]
        else: return data["msg"]

    def deviceMonitoring(self):
        url = f"http://{self.ip}:{self.port}/ugreen/v1/desktop/components/data?id=desktop.component.DeviceMonitoring&token={self.static_token}"
        response = requests.request("GET", url, verify=False)
        data = json.loads(response.text)
        if data["code"] == 200: return data["data"]
        else: return data["msg"]

    def temperatureMonitoring(self):
        url = f"http://{self.ip}:{self.port}/ugreen/v1/desktop/components/data?id=desktop.component.TemperatureMonitoring&token={self.static_token}"
        response = requests.request("GET", url, verify=False)
        data = json.loads(response.text)
        if data["code"] == 200: return data["data"]
        else: return data["msg"]

    def storageSpace(self):
        url = f"http://{self.ip}:{self.port}/ugreen/v1/desktop/components/data?id=desktop.component.StorageSpace&token={self.static_token}"
        response = requests.request("GET", url, verify=False)
        data = json.loads(response.text)
        if data["code"] == 200: return data["data"]
        else: return data["msg"]

if __name__ == "__main__":
    #nas = UgreenNAS("<nas_ip>", <port>, "<username>", "<password>", "public_key.pem")
    nas = UgreenNAS("192.168.1.193", 9999, "uguraltnsy", "Albz5Kymt3fsill3256", "public_key.pem")
    
    #connection, code, msg = nas.isConnect()
    #token = nas.getToken()
    #chekHandshake = nas.chekHandshake("<token>")
    #image = getUserImage()
    #nas.saveUserImage("","uguraltnsy.jpg")
    #priority_link = nas.priorityLink()
    #sysInfo = nas.sysInfo()
    #systemStatus = nas.systemStatus()
    #deviceMonitoring = nas.deviceMonitoring()
    #temperatureMonitoring = nas.temperatureMonitoring()
    #storageSpace = nas.storageSpace()

    
    
