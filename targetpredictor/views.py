from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from mirna.models import * 

import json

# Create your views here.

def toJSON(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')


def mirna_view(request) :

    # get mirna list	
    if request.method == 'GET' :
        sts = mirna.objects.all()
        total = mirna.objects.all().count()

        rst = {}

        data = []

        for st in sts : 
            st_info = {}
            st_info['id'] = st.id
            st_info['name'] = st.name
            st_info['seq'] = st.seq
            data.append(st_info)

        rst['data'] = data
        rst['total'] = total

    elif request.method == 'POST' : 
        name = request.POST.get('name')
        seq = request.POST.get('seq')

        st = mirna()
        st.name = name
        st.seq = seq
        st.save()

        rst = {}
        rst['id'] = st.id
        rst['msg'] = 'OK'    
   
    return toJSON(rst, 200)

def mirna_detail_view(request, id) :

    if request.method == 'GET' : 
        param_id = id	
        st = mirna.objects.get(id=param_id)

        rst = {}
        rst['id'] = st.id
        rst['name'] = st.name
        rst['seq'] = st.seq

    elif request.method == 'PUT' :
        put = QueryDict(request.body)
        
        param_id = id
        param_name = put.get('name')
        param_seq = put.get('seq')

        st = mirna.objects.get(id=param_id)
        if param_name != "" :
            st.name = param_name
        if param_seq != "" : 
            st.seq = param_seq
     
        st.save()   
      
        rst = {} 
        rst['id'] = st.id
        rst['name'] = st.name
        rst['seq'] = st.seq

    elif request.method == 'DELETE' :
        delete = QueryDict(request.body)
        
        param_id = id
        st = mirna.objects.get(id=param_id)
        st.delete()
     
        rst = {} 
        rst['msg'] = 'OK'

    return toJSON(rst, 200)
