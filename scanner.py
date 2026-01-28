import socket
import re
import ssl 
import threading 

'''
Prompt the user to input a VALID IPv4 address. If
it is not valid, they will be asked to input a valid
one until they do so.
''' 

def getvalid_ip(prompt):   #pass prompt into function
    valid_ip = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$') #regex pattern for a valid Ipv4 address
    while True: #while loop until we get the valid ip input
        ip = input(prompt)
        match = valid_ip.match(ip) #checks to see if it matches the pattern
        if match:
            nums = match.groups() #creates octects for the ip address
            if all(0 <= int(num) <= 255 for num in nums): #the range for the octects are 0 to 255
                return ip # the ip address is valid so it will be returned
            else:
                print('Please enter numbers between the range of 0-255')
        else:
            print('Error: Please input a valid IPv4 address.')


'''
Port Scanner Class

'''
class PortScanner: #initialize port scanner class

    def __init__(self, ip_addr): #constructor method that takes the ip address
        self.ip_addr = ip_addr #assign the address to the instance variable
    
    def scan_port(self,port): #function thats in control of scanning the port
        sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object that uses the IPv4 address and TCP protocol
        sock.settimeout(1) #will timeout if it doesnt receive any response
        try: #safety net to catch any errors
            sock.connect((self.ip_addr, port)) #attempts to connect to the ip and port; formatted as a tuple
            print(f'Port {port} is open')
            sock.close() #closes the socket after use
            
        except: #if an error appears it will just continue
            pass 

    def run_scan(self): #lets run the scan
        for port in range(1, 1025): #scans ports in this range
            self.scan_port(port) #calls the method for each port

#Lets run the program
ip=getvalid_ip('Please enter a valid Ipv4 address you want to scan: ') #gets the valid ip
scanner= PortScanner(ip) #creates PortScanner class instance
scanner.run_scan() #runs the scan method
