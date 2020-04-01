from eaa.client import Client
from eaa.common import *
from sys import argv
import time

client = Client(api_key='AAAAAA', secret_key='BBBBB')
apps = client.applications
directories = client.directories
connectors = client.connectors
certificates = client.certificates

# filename = argv[1]
# with open(filename) as f:
#     fl = f.readlines()

# for line in fl:
#     fh = line.split(',')
#     # Build the application
#     print (fh[0])
#     print ("Application Creation Complete.")

spgi_dir = directories.get(name='AWS AD LDAP')

# print(spgi_dir)
# print(type(spgi_dir))
print spgi_dir

