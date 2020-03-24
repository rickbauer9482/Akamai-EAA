import sys
from sys import argv
from eaa.client import Client
from eaa.resources import *
from eaa.common import *

client = Client(api_key='XXXXXXXXX', secret_key='XXXXXXXXXX')
apps = client.applications
directories = client.directories
idps = client.idps
connectors = client.connectors
certificates = client.certificates

# Get Users in Directory
aka_dir = client.directories.get(name='AWS AD LDAP')

# Print the all the groups in the directory
# print aka_dir.groups

# Print Users in the directory 25 users at a time
# print aka_dir.get_users

# Print all the Users in the Directory
# print aka_dir.get_users(limit=0, offset=0)

# Print all Groups and Users in the directory to a file
sys.stdout=open("EAA-GRPS-USRS.txt","w")
print aka_dir.groups
print aka_dir.get_users(limit=0, offset=0) 
sys.stdout.close()
 
