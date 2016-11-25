# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 08:25:36 2016

@author: Peter Knight
"""

import collections
import socket
import datetime


""" Dictionary manipulation goes here. """

def flatten_dictionary(d, parent_key='', sep='_'):

    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten_dictionary(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
        


def remove_null_keys_from_dictionary(dict_to_clean):
    cleaned = []
    for i, j in dict_to_clean.items():
        if j is not None and j != 'None':
            cleaned.append((i, j))
    return dict(cleaned)



def count_keys_in_dictionary(input_list_of_dicts, keyname = "EVENT_TYPE"):
    countlist = []
    for i in input_list_of_dicts:
        newdict = {}
        try:
            newdict[i[keyname]] = 1
            countlist.append(newdict)
        except:
            pass
    try:    
       counter = collections.Counter(countlist[0])
       for d in countlist[1:]:
           counter += collections.Counter(d)
       return counter 
    except:
        pass
    



""" Networking stuff goes here. """

def pynetcat(hostname, port, content, buffer_size = 2048):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(buffer_size)
        if data == "":
            break
        reply = data
    s.close()
    return reply    
        
    






def tests():
    print ' flatten_dictionary test:'   
    a = {"a":1, "d":{"b":2, "c":3}}   
    print flatten_dictionary(a)
       
    print '\n count_keys_in_dictionary test:'
    list_of_dicts = []
    list_of_dicts.append({u'CUSTOMER_ID': u'A', u'EVENT_DATE': datetime.datetime(2016, 1, 1, 12, 0), u'EVENT_TYPE': u'BILL SENT'})
    list_of_dicts.append({u'CUSTOMER_ID': u'A', u'EVENT_DATE': datetime.datetime(2016, 1, 4, 12, 0), u'EVENT_TYPE': u'INBOUND PHONE CALL'})
    list_of_dicts.append({u'CUSTOMER_ID': u'A', u'EVENT_DATE': datetime.datetime(2016, 1, 7, 12, 0), u'EVENT_TYPE': u'PAYMENT RECEIVED'})
    list_of_dicts.append({u'CUSTOMER_ID': u'A', u'EVENT_DATE': datetime.datetime(2016, 2, 1, 12, 0), u'EVENT_TYPE': u'BILL SENT'})
    list_of_dicts.append({u'CUSTOMER_ID': u'A', u'EVENT_DATE': datetime.datetime(2016, 2, 4, 12, 0), u'EVENT_TYPE': u'INBOUND PHONE CALL'})
    list_of_dicts.append({u'CUSTOMER_ID': u'A', u'EVENT_DATE': datetime.datetime(2016, 2, 8, 12, 0), u'EVENT_TYPE': u'PAYMENT RECEIVED'}) 
    print count_keys_in_dictionary(list_of_dicts,keyname = "EVENT_TYPE")
    
if __name__ == '__main__':
    tests()
