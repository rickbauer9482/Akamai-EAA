# Akamai-EAA
Project to automate tasks around Akamai's EAA ZeroTrust VPN

You will need the Akamai SDK
https://learn.akamai.com/en-us/webhelp/enterprise-application-access/enterprise-application-access/GUID-091D3A09-3E65-42A4-B1CF-EB058260D7B2.html

Download the SDK
https://downloads.akamai-access.com/eaa-sdk/eaa-sdk.tar.gz

Input file must follow this format. Do not include a header.
Application Name,AppServer,Cloud Region,External hostname,Connector,IDP,Directory,Group,Username

HOST28020-X.X.X.X,x.x.x.x,US East,us-xxxx-host28020,CONNECTOR01,CONNECTOR02,AAD,AD LDAP,HOST28020-GRP,shucky.daclown@xyz.com,

# Akamai-EAA-CLI
The akamai CLI is our own binary that can make calls to our REST API (the Akamai CLI is faster to update than the EAA-SDK at the moment).
 
To install: (instructions here -> https://github.com/akamai/cli)
            On Mac, if you have Homebrew installed: (if you have docker, you can also access the akamai CLI from there)     
            brew install akamai
 
To install the EAA-CLI, run
            akamai install eaa
 
To create an EAA API key
            Follow the instructions here -> https://learn.akamai.com/en-us/webhelp/enterprise-application-access/enterprise-application-access/GUID-686D6E91-239E-447E-8F40-FCACE2C3564F.html
            Your .edgerc file should look similar to this (the eaa_api_host is the same for everyone):
           
[default]
eaa_api_host = manage.akamai-access.com
eaa_api_key = xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx
eaa_api_secret = xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx
 
To add an overlay group once the EAA-CLI is installed (normally, each command will give you a ‘help’ output if you do a -h after it, like ‘akamai eaa dir -h’)
            akamai eaa --section eaa dir addovlgroup directory_id group

If you create a script to run an automation for multiple groups you'll need to change the permissions of the file on Linux and OSX

chmod 755 myscript.sh

BREAKDOWN OF OPTIONS
akamai
calling the program
eaa
which CLI to use (there are others, such as appsec that you can install)
--section eaa
what part of the .edgerc file to use (in my personal .edgerc file, I have a [default] section, an [all] section, and now an [eaa] section)
dir
the option to use (other options include log, search, etc. use -h instead of ‘dir’ to see the other options)
addovlgroup directory_id group
this will create the overlay group. `Directory_id` and `group` are the parameters, put the actual values in these arguments
