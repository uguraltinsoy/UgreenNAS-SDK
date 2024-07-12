# UGREEN NAS Simple SDK
```
UGREEN is a PRIVATE API based Simple SDK being developed for NAS servers. NOT AN OFFICIAL DOCUMENT! 
```
## RSI Public key Creation
To use the SDK, connect to your NAS server via SSH and open the example 999.pub file of your user uid in the ```/var/cache/ugreen-rsa``` folder as ```cat 999.pub```, copy the content and save it into your project as ```public_key.pem``` as below
![ssh](https://i.imgur.com/CnMm2jN.png)
![app](https://i.imgur.com/HLOdOvs.png)

## SDK
### [JAVA SDK](./Java)
### [PYTHON SDK](./Python)


## Verify
#### GET HTTP  ```{ip-address}:{port}/ugreen/v1/verify/heartbeat```
```Json
{
  "code": 200,
  "msg": "success",
  "data": {},
  "time": 0.000001304
}
```
#### POST HTTP  ```{ip-address}:{port}/ugreen/v1/verify/check```
```Json
{
  "username": "{username}"
}
```
Result:
```Json
{
  "code": 200,
  "msg": "success",
  "data": {},
  "time": 0.000001304
}
```
#### POST HTTP  ```{ip-address}:{port}/ugreen/v1/verify/login```
```Json
{
  "keepalive": true,
  "username": "{username}",
  "password": "{hash-password}"
}
```
Result:
```Json
{
  "code": 200,
  "msg": "success",
  "data": {
    "auth_type": "header",
    "ddns": [],
    "deny_change_pwd": false,
    "enable_change_pwd": false,
    "http_port": 9999,
    "https_port": 9443,
    "ipv4": [
      "111.111.111.111"
    ],
    "ipv6": [],
    "is_bootstrap_completed": true,
    "is_cloud": false,
    "is_domain": false,
    "mobile_guide": false,
    "model": "DXP4800 Plus",
    "nas_name": "{nas_name}",
    "public_key": "{public_key}",
    "role": "admin",
    "sn": "{sn}",
    "static_token": "{static_token}",
    "system_version": "1.0.0.0940",
    "token": "{token}",
    "uglink": "",
    "uglink_id": "",
    "uid": {uid},
    "username": "{username}",
    "version_number": 100000940
  },
  "time": 1.186819069
}
```
#### GET HTTP  ```{ip-address}:{port}/ugreen/v1/verify/handshake?token={token}```
```Json
{
  "code": 200,
  "msg": "success",
  "data": {},
  "time": 0.017705918
}
```
## User
#### GET HTTP  ```{ip-address}:{port}/ugreen/v1/user/headpic/stream/{uid}?token={token}```
```Json
USER IMAGE
```
#### GET HTTP  ```{ip-address}:{port}/ugreen/v1/user/priority_link?token=?token={token}```
```Json
{
  "code": 200,
  "msg": "success",
  "data": {
    "ddns": [],
    "host": "111.111.111.111",
    "uglink": "",
    "uglink_id": "",
    "ipv_4": [
      "111.111.111.111"
    ],
    "ipv_6": [],
    "http_port": 9999,
    "https_port": 9443
  },
  "time": 0.527269986
}
```
## Sysinfo
#### GET HTTPS  ```{ip-address}:{ssl_port}/ugreen/v1/sysinfo/machine/common?token={token}```
```Json
{
  "code": 200,
  "msg": "success",
  "data": {
    "common": {
      "nas_name": "DXP4800PLUS",
      "uglink_id": "",
      "nas_owner": "{owner_email}",
      "model": "DXP4800 Plus",
      "serial": "{serial_number}",
      "mac": [
        "{mac_1}",
        "{mac_2}"
      ],
      "system_version": "1.0.0.0940",
      "run_time": 200635,
      "last_turn_on_time": "2024-07-08 14:45:43",
      "repair_start_time": 0,
      "repair_end_time": 0
    },
    "hardware": {
      "cpu": [
        {
          "model": "Intel(R) Pentium(R) Gold 8505",
          "ghz": 4400,
          "core": 5,
          "thread": 6,
          "temperature": 42
        }
      ],
      "mem": [
        {
          "model": "M425R1GB4BB0-CQKOL",
          "size": 8589934592,
          "mhz": "4800 MHz"
        }
      ],
      "net": [
        {
          "model": "eth1",
          "ip": "-",
          "mac": "{mac_1}"
        },
        {
          "model": "eth0",
          "ip": "-",
          "mac": "{mac_2}"
        }
      ],
      "ups": null,
      "usb": null
    }
  },
  "time": 0.47923691
}
```
## Components
#### GET HTTPS  ```{ip-address}:{ssl_port}/ugreen/v1/desktop/components/data?id=desktop.component.SystemStatus&token={token}```
```Json
{
  "code": 200,
  "msg": "success",
  "data": {
    "dev_name": "DXP4800PLUS",
    "last_boot_date": "07-08 14:45",
    "last_boot_time": 1720439143,
    "message": "The system is running normally.",
    "status": 0,
    "total_run_time": 200835,
    "type": 2
  },
  "time": 0.022031365
}
```
#### GET HTTPS  ```{ip-address}:{ssl_port}/ugreen/v1/desktop/components/data?id=desktop.component.DeviceMonitoring&token={token}```
```Json
{
  "code": 200,
  "msg": "success",
  "data": {
    "cpu_usage_rate": 0.67,
    "download_speed": {
      "unit": "KB/s",
      "value": 2.4
    },
    "ram_usage_rate": "13.09",
    "type": 3,
    "upload_speed": {
      "unit": "KB/s",
      "value": 0.06
    }
  },
  "time": 0.000110174
}
```
#### GET HTTPS  ```{ip-address}:{ssl_port}/ugreen/v1/desktop/components/data?id=desktop.component.TemperatureMonitoring&token={token}```
```Json
{
  "code": 200,
  "msg": "success",
  "data": {
    "cpu_status": 0,
    "cpu_temperature": 43,
    "disk_list": [],
    "fan_speed": 590,
    "fan_status": 0,
    "message": "The temperature is normal, and the heat dissipation is good.",
    "status": 0,
    "type": 6
  },
  "time": 0.002065633
}
```
#### GET HTTPS  ```{ip-address}:{ssl_port}/ugreen/v1/desktop/components/data?id=desktop.component.StorageSpace&token={token}```
```Json
{
  "code": 200,
  "msg": "success",
  "data": {
    "storage_list": null,
    "type": 4
  },
  "time": 0.000809068
}
```

