from django.db import connection
import pandas as pd
from requests import request
from django.http.response import JsonResponse
import json
from main.models import Population_by_countries as PBC
# Create your views here.

def TableView(request, id):

    #Dataframe
    df = pd.DataFrame(list(PBC.objects.all().values()))
    df = df.pivot_table('data', ['country_name', 'code'], 'year')
    df.reset_index( drop=False, inplace=True )
    ann = 0
    for i in range(0,len(df)):
        ann = df[id].fillna(0) - df[id-1].fillna(0)


    
    country_name = [i for i in df['country_name']]
    score = [i for i in df[id].fillna(0)]
    annual = [i for i in ann]


    a = {}
    for i in range(1,len(country_name)+1):
        a[ i ] = country_name[i-1]
    country_name = a

    b = {}
    for i in range(1,len(score)+1):
        b[ i ] = score[i-1]
    score = b
  
    global_rank = [1]
    
    for i in range(1, len(country_name)+1):
        s = score[i]
    
        sorted_score = [1]
        sorted_rnk = [1]

        sort_score = sorted(score.items(), key=lambda x: x[1], reverse=True)
     
        rnk = 1
        n = 1
        for j in sort_score:
            
            scr = j[1]

            if n ==1:
                sorted_score.append(scr)
                sorted_rnk.append(rnk)
            
            else:
                if scr==sorted_score[n-1]:
                    sorted_score.append(scr)
                    sorted_rnk.append(rnk)
                elif scr<sorted_score[n-1]:
                    rnk+=1
                    sorted_score.append(scr)
                    sorted_rnk.append(rnk)
                else:
                    raise('Error')
                    
            
            n+=1
            
        index = sorted_score.index(s)
        rankk = sorted_rnk[index]

        global_rank.append(rankk)
    
    
    c = {}
    for i in range(1,len(annual)+1):
        c[ i ] = annual[i-1]
    annual = c

   
    data = []
  
    for i in range(1, len(country_name)+1):
        data.append({'id':i, 'country': country_name[i],'score': score[i],'annual': annual[i], 'rank': global_rank[i]})
    table_data = data


    if request.method == 'GET':
        return JsonResponse(table_data, safe=False)

  


        
    
    
 


    
