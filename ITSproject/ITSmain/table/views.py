from django.db import connection
import pandas as pd
from requests import request
from django.http.response import JsonResponse
import json

# Create your views here.

def TableView(request, id):

    #SQLquery
    if id>2000:
        qry = f'SELECT  main_Country.country_name, main_Ipad.year{id}, (main_Ipad.year{id}-main_Ipad.year{id-1}) AS annual FROM main_Ipad, main_Country WHERE main_Ipad.country_id = main_Country.id'.format(id=id)

    else:
        qry = f'SELECT  main_Country.country_name, main_Ipad.year{id} FROM main_Ipad, main_Country WHERE main_Ipad.country_id = main_Country.id'.format(id=id)


    #Dataframe
    df = pd.read_sql_query(qry, connection)
    

    country_name = [i for i in df['country_name']]
    score = [i for i in df[f'year{id}'.format(id=id)]]
    if id>2000:
        annual = [i for i in df['annual']]


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
                    print(222525623661777774377474574574557)
            
            n+=1
            
        index = sorted_score.index(s)
        rankk = sorted_rnk[index]

        global_rank.append(rankk)
    
    if id>2000:
        c = {}
        for i in range(1,len(annual)+1):
            c[ i ] = annual[i-1]
        annual = c

    if id>2000:
        data = []
        for i in range(1, len(country_name)+1):
            data.append({'id':i, 'country': country_name[i],'score': score[i],'annual': annual[i], 'rank': global_rank[i]})
        table_data = data
       
    else:
        data = []
        for i in range(1, len(country_name)+1):
            data.append({'id':i, 'country': country_name[i],'score': score[i],'annual': 'no data', 'rank': global_rank[i]})
        table_data = data
    
    if request.method == 'GET':
        return JsonResponse(table_data, safe=False)

  


        
    
    
 


    
