n = int(input("Number of pages:"))
alpha = list(map(chr, range(65, 65+n)))
hub = {}
print("Enter the Outlink for the corresponding pages:")
for a in alpha:
    outl = input(a+": ").split(",")
    hub[a] = outl
auth = {}
for a in alpha:
    inl = []
    for b in alpha:
        for i in hub[b]:
            if(i==a):
                inl.append(b)
    auth[a] = inl
hub_score = {}
auth_score = {}
for a in alpha:
    hub_score[a] = 1
    auth_score[a] = 0
print("Site name\tHub Score\tAuthority Score")
for j in range(0,20):
    s1 = 0
    s2 = 0
    for a in alpha:
        s = 0
        for i in auth[a]:
            s = s + hub_score[i]
        auth_score[a] = auth_score[a]+ s
    for a in alpha:
        s1 = s1 + auth_score[a]
    for a in alpha:
        auth_score[a] = auth_score[a]/s1
    for a in alpha:
        print(a,"\t",hub_score[a],"\t",auth_score[a])
    print("\n")
    for a in alpha:
        f = 0
        for i in hub[a]:
            f = f + auth_score[i]
        hub_score[a] = hub_score[a] + f
    for a in alpha:
        s2 = s2 + hub_score[a]
    for a in alpha:
        hub_score[a] = hub_score[a]/s2
     #print("Hub:") #print(hub_score)
