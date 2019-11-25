# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:55:05 2019

@author: sarthakcfc
"""


import pandas as pd    
import sqlite3
import ipaddress

class Firewall:
    def __init__(self, path_to_csv):
        """
        1. Read CSV.
        2. Convert to data frames using Pandas.
        3. Store in SQLite DB by calling generate_rules .
        """
        self.path_to_csv = path_to_csv
        self.csv_data = pd.read_csv(path_to_csv, header=None)
        self.data_frames = pd.DataFrame(self.csv_data)
       
        """
            ":memory:" stores database in RAM (faster access)
        """ 
        self.conn = sqlite3.connect(":memory:")
        
        """
        - alertnative method to store on disk        
        self.conn = sqlite3.connect("com.illumio.firewall") 
        """
        c = self.conn.cursor()
        c.execute("DROP TABLE IF EXISTS firewall")
        create_table_query = "CREATE TABLE firewall (direction text, protocol \
                text, port_start int, port_end int, ip_start int, ip_end int)"
        c.execute(create_table_query)
        c.close()
        self.generate_rules()

    def generate_rules(self):
        """
        1. Parse data frame to find direction, protocol, port range and ip range.
        2. Find the from and to for port and ip
        3. Store in DB
        """
        
        for row in self.data_frames.itertuples():
            c = self.conn.cursor()
            direction = str(row[1]).strip().lower()
            protocol = str(row[2]).strip().lower()
            find_split_for_row3 = str(row[3]).find('-')
            
            if find_split_for_row3 == -1:
                port_from = port_to = (int(row[3]))
            else:
                port_from = int((row[3])[:find_split_for_row3])
                port_to = int((row[3])[find_split_for_row3+1:])
            
            find_split_for_row4 = str(row[4]).find('-')
            
            if find_split_for_row4 == -1:
                ip_from = ip_to = str(row[4])
            else:
                ip_from = (str(row[4])[:find_split_for_row4])
                ip_to = (str(row[4])[find_split_for_row4+1:])
                
            
            temp_from_port = min(port_from, port_to)
            temp_to_port = max(port_from, port_to)
            
            port_from = str(temp_from_port)
            port_to = str(temp_to_port)
            
            temp_from_ip = int(ipaddress.ip_address(ip_from))
            temp_to_ip = int(ipaddress.ip_address(ip_to))
            ip_from = min(temp_from_ip, temp_to_ip)
            ip_to = max(temp_from_ip, temp_to_ip)
            
            query = "INSERT INTO firewall VALUES ('"+direction+"', '"+protocol+"', "+port_from+","+port_to+", "+str(ip_from)+", "+str(ip_to)+")"
            c.execute(query)
            
            
            c.close()
        
    def accept_package(self, direction, protocol, port, ip_address) ->bool:
        """
        1. Check if rule exists in DB
        2. Return and print result
        """
        c = self.conn.cursor()
        query = "SELECT * FROM firewall WHERE direction = ? AND protocol = ? AND port_start <=? AND port_end >=? AND ip_start <=? AND ip_end >=?"
        ip_int = int(ipaddress.ip_address(ip_address))
    
    
        c.execute(query, (str(direction), str(protocol), port, port, ip_int, ip_int))
        
        if len(c.fetchall()) > 0:  
            print("true")
            return True
        else:
            print("false")
            return False