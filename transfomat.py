with open("ip.txt", 'r') as f:
    a=""
    for ip in f:
        a = a + " " + ip.strip()
    print(a)