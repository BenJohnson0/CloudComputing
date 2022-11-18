import requests
import json

url = "https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/create-or-update?tabs=HTTP#code-try-0"

headers = {"Content-Type": "application/json; charset=utf-8"}

data = {
"properties": {
"publicIPAllocationMethod": "Static",
"idleTimeoutInMinutes": 10,
"publicIPAddressVersion": "IPv4"
},
"sku": {
"name": "Basic"
},
"location": "westeurope"
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)


################################################################

import requests
import json

url = "https://learn.microsoft.com/en-us/rest/api/virtualnetwork/network-interfaces/create-or-update?tabs=HTTP#code-try-0"

headers = {"Content-Type": "application/json; charset=utf-8"}

data = {
    "name": "cloudcomputing372",
    "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CloudComputing_group/providers/Microsoft.Network/networkInterfaces/cloudcomputing372",
    "etag": "W/\"f4082d69-2de2-426b-80fd-20db6f654e67\"",
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "ceb4563d-5fee-4f35-8f21-c7eeff33f3af",
        "ipConfigurations": [
            {
                "name": "ipconfig1",
                "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CloudComputing_group/providers/Microsoft.Network/networkInterfaces/cloudcomputing372/ipConfigurations/ipconfig1",
                "etag": "W/\"f4082d69-2de2-426b-80fd-20db6f654e67\"",
                "type": "Microsoft.Network/networkInterfaces/ipConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAddress": "10.2.0.4",
                    "privateIPAllocationMethod": "Dynamic",
                    "publicIPAddress": {
                        "name": "CloudComputing-ip",
                        "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CloudComputing_group/providers/Microsoft.Network/publicIPAddresses/CloudComputing-ip",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "resourceGuid": "562a305f-2c97-4a68-baba-43131a121a19",
                            "publicIPAddressVersion": "IPv4",
                            "publicIPAllocationMethod": "Dynamic",
                            "idleTimeoutInMinutes": 4,
                            "ipTags": [],
                            "ipConfiguration": {
                                "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CloudComputing_group/providers/Microsoft.Network/networkInterfaces/cloudcomputing372/ipConfigurations/ipconfig1"
                            },
                            "deleteOption": "Detach"
                        },
                        "type": "Microsoft.Network/publicIPAddresses",
                        "sku": {
                            "name": "Basic",
                            "tier": "Regional"
                        }
                    },
                    "subnet": {
                        "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CloudComputing_group/providers/Microsoft.Network/virtualNetworks/CloudComputing_group-vnet/subnets/default"
                    },
                    "primary": True,
                    "privateIPAddressVersion": "IPv4"
                }
            }
        ],
        "dnsSettings": {
            "dnsServers": [],
            "appliedDnsServers": [],
            "internalDomainNameSuffix": "04rvx15tquyetfrxmd4tc5ka1h.ax.internal.cloudapp.net"
        },
        "macAddress": "00-0D-3A-29-27-AE",
        "enableAcceleratedNetworking": False,
        "vnetEncryptionSupported": False,
        "enableIPForwarding": False,
        "networkSecurityGroup": {
            "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CloudComputing_group/providers/Microsoft.Network/networkSecurityGroups/CloudComputing-nsg"
        },
        "primary": True,
        "virtualMachine": {
            "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CLOUDCOMPUTING_GROUP/providers/Microsoft.Compute/virtualMachines/CloudComputing"
        },
        "hostedWorkloads": [],
        "tapConfigurations": [],
        "nicType": "Standard"
    },
    "type": "Microsoft.Network/networkInterfaces",
    "location": "westeurope",
    "kind": "Regular"
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)


##########################################################################


import requests
import json

url = "https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/create-or-update?tabs=HTTP&tryIt=true&source=docs#code-try-0"

headers = {"Content-Type": "application/json; charset=utf-8"}

data = {
    "name": "CloudComputing",
    "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CLOUDCOMPUTING_GROUP/providers/Microsoft.Compute/virtualMachines/CloudComputing",
    "type": "Microsoft.Compute/virtualMachines",
    "location": "westeurope",
    "properties": {
        "vmId": "0351e983-7a34-42cd-bd88-5ed67a3d68fa",
        "hardwareProfile": {
            "vmSize": "Standard_B2s"
        },
        "storageProfile": {
            "imageReference": {
                "publisher": "canonical",
                "offer": "0001-com-ubuntu-server-focal",
                "sku": "20_04-lts-gen2",
                "version": "latest"
            },
            "osDisk": {
                "osType": "Linux",
                "name": "CloudComputing_OsDisk_1_9c5ad7710975451aa820fa36b6f89747",
                "createOption": "FromImage",
                "caching": "ReadWrite",
                "managedDisk": {
                    "storageAccountType": "Premium_LRS",
                    "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CLOUDCOMPUTING_GROUP/providers/Microsoft.Compute/disks/CloudComputing_OsDisk_1_9c5ad7710975451aa820fa36b6f89747"
                },
                "diskSizeGB": 30
            },
            "dataDisks": []
        },
        "osProfile": {
            "computerName": "CloudComputing",
            "adminUsername": "C20316733",
            "linuxConfiguration": {
                "disablePasswordAuthentication": True,
                "ssh": {
                    "publicKeys": [
                        {
                            "path": "/home/C20316733/.ssh/authorized_keys",
                            "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC1X8hUrhkP8a1HE0YToY308rxte6VfStRtfAwxUIZk9e196ZQbkvdisASs8OY7PmLbI+7e599CxE2eb/1p/m6aV/+bxH+6IW1K6G+U+RFiB1c5wiQ47JT3anA0btPGE0DlWNokv85YYW94/LZqmXXQz7cVanD+tUvFriGrd81r7lz1V5nFpz1UUSrVHen+uXyTDfkB6ZP14+xzq39hKZsCteRSe2jfCGTQtDOEmiLVr7ltMEJxNilqoxFJ/IDOWwJWycLtbvYLS0ttw+yd+VCeK9n/KnIL2yW1a5odP4jTpwuL2ILbAjpwJAk1+Eb8WMNF64CB9bI7EaToR4AL1UqE0TF/jrm51Lte0D27fxx8GxPt5TmwrXhfkChzKq1TKlGeKPoiWozPOQtubDDpIBAj0YVQjYmH+2CCkiPIny/zdTjDbmoK8y9TBnUqgixBJKsf1dmwuvBcn6jWgggs7lDZqd/b0l3uC/z0P4XT2HpeENMffTohQd4ThDOYrG6N81s= benjo@LAPTOP-REEGSQ6F\n"
                        }
                    ]
                }
            },
            "secrets": []
        },
        "networkProfile": {
            "networkInterfaces": [
                {
                    "id": "/subscriptions/25f71c06-5451-4329-9a1a-cfa8b1c72ef6/resourceGroups/CloudComputing_group/providers/Microsoft.Network/networkInterfaces/cloudcomputing372",
                    "properties": {
                        "deleteOption": "Detach"
                    }
                }
            ]
        },
        "diagnosticsProfile": {
            "bootDiagnostics": {
                "enabled": True
            }
        },
        "provisioningState": "Succeeded"
    }
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)