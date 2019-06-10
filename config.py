

# developed by Gabi Zapodeanu, TME, Enterprise Networking, Cisco Systems


# This file contains the:
# Cisco DNA Center username and password, server info
# ServiceNow developer instance info, username and password
# IOS XE Device name, IP address, username and password


# Update this section with the DNA Center server info and user information
DNAC_URL = 'https://128.107.70.181'
DNAC_USER = 'gabi'
DNAC_PASS = 'password'  # replace this with the provided password

# Update this section with the Service Now instance to be used for labs
SNOW_URL = 'https://devXXXXX.service-now.com/api/now'  # replace XXXXX with the instance number provided
SNOW_ADMIN = 'APIAPP'
SNOW_DEV = 'APIAPP'
SNOW_PASS = 'password'  # replace this with the provided password
SNOW_INSTANCE = 'devXXXXX'  # replace XXXXX with the instance number provided

# Update this section with the info for the CSR 1000V
IOS_XE_HOST = '128.107.70.16X'  # replace X with the Pod number
IOS_XE_USER = 'devnet'
IOS_XE_PASS = 'password'  # replace this with the provided password
IOS_XE_PORT = '830'
IOS_XE_HOSTNAME = 'CSR1Kv-0X'  # replace X with your device number


# Mapping for NAT if required
NAT = {
    '10.93.130.42': '10.93.130.42',
    '10.93.130.21': '10.93.130.21',
    '10.93.140.23': '10.93.140.23',
    '10.255.3.11': '128.107.70.161',
    '10.255.3.12': '128.107.70.162',
    '10.255.3.13': '128.107.70.163',
    '10.255.3.14': '128.107.70.164',
    '10.255.3.15': '128.107.70.165',
    '10.255.3.16': '128.107.70.166',
    '10.255.3.17': '128.107.70.167',
    '10.255.3.18': '128.107.70.168',
    '10.255.3.19': '128.107.70.169',
}
