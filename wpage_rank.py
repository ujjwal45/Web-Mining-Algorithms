link = {}
number_of_page = int(input("Enter number of pages:"))   #Getting the number of pages

let = list(map(chr, range(65, 65+number_of_page)))

for i in range(number_of_page):
    link[let[i]] = list(map(str, input("Outllink from %s:"%let[i]).split(','))) #Getting the outlink for all pages
print(link)

PR = {}
for i in range(len(let)):
    PR[let[i]] = 1                           #Initializing the Page Rank value of all pages as '1'
print(PR)

df = float(input('Enter the damping factor:'))   #Taking input of damping factor
links = []

for i in range(number_of_page):
    for j in range(len(link[let[i]])):
        links.append(let[i] + '-->' + link[let[i]][j])
       
print(links)
win = []
wout = []

for i in range(len(links)):
    if '-->' in links[i]:
        index = links[i].index('-->')
        chr0 = links[i][index-1]
        chr1 = links[i][index+len('-->')]
        n = len(link[chr1])
        d = 0
        for j in range(len(link[chr0])):
            d += len(link[link[chr0][j]])
        wout.append(n/d)
print(wout)


num_inlink = {}
in_link = {}
for i in range(len(let)):
    alpha = list(let)
    alpha.remove(let[i])
    sl = 0
    f = []
    for j in range(len(alpha)):
        if let[i] in link[alpha[j]]:
            sl = sl +1
            f.append(alpha[j])
    in_link[let[i]] = f        
    num_inlink[let[i]] = sl
print(num_inlink)
print(in_link)

for i in range(len(links)):
    if '-->' in links[i]:
        index = links[i].index('-->')
        chr0 = links[i][index-1]
        chr1 = links[i][index+len('-->')]
        n = num_inlink[chr1]
        d = 0
        for j in range(len(link[chr0])):
            d += num_inlink[link[chr0][j]]
        win.append(n/d)
print(win)        
            
k = 2
while(k>0):
    for i in range(len(let)):
        sh = 0
        for j in range(len(in_link[let[i]])):
            st = in_link[let[i]][j] + '-->' + let[i]
            index = links.index(st)
            sh = sh + PR[in_link[let[i]][j]]*wout[index]*win[index]
        PR[let[i]] = (1-df) + df*(sh)
    print(PR)
    k = k - 1
    
        

