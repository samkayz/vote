from vote.models import *
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.http import JsonResponse



"""Sum all the Vote"""

def returnSum(dict):
    sum = 0
    # print(dict)
    for i in dict:
        sum = sum + i['total_vote']
    return sum


"""Get IP of User"""
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # print ("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        # print ("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        # print ("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip


 
 
"""Main class that handle the process flow of the system"""
class Main: 
    
    #Function that get data from the DB        
    def get_data(self):
        show = State.objects.filter()
        agentname = AgentName.objects.filter()
        party = Party.objects.filter()
        data = {
            "show":show,
            "agentname": agentname,
            "party": party
        }
        return data
    
    
    #Function the handle result by selected LGA
    def result_by_lga(self, lga_id):
        lga = get_object_or_404(Lga, lga_id=lga_id)
        state = get_object_or_404(State, id=lga_id)
        punit = PollingUnit.objects.filter(lga_id=lga_id)
        
        final_result = []
        for pollunit in punit:
            data = {}
            total_vote = AnnouncedPUResult.objects.filter(polling_unit=pollunit.polling_unit_id).aggregate(Sum('party_score'))['party_score__sum']
            data['pollingUnitName'] = pollunit.polling_unit_name
            if total_vote == None: continue
            
            
            data['total_vote'] = total_vote
            # data['polling_unit_name'] = "Polling Unit Name: {} \nPolling Unit NO: {}".format(pollunit.polling_unit_name, pollunit.polling_unit_number)
            final_result.append(data)
        # print(final_result)
            
        
        sum_total = returnSum(final_result)
        
        return final_result,  lga, state, sum_total
    
    
    #Function the Handle Adding of result to the System
    def add_result(self, polling_unit, party_abbreviation, party_score, entered_by_user, date_entered, user_ip_address):
        add = AnnouncedPUResult(
            polling_unit=polling_unit, 
            party_abbreviation=party_abbreviation, 
            party_score=party_score, 
            entered_by_user=entered_by_user,
            date_entered = date_entered,
            user_ip_address=user_ip_address
            )
        add.save()   
        return True  