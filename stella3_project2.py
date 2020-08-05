import operator
import sys

ccount=0


def merge_and(result,b):
    temp=[]
    size_1 = len(result) 
    size_2 = len(b)
    comp=0
    i, j = 0, 0
    while i < size_1 and j < size_2:
        if result[i] == b[j]: 
            temp.append(result[i]) 
            i+=1
            j+=1
            comp+=1
        elif result[i]>b[j]:
            j+=1
            comp+=1
        else:
            i+=1
            comp+=1
                
    return temp,comp


def merge_or(result,b):
    temp=[]
    temp=list(set(result) | set(b))
    temp.sort()
    size_1 = len(result) 
    size_2 = len(b)
    comp=0
    i, j = 0, 0  
    while i < size_1 and j < size_2:
        if result[i] == b[j]: 
            i+=1
            j+=1
            comp+=1
        elif result[i]>b[j]:
            j+=1
            comp+=1
        else:
            i+=1
            comp+=1
                
    return temp,comp


               
def DaatAND(test2):
    a=[]
    print('DaatAnd')
    
    fcomp=0
    for i in test2:
        a.append(posting_dict[i])
    z=[]
    for i in test2:
        z.append(i)
    for i in range(0,len(z)):
        if(i!=len(z)-1):
            print(z[i],"",end="")
        else:
            print(z[i])   
    #a.sort(key=len)
    result=a[0]
    for i in range (1,len(a)):
        b=a[i]
        res=merge_and(result,b)
        result=res[0]
        fcomp=fcomp+res[1]       
    #print(result)
    numterm=len(result)
    #print("Results:",end="")
    #print(k)
    #sank=0
  
    if(numterm==0):
            print('Results: empty')
    else:
        print('Results: ',end="")
        for i in range(0,numterm):
            if(i!=numterm-1):
                print(result[i],"",end="")
            else:
                print(result[i])
    print("Number of documents in results: ",end="")
    print(numterm)
    
    print("Number of comparisons: ",end="")
    print(fcomp)
    #print(fcomp)
    tfidf_and(work,result)
      
    
def DaatOR(test2,lcount):
    a=[]
    fcomp=0
    print('DaatOr')
    
    for i in test2:
        a.append(posting_dict[i])
    #a.sort(key=len)
    z=[]
    for i in test2:
        z.append(i)
    for i in range(0,len(z)):
        if(i!=len(z)-1):
            print(z[i],"",end="")
        else:
            print(z[i])
    result=a[0]
    for i in range (1,len(a)):
        b=a[i]
        res=merge_or(result,b)
        result=res[0]
        fcomp=fcomp+res[1]
    #print(result)
    #print(fcomp)
    numterm=len(result)
    print('Results: ',end="")
    for i in range(0,numterm):
        if(i!=numterm-1):
            print(result[i],"",end="")
        else:
            print(result[i])
    
    
    
    
    print("Number of documents in results: ",end="")
    print(numterm)
    
    print("Number of comparisons: ",end="")
    print(fcomp)
    tfidf_or(work,result,lcount)

    
def tfidf_and(work,result):
    #print('hi')
    a=[]
    print('TF-IDF')
    print("Results:",end="")
    num_idf=len(pre_dict)
    den_idf=len(result)
    if len(result)==0:
        print("",'empty')
    else:
        idf=num_idf/den_idf
        tf_idf={}
        for i in work:
            a.append(i)
        #print('hellllloooo')
        for i in result:
            k=0
            for j in a:
                k=k+tf_dict[i+'_'+j]
            k=k*idf
            tf_idf.update({i:k})
        #print(tf_idf)
        #print('hiiiii')
        sorted_d = sorted(tf_idf.items(), key=operator.itemgetter(1))
        #print(sorted_d)
        x=[]
        for i in sorted_d:
            x.append(i[0])
        #x.sort()
        #print(x)
        x.reverse()
        for l in x:
            #sank+=1
            #if(sank<=lan-1):
            print("",l,end="")
            #else:
        print("")
        
        
        
        #print(x)    
        #print(type(sorted_d))
        #return sorted_d


def tfidf_or(work,result,lcount):
    
    a=[]
    t1={}
    idf=0
    print('TF-IDF')
    print("Results:",end="")
    global ccount
    ccount=ccount+1
   
    for i in work:
        a.append(i)
    for i in result:
        k=0
        idf=0
        n=0
        for j in a:
            if j in pre_dict[i]:
                k=tf_dict[i+'_'+j]
                idf=(len(pre_dict)/len(posting_dict[j]))
                m=k*idf
                n=n+m
        #m=k*idf
                
        t1.update({i:n})
    #print(t1)
    sorted_d = sorted(t1.items(), key=operator.itemgetter(1))
    x=[]
    for i in sorted_d:
        x.append(i[0])
    #x.sort()
    #print(x)
    x.reverse()
    #print(x)
    if ccount!=lcount:
        for l in x:
                #sank+=1
                #if(sank<=lan-1):
            print("",l,end="")
                #else:
        print("")
    else:
        for l in x:
                #sank+=1
                #if(sank<=lan-1):
            print("",l,end="")
        



def generate_list(key,pre_dict):
     l=pre_dict[key]    
     for i in l:
         a=[]
         n=0
         for k in check:
            if k==i:
              n=n+1
         if n==0:
           check.append(i)
           a.append(key)
           posting_dict.update({i:a})
         else:
             c=posting_dict[i]
             c.append(key)
             posting_dict.update({i:c})
             


def main():
    corp_in=sys.argv[1]
    out=sys.argv[2]
    
    f = open(out,'w')
    sys.stdout = f
    with open(corp_in) as corpusopen:
       for line in corpusopen:
         p=[]
         t=line.split()
         len_of_line=len(t)
         len_of_line=len_of_line-1
         for i in t:
           count=0
           if t[0]!=i:
             #k=i.translate({ord(j): None for j in '.,!?:;'})
             #k=i.lower()
             d=t[0]
             d=d+'_'+i
             count=t.count(i)
             count=count/len_of_line
             tf_dict.update({d:count})
             p.append(i)
         res=[] 
         res1=[]
         for i in p:
           res1.append(i)
         idf_dict.update({t[0]:res1})
         for i in p:
           if i not in res: 
               res.append(i)
         pre_dict.update({t[0]:res})
       
    for key in pre_dict:
         #print(posting_dict[key])
         generate_list(key,pre_dict)
if __name__ == "__main__":
    pre_dict={}
    tf_dict={}
    posting_dict={}
    add={} 
    check=[]
    idf_dict={}
    main()
    for keys,values in posting_dict.items():
        values.sort()
    inp=sys.argv[3]
    #ind=0
    #print(pre_dict)    
    #print(posting_dict)
    #print(check)
    #print(tf_dict)
    with open(inp) as testfile:
        #mbrk=0
        ind=0
        lcount=sum(1 for line in open(inp))
        for line in testfile:
            test=[]
            test1=[]
            #lcount=lcount+1
            t=line.split()
            brk=0
            work={}
                #count=len(test)
                #print(count)
            for i in t:
                test1.append(i)
                
                #print(ind)
                
                k=[]
                k=posting_dict[i]
                work.update({i:k})
                
                #lan=len(k)
                #print(\n)
                if brk==0 and ind==0:
                    brk=1
                    ind=1
                    print('GetPostings')
                elif ind==1 and brk==0:
                    brk=1
                    print('\nGetPostings')
                else:
                    print('GetPostings')
                    
                print(i)
                print("Postings list:",end="")
                #print(k)
                #sank=0
                for l in k:
                    #sank+=1
                    #if(sank<=lan-1):
                    print("",l,end="")
                    #else:
                print("")
            #print(work)
            for keys,values in work.items():
                values.sort()
            DaatAND(test1)
            DaatOR(test1,lcount)
            #tfidf(y,z)            
    #print(pre_dict)    
    #print(posting_dict)
    #print(check)
    #print(tf_dict)
    #print(idf_dict)
    #out=input("Output Path")

