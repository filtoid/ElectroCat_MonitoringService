# ElectroCat_MonitoringService
Helper library for uploading to the Electro Cat Studios Monitoring Service

## Setup
In order to use this library you will need an account on Electro Cat Studios (https://electrocatstudios.com/login)

Once you have an account you can generate a device and once this device has been generated it will give you a device key. You will need this key to use this library. Once you have uploaded readings then you can view them through the login on Electro Cat Studios.


## Usage
The simplest usgae is found below:
```
    import monitoringservice

    ms = monitoringservice.MonitoringService(key='<insert_key_here>', type=MonitoringService.GENERIC)

    ms.upload_reading("Our sensor has been triggered")
```
