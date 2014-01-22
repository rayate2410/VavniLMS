from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
import sqlite3
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
import os

path_to_db = os.path.dirname(os.path.dirname(__file__))+"/HelloDjango/vavnilmsdb.sqlite3"

def test_method(request):
    return HttpResponse("This iasdass Spa!")

def index(request):
    return render_to_response("apply_for_leave.html", "text/html")

@csrf_exempt
def apply_for_leave(request):
    
    desc = request.POST['description']
    date_from = request.POST['date_from']
    date_to = request.POST['date_to']
    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()
    
    query = "INSERT INTO leaves_info VALUES("+str(1)+","+date_from+","+date_to+","+str(3)+","+desc+","+"pending"+")"
    #cursor.execute(query)
    
    #query = "SELECT status FROM leaves_info where employee_id="+1+"LIMIT 1"
    #cursor.execute(query)
    #row = cursor.fetchone()
    #status = row["status"]
    response_dict = {}
    #response_dict.update({'stat': 'ok', 'status' : status})
    response_dict.update({'stat': 'ok', 'description' : desc, 'date_from' : date_from , "date_to" : date_to })                                                                  
    return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    