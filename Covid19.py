import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def State():
    url='https://api.covid19india.org/data.json'
    print('Retrieving  data...wait a moment')
    uh=urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()
    js=json.loads(data)


    place=[]
    for i in js['statewise']:
        state=i['state']
        place.append(state)
        print(state)


    n=input('\n\nEnter the states from above list to get the results:')
    n=n.capitalize()

    state_index=place.index(n)

    confirmed=js['statewise'][state_index]['confirmed']
    active=js['statewise'][state_index]['active']
    recovered=js['statewise'][state_index]['recovered']
    deaths=js['statewise'][state_index]['deaths']
    update=js['statewise'][state_index]['lastupdatedtime']
    
    return n, confirmed, active, recovered, deaths, update

def district(n):
    url='https://api.covid19india.org/state_district_wise.json'
    print('Retrieving  data...wait a moment')
    uh=urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()
    js=json.loads(data)

    districts=[]
    for i in js[n]['districtData']:
        print(i)
        districts.append(i)
        
    m=input('\n\nEnter the Districts from above list to get the results:')
    m=m.split()
    sep=[name.capitalize() for name in m] 
    m=sep[0]+' '+sep[1]

    print('Confirmed cases:', js[n]['districtData'][m]['confirmed'])
    print('Active cases:', js[n]['districtData'][m]['active'])
    print('Recovered:', js[n]['districtData'][m]['recovered'])
    print('Death:', js[n]['districtData'][m]['deceased'])
    print('\n\n\t Refresh the page to check for another state and district \n\t\t\t THANK YOU')
    
    return None

input("Press enter to get COVID 19 results") 
n, confirmed, active, recovered, deaths, update=State()
print('Confirmed Cases:', confirmed)
print('active Cases:', active)
print('Recovered:', recovered)
print('Deaths:', deaths)
print('Last Updated time:', update)


confirmation=input("Do you want to Check the district Wise results of "+n+" state  [y/n]:\n")

    

if confirmation=='y':
    district(n)
else:
    print("\t\t THANK YOU")


