# Akamai-EAA
Project to automate tasks around Akamai's EAA ZeroTrust VPN

You will need the Akamai SDK
https://learn.akamai.com/en-us/webhelp/enterprise-application-access/enterprise-application-access/GUID-091D3A09-3E65-42A4-B1CF-EB058260D7B2.html

Download the SDK
https://downloads.akamai-access.com/eaa-sdk/eaa-sdk.tar.gz

Input file must follow this format. Do not include a header.
Application Name,AppServer,Cloud Region,External hostname,Connector,IDP,Directory,Group,Username

HOST28020-X.X.X.X,x.x.x.x,US East,us-xxxx-host28020,CONNECTOR01,CONNECTOR02,AAD,AD LDAP,HOST28020-GRP,shucky.daclown@xyz.com,
