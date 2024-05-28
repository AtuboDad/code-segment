# -*- coding: utf-8 -*-

import win32com.client
import pprint

wmi = win32com.client.GetObject("winmgmts:")
for usb in wmi.InstancesOf("Win32_USBHub"):
    # print(usb.DeviceID
    # pprint.pprint((dir(usb))
    # pprint.pprint((vars(usb))
    # print(usb.__dict__
    print('Device ID:', usb.DeviceID)
    print('Name:', usb.name)
    print('System Name:', usb.SystemName)
    print('Caption:', usb.Caption)
    print('Caption:', usb.Caption)
    print('ClassCode:', usb.ClassCode)
    print('CreationClassName:', usb.CreationClassName)
    print('CurrentConfigValue:', usb.CurrentConfigValue)
    print('Description:', usb.Description)
    print('PNPDeviceID:', usb.PNPDeviceID)
    print('Status:', usb.Status)
    print('\n')
