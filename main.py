from http.client import responses
import requests
import config
import json
import sys
class User:
    def __init__(self,apikey,serverid,identifier):
        self.apikey = apikey
        self.serverid = serverid
        self.identifier = identifier
    def apikey(self):
        return self.apikey
    def serverid(self):
        return self.serverid
    def identifier(self):
        return self.identifier
token=config.getapikey()
baseurl=config.getbaseurl()
auth={
    'Authorization':f"Bearer {token}",
    "Accept":"application/json"
}
def userapi():
    api=input("enter your api key:")
    return api
def server(serverid):
    try:
        response = requests.get(baseurl+f"/servers/{serverid}",headers=auth)
        print(f"Hi {getuser(response.json()['attributes']['user'])}")
        print(f"Server : {getservername(session.serverid)}")
        print(f"Memory = {response.json()['attributes']['limits']['memory']}")
        print(f"Cpu = {response.json()['attributes']['limits']['cpu']}")
        print(f"Disk= {response.json()['attributes']['limits']['disk']}")
    except:
        print("error")
        return -1
def serveridentifier(serverid):
    try:
        response = requests.get(baseurl+f"/servers/{serverid}",headers=auth)
        return response.json()['attributes']['identifier']
    except:
        print("error")
        return -1
def getuser(userid):
    try:
        response = requests.get(baseurl+f"/users/{userid}",headers=auth)
        return response.json()['attributes']['username']
    except:
        return -1
def poweract(serverid,action):
    params={}
    params['ID']=serverid
    params['signal'] = action
    authuser={"Accept":"application/json"}
    authuser['Authorization']=f"Bearer {session.apikey}"
    try:
        response = requests.post(config.getclient()+f"/servers/{serverid}/power?type=admin",headers=authuser,params=params)
        return "server "+action+"ed "+"successfully"
    except:
        return "server "+action+"failed"
def sendcommand(serverid,command):
    params={}
    params['ID']=serverid
    params['command']=command
    authuser={"Accept":"application/json"}
    authuser['Authorization']=f"Bearer {session.apikey}"
    try:
        requests.post(config.getclient()+f"/servers/{serverid}/command",headers=authuser,params=params)
        return "command sent successfully"
    except:
        return "command failed"
def getservername(serverid):
    try:
        response = requests.get(baseurl+f"/servers/{serverid}",headers=auth)
        return response.json()['attributes']['name']
    except:
        return "error"
if __name__ == "__main__":
    print(r" |  ____| |        /\    / ____| |  | | \ | |/ __ \|  __ \|  ____|/ ____|")
    print(r" | |__  | |       /  \  | (___ | |__| |  \| | |  | | |  | | |__  | (___ ")
    print(r" |  __| | |      / /\ \  \___ \|  __  | . ` | |  | | |  | |  __|  \___ \ ")
    print(r" | |    | |____ / ____ \ ____) | |  | | |\  | |__| | |__| | |____ ____) |")
    print(r" |_|    |______/_/    \_\_____/|_|  |_|_| \_|\____/|_____/|______|_____/ ")


    apikey=input("enter your api key:")
    serverid=input("enter your serverid:")
    identifier=serveridentifier(serverid)
    session = User(apikey, serverid, identifier)
    server(session.serverid)
    while 1:
        print("Hi Please Select An Option")
        print(f"Logged in to server : {getservername(session.serverid)}")
        print("1.Power \n2.SendCommand\n3.Exit ")
        opt=input("Enter your option : ")
        if opt == "1":
            print("select an action")
            print("1.start \n 2.stop \n 3.restart \n 4.kill")
            option=input("Enter your choice : ")
            if option=="1":
                print(poweract(session.identifier,"start"))
            if option=="2":
                print(poweract(session.identifier,"stop"))
            if option=="3":
                print(poweract(session.identifier,"restart"))
            if option=="4":
                print(poweract(session.identifier,"kill"))
        if opt=='2':
            command=input("Enter command : ")
            print(sendcommand(session.identifier,command))
        if opt=='3':
            sys.exit(0)