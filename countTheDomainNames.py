import pprint
#domain name visit counter

######sample list:
domains_list = '''\
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87'''

###### Sample Output for above:
'''\
root-servers.net (1059)
google.com (957)
facebook.com (525)
google-analytics.com (525)'''
###### End Sample output

def by_value(item):
    return item[1]

def count_domains(domains, countMin: int = 0):
    totalCount = {}                                         #initialize dictionary to keep count
    splitLine = domains.split("\n")                         #separate each line into a separate string
    for line in splitLine:                                  
        newLine = line.split(" ")                           #split each string so that we get the URL as the first item and the number of visits as the last item
        domainTest = newLine[0].split('.')
        if domainTest[-2] == "com" or domainTest[-2] == "co":   #the second to last item will indicate if the domain is in two or three parts
            actualDomain = ".".join(domainTest[-3:])
        else:
            actualDomain = ".".join(domainTest[-2:])
        
        if actualDomain in totalCount.keys():                   #now add the key and the value to the dictionary
            totalCount[actualDomain] += int(newLine[-1])
        else:
            totalCount[actualDomain] = int(newLine[-1])
    for k ,v in sorted(totalCount.items(), key = by_value, reverse = True): #then print it out if it's more than the max number provided.
        if v >= countMin:
            print(k, "(" + str(v) + ")")


#Given the prompt, I want to take either the [-2] or [-3] item from a string after delineating based on '.'
#read in a line, delineate on " " and add to a list with [0] being the url and [-1] being the number of instances.
#will need to convert [-1] to an int.
#Then add both to a dictionary, updating any item that is currently there.


#So first I want to split on '.'
#Then check [-2], if it is not "co" or "com" then we return [-2:]
#If [-2] is "co" or "com", then we return [-3:]

count_domains(domains_list, 1000)

