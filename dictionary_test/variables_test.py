import information

info = information.login_information

username = "Gonzalo"

if username in info['name']:
    print("Existe!")
else:
    print("no existe")

print("We can use values of a dictionary like Mail that is", info['mail'])
print(type(info['mail']))

# Use Example
username = info['name']
branch = info['branch']
mail = info['mail']
apikey = info['apikey']

#api_call = "http://BRANCH:APIKEY.internal.qadal1301.softlayer.USERNAME.local/HardwareComponent/inventoryCheckin"
api_call = "http://%s:%s.internal.qadal1301.softlayer.%s.local/HardwareComponent/inventoryCheckin" % (branch, apikey, username)
print(api_call)
