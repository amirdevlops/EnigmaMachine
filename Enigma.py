#0.0.1v creator AMIR
#This program is simulatoin of Enigma machine 
#If u dont know about Enigma machine dont try to use this program 
#Github : amirdevlops/path 

#taking user input 
print("<<--------------------------------Enigma Machine-------------------------------->>")
print("This program is the semulation Of ENIGMA MACHINE ")

#variables 

file_save = 0
arr = []
PlugBoardlist = []
Roteres_list = []
rotortworeslist = []
#settings 
listofplugbords = ["a" , "o" , "i" , "r", "q" , "v" , "c" , "z" ,"k" , "s"]
print(listofplugbords , " : PlugBoard Setting ")
listofencryptedplugboards = ["j" , "l" , "x" , "t" , "h" , "f" , " w" , "t", "n" , "d"]
print( listofencryptedplugboards , " : Encrypted PlugBoard")
a = 5
b = 24
c = 19
d = 3
e = 1
f = 20
g = 12
h = 6
i = 18
j = 10
k = 26
l =  8
m = 14
n = 15
o = 13
p = 23
q = 2
r = 7
s = 21
t = 11
u = 4
v = 16
w = 8
x = 0
y = 22
z = 17
print(a ,b ,c ,d ,e ,f ,g ,h ,i ,j , k, l ,m,  n, o ,p ,q, r ,s ,  t, u ,v ,w, x,  y,  z , " : Rotor 1 Num")
#for rotor two we need diferent variables 

at = 25
bt = 17
ct = 11
dt = 2
et = 19
ft = 16
gt = 9
ht = 24
kt = 13
it = 21
jt = 6
lt = 8
mt = 23
nt = 10
ot = 4
pt = 1
qt = 22
rt = 20
st = 5
tt = 15
ut = 0
vt = 3
wt = 18
xt = 12
yt = 14
zt = 7
print(at ,bt ,ct ,dt ,et ,ft, gt ,ht ,it ,jt , kt, lt ,mt,  nt, ot ,pt ,qt, rt ,st ,  tt, ut ,vt ,wt, xt,  yt,  zt , " : Rotor 1 Num")




#Functions

def PlugBoard(a):
    
    for P in range(len(listofplugbords)):
        
        if(a == listofplugbords[P]):
            print(f"Match has been founded : {listofplugbords[P]} & the match is : {listofencryptedplugboards[P]}")
            
            return listofencryptedplugboards[P]     #bracking this loop if the match if is found 


#some doucmention so u can create an copy
#this is function name Plugboard() this function is in from enogma machine where is a boaed where u change the latter first
#this is an basic type of encryption 
#as enigma machine support only 10 latters at a time so i have make it for only 10 words which can be changed by the user or am self mode which i will create later 
#this function basicly checks if there is any workd match which is present in thes list name listofplugboards where 1o letters are presented if any of them matche the 
#function simply returns the respected  list char : listofencryptedplugboards its simple as fouck u fool

def incremnt():

    global a
    global b  
    global c  
    global d 
    global e 
    global f  
    global g  
    global h 
    global i  
    global j  
    global k  
    global l  
    global m  
    global n  
    global o  
    global p  
    global q 
    global r 
    global s  
    global t  
    global u 
    global v  
    global w 
    global x  
    global y  
    global z  

    a = a + 1
    if(a == 26):
        a = 0
    b =  b + 1
    if(b == 26):
        b = 0
    c =  c + 1
    if(c == 26):
        c = 0
    d = d + 1
    if(d == 26):
        d = 0
    e = e  + 1
    if (e == 26):
        e = 0
    f =  f + 1
    if(f == 26):
        f = 0
        incremnttwo()
    g =  g + 1
    if(g == 26):
        g = 0
    h = h + 1
    if(h == 26):
        h= 0
    i =  i + 1
    if(i == 26):
        i = 0
    j =  j + 1
    if(j == 26):
        j = 0
    k =  k + 1
    if(k == 26):
        k = 0
    l =  l + 1
    if(l == 26):
        l = 0
    m =  m + 1
    if(m == 26):
        m = 0
    n =  n + 1
    if(n == 26):
        n = 0
    o =  o + 1
    if(o == 26):
        o = 0
    p =  p + 1
    if(p == 26):
        p = 0
    q =  q + 1
    if(q == 26):
        q = 0
    r = r + 1
    if(r == 26):
        r = 0
    s =  s + 1
    if(s == 26):
        s = 0
        #incremnttwo()

    t = t + 1
    if(t == 26):
        t = 0 
    u = u + 1
    if(u == 26):
        u = 0
    v = v + 1
    if(v == 26):
        v = 0 
    w = w + 1
    if(w == 26):
        w = 0
    x = x + 1
    if(x == 26):
        x = 0
    y = y + 1
    if(y == 26):
        y = 0 
    z = z + 1
    if(z == 26):
        z = 0 



def incremnttwo():
    global at
    global bt  
    global ct  
    global dt 
    global et 
    global ft  
    global gt  
    global ht 
    global it  
    global jt  
    global kt  
    global lt  
    global mt  
    global nt  
    global ot  
    global pt  
    global qt 
    global rt 
    global st  
    global tt  
    global ut 
    global vt  
    global wt 
    global xt  
    global yt  
    global zt  

    at = at + 1
    if(at == 26):
        at = 0
    bt =  bt + 1
    if(bt == 26):
        bt = 0
    ct =  ct + 1
    if(ct == 26):
        ct = 0
    dt = dt + 1
    if(dt == 26):
        dt = 0
    et = et  + 1
    if (et == 26):
        et = 0
    ft =  ft + 1
    if(ft == 26):
        ft = 0
    gt =  gt + 1
    if(gt == 26):
        gt = 0
    ht = ht + 1
    if(ht == 26):
        ht= 0
    it =  it + 1
    if(it == 26):
        it = 0
    jt =  jt + 1
    if(jt == 26):
        jt = 0
    kt =  kt + 1
    if(kt == 26):
        kt = 0
    lt =  lt + 1
    if(lt == 26):
        lt = 0
    mt =  mt + 1
    if(mt == 26):
        mt = 0
    nt =  nt + 1
    if(nt == 26):
        nt = 0
    ot =  ot + 1
    if(ot == 26):
        ot = 0
    pt =  pt + 1
    if(pt == 26):
        pt = 0
    qt =  qt + 1
    if(qt == 26):
        qt = 0
    rt = rt + 1
    if(rt == 26):
        rt = 0
    st =  st + 1
    if(st == 26):
        st = 0
        

    tt = tt + 1
    if(tt == 26):
        tt = 0 
    ut = ut + 1
    if(ut == 26):
        ut = 0
    vt = vt + 1
    if(vt == 26):
        vt = 0 
    wt = wt + 1
    if(wt == 26):
        wt = 0
    xt = xt + 1
    if(xt == 26):
        xt = 0
    yt = yt + 1
    if(yt == 26):
        yt = 0 
    zt = zt + 1
    if(zt == 26):
        zt = 0 




def rotorone(rone):
    
    rouoronelist = ["m" , "x" ,"t" , "l" , "h" , "v" , "o" , "p", "z" , "n" , "b" , "c" , "e" , "k" , "u" , "f" , "k" , "i" , "y", "d" , "g" , "q" , "s" , "t" , "w" , "a"]


    if(rone == "a"):
        return rouoronelist[a]
        
    if(rone == "b"):
        return rouoronelist[b]
    if(rone == "c"):
        return rouoronelist[c]
    if(rone == "d"):
        return rouoronelist[d]
    if(rone == "e"):
        return rouoronelist[e]
    if(rone == "f"):
        return rouoronelist[f]
    if(rone == "g"):
        return rouoronelist[g]
    if(rone == "h"):
        return rouoronelist[h]
    if(rone == "k"):
        return rouoronelist[k]
    if(rone == "i"):
        return rouoronelist[i]
    if(rone == "j"):
        return rouoronelist[j]
    if(rone == "j"):
        return rouoronelist[j]
    if(rone == "l"):
        return rouoronelist[l]
    if(rone == "m"):
        return rouoronelist[m]
    if(rone == "n"):
        return rouoronelist[n]
    if(rone == "o"):
        return rouoronelist[o]
    if(rone == "p"):
        return rouoronelist[p]
    if(rone == "q"):
        return rouoronelist[q]
    if(rone == "r"):
        return rouoronelist[r]
    if(rone == "s"):
        return rouoronelist[s]
    if(rone == "t"):
        return rouoronelist[t]
    if(rone == "u"):
        return rouoronelist[u]
    if(rone == "v"):
        return rouoronelist[v]
    if(rone == "w"):
        return rouoronelist[w]
    if(rone == "x"):
        return rouoronelist[x]
    if(rone == "y"):
        return rouoronelist[y]
    if(rone == "z"):
        return rouoronelist[z]
    else:
        return rouoronelist[w]

def rotortwo(rtwo):
    rouoronelist = ['t', 'l', 'o', 'z', 's', 'a', 'y', 'g', 'x', 'b', 'k', 'p', 'e', 'v', 'd', 'm', 'h', 'i', 'n', 'w', 'c', 'u', 'q', 'f', 'k', 't']
    


    if(rtwo == "a"):
        return rouoronelist[at]
        
    if(rtwo == "b"):
        return rouoronelist[bt]
    if(rtwo == "c"):
        return rouoronelist[ct]
    if(rtwo == "d"):
        return rouoronelist[dt]
    if(rtwo == "e"):
        return rouoronelist[et]
    if(rtwo == "f"):
        return rouoronelist[ft]
    if(rtwo == "g"):
        return rouoronelist[gt]
    if(rtwo == "h"):
        return rouoronelist[ht]
    if(rtwo == "k"):
        return rouoronelist[kt]
    if(rtwo == "i"):
        return rouoronelist[it]
    if(rtwo == "j"):
        return rouoronelist[jt]
    if(rtwo == "j"):
        return rouoronelist[jt]
    if(rtwo == "l"):
        return rouoronelist[lt]
    if(rtwo == "m"):
        return rouoronelist[mt]
    if(rtwo == "n"):
        return rouoronelist[nt]
    if(rtwo == "o"):
        return rouoronelist[ot]
    if(rtwo == "p"):
        return rouoronelist[pt]
    if(rtwo == "q"):
        return rouoronelist[qt]
    if(rtwo == "r"):
        return rouoronelist[rt]
    if(rtwo == "s"):
        return rouoronelist[st]
    if(rtwo == "t"):
        return rouoronelist[tt]
    if(rtwo == "u"):
        return rouoronelist[ut]
    if(rtwo == "v"):
        return rouoronelist[vt]
    if(rtwo == "w"):
        return rouoronelist[wt]
    if(rtwo == "x"):
        return rouoronelist[xt]
    if(rtwo == "y"):
        return rouoronelist[yt]
    if(rtwo == "z"):
        return rouoronelist[zt]
    else:
        return rouoronelist[wt]
#temporoy fix
#i have created this function simple where it just match the char and return the recpected index char

def rotorthree(rthree):
    rouoronelist = ['t', 'l', 'o', 'z', 's', 'a', 'y', 'g', 'x', 'b', 'k', 'p', 'e', 'v', 'd', 'm', 'h', 'i', 'n', 'w', 'c', 'u', 'q', 'f', 'k', 't']
    


    if(rthree == "a"):
        return rouoronelist[at]
        
    if(rtwo == "b"):
        return rouoronelist[bt]
    if(rtwo == "c"):
        return rouoronelist[ct]
    if(rtwo == "d"):
        return rouoronelist[dt]
    if(rtwo == "e"):
        return rouoronelist[et]
    if(rtwo == "f"):
        return rouoronelist[ft]
    if(rtwo == "g"):
        return rouoronelist[gt]
    if(rtwo == "h"):
        return rouoronelist[ht]
    if(rtwo == "k"):
        return rouoronelist[kt]
    if(rtwo == "i"):
        return rouoronelist[it]
    if(rtwo == "j"):
        return rouoronelist[jt]
    if(rtwo == "j"):
        return rouoronelist[jt]
    if(rtwo == "l"):
        return rouoronelist[lt]
    if(rtwo == "m"):
        return rouoronelist[mt]
    if(rtwo == "n"):
        return rouoronelist[nt]
    if(rtwo == "o"):
        return rouoronelist[ot]
    if(rtwo == "p"):
        return rouoronelist[pt]
    if(rtwo == "q"):
        return rouoronelist[qt]
    if(rtwo == "r"):
        return rouoronelist[rt]
    if(rtwo == "s"):
        return rouoronelist[st]
    if(rtwo == "t"):
        return rouoronelist[tt]
    if(rtwo == "u"):
        return rouoronelist[ut]
    if(rtwo == "v"):
        return rouoronelist[vt]
    if(rtwo == "w"):
        return rouoronelist[wt]
    if(rtwo == "x"):
        return rouoronelist[xt]
    if(rtwo == "y"):
        return rouoronelist[yt]
    if(rtwo == "z"):
        return rouoronelist[zt]
    else:
        return rouoronelist[wt]


#Main body 

userInput = input("Enter Your String To Encode : ")



for userip in userInput:         # converting user input into an array 
    arr.append(userip)



for lenofarr in range(len(arr)):

    plugboardchar = PlugBoard(arr[lenofarr])
    if not plugboardchar:
        PlugBoardlist.append(arr[lenofarr]) 
    
    
    PlugBoardlist.append(plugboardchar)

filtered_list = [item for item in PlugBoardlist if item is not None] #removing none char 

for lenoffilterlist in range(len(filtered_list)):
    
    #print(filtered_list[lenoffilterlist] , " : Filterd list")
    Roteres = rotorone(filtered_list[lenoffilterlist])
    incremnt()

    #print(Roteres, "Rotor 1 response")
    Roteres_list.append(Roteres)

for test in range(len(Roteres_list)):
    print(Roteres_list[test] , " : From rotor 1 ")
    rotortwores = rotortwo(Roteres_list[test])
    print(Roteres_list[test], " : Sent to Rotor 2")
    print(rotortwores , " : From rotor 2 ")
    rotortworeslist.append(rotortwores)

for charinrtwo in range(len(rotortworeslist)):
    print(rotortworeslist[charinrtwo] ," : thats rotor two response")
    rotortworeslist

