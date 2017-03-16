# Rackspace configuration data
rackspace = {
    # CLB_IDS:
    #
    # Add an ID (or a list of space-seperated IDs) of the cloud
    # load balancers you want to deploy generated certificates
    # on to.
    'CLB_IDS' : '',

    # Port to use for SSL Traffic
    'SECURE_PORT': 443,

    # Whether to allow both HTTP and HTTPS (False) or only HTTPS (True)
    'ALLOW_SECURE_TRAFFIC_ONLY' : False
}
