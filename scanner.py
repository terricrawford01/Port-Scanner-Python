import socket
import ssl
import re
import threading 

'''
Prompt the user to input a VALID IPv4 address. If
it is not valid, they will be asked to input a valid
one until they do so.
'''

def getvalid_ip(prompt):
   valid_ip = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1})\.(\d{1})$')
   while True:
      ip = input(prompt)
      match = valid_ip.match(ip)
      if match:
         nums = match.groups()
         if all(0 <= int(num) <= 255 for num in nums):
            print(f'IP address {ip} is valid')
            return ip
         else:
            print('Please enter numbers between the range of 0-255 in this format xxx.xxx.xxx.xxx')
      else:
         print('Error: Please input a valid IPv4 address.')

prompt = 'Type in the IPV4 address you would like to get scanned. (E.g 192.168.1.1): '
ip_address = getvalid_ip(prompt)
print(f'The valid IP address you entered is: {ip_address}')