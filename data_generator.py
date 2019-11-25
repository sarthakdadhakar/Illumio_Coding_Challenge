# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:09:54 2019

@author: sarthak
"""

import random

#input format = inbound/o , tcp/u, int-int(1-65536), ip_addr-ip_addr

direction = [ "inbound" , "outbound" ]
mode = [ "tcp" , "udp" ]
is_range = [ True , False ]
size_of_data = 50000
output_file_name = "firewall_rules_50k.csv"
output_file = open(output_file_name , "w+")

"""
    randomly generating IPv4
"""
def generate_ip(version=4):
    return str('.'.join([str(random.randint(0,255)) for x in range(version)]) )

"""
    randomly generating port number
"""
def generate_port():
    return str(random.randint(1,65536))


"""
    generating csv file
"""
string = ""

def make_a_csv_line():
    string = "\n"
    string += random.choice( direction )
    string += ","

    string += random.choice( mode )
    string += ","

    if ( random.choice(is_range) ):
        string += generate_port() + "-" + generate_port()
    else:
        string += generate_port()
    string += ","

    if ( random.choice(is_range) ):
        string += generate_ip() + "-" + generate_ip()
    else:
        string += generate_ip()
    return string

string = make_a_csv_line()
output_file.write( string[1:] )

for i in range(size_of_data-1):
    output_file.write( make_a_csv_line() )

output_file.close()