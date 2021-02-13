# coding:utf-8

def changeUsername(name):
    if(name === ""):
        return None
    username = list(name)
    for i in range(0, len(username)):
        if username[i] > username[i+1]:
            return "YES"
        else:
            return "NO"
