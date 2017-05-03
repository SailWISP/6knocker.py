#!/usr/bin/python

import socket
import argparse


def main():

    #create parser
    parser = argparse.ArgumentParser(description="Enter Hostname or IP address and ports to knock.")

    #create arguments
    parser.add_argument("host", help="Enter host followed by port(s)", type=str)
    parser.add_argument("port", help=("Example: knocker.py myserver.example.com 123 456 789"), type=int, nargs="+")

    #parse arguments
    parser.parse_args()
    args = parser.parse_args()
    uknock(args.host,args.port)

# Uncomment to debug parse function
#    print("Target Host IP Address: " + str(args.host))
#    print("Target port: " + str(args.port))


def uknock(host,ports):
    #Send UDP knock to each port specified in argparse
    for port in ports:
        print(host)
        print(port)
        message = "knock"
        emessage = message.encode()
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(emessage,(host,port))


if __name__ == '__main__':
    main()
