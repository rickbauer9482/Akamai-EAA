from eaa.client import Client
from eaa.common import *
from sys import argv

client = Client(api_key='XXXXXXXX', secret_key='YYYYYYYYY')
apps = client.applications
directories = client.directories
connectors = client.connectors
certificates = client.certificates

filename = argv[1]
with open(filename) as f:
    fl = f.readlines()

for line in fl:
    fh = line.split(',')
    # Build the application
    app = apps.create(
        name=fh[0], 
        host=fh[3], 
        domain=Domain.APP_DOMAIN_WAPP, 
        app_profile=AppProfile.APP_PROFILE_RDP, 
        pop_region=fh[2], 
        description='This application was created by EAA-Bulk-RDP.py')

    # Add App Servers
    app.servers.add(
        orig_tls=True, 
        origin_protocol=Protocol.PROTOCOL_RDP, 
        origin_host=fh[1], 
        origin_port=3389)
    app.connectors.add(name=fh[4])
    app.connectors.add(name=fh[5])

    # Configure the IDP and Directory

    app.set_idp(name=fh[6])
    app.directories.add(name=fh[7])
    app.groups.add(directory_name=fh[7], group_names=[fh[8]])

    # Add users to the Overlay group
    dr = directories.get(name=fh[7])
    usr = dr.users.get(name=''+fh[9]+'')
    grp = dr.groups.get(name=fh[8])
    usr.add_groups([grp])
    # Configure Services
    app.services.add(service_type=ServiceType.SERVICE_TYPE_ACCELERATION)

    #Configure RDP Advanced Settings
    app.set_remote_spark_advanced_settings(remote_spark_mapClipboard=False, remote_spark_mapDisk=False, remote_spark_disk=None, remote_spark_mapPrinter=False, remote_spark_audio=False)

    print "Application Creation Complete."
    app.deploy()
    app.get_deploy_status()



