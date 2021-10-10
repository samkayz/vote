from django.http import response
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.views.generic.base import View
from function.func import Main, get_client_ip
from django.shortcuts import render
from django.core import serializers
from vote.models import AnnouncedPUResult, Lga, PollingUnit
from django.http import HttpResponse
from datetime import datetime



base_date_time = datetime.now()
now = (datetime.strftime(base_date_time, "%Y-%m-%d:%H:%M:%S"))


func = Main()



# IndexPage Handle rendering of landing page
class IndexPage(TemplateView):
    template_name = 'index.html'
    
    def get(self, request):
        response = func.get_data()
        show = response['show']
        agentname = response['agentname']
        party = response['party']
        return render(request, self.template_name, {'show':show, 'agentname':agentname, 'party':party})
    
    def post(self, request):
        if request.method == "POST":
            state_id = request.POST['state_id']
            get_queryset = Lga.objects.filter(state_id=state_id)
            data = serializers.serialize('json', get_queryset)
            #print(data)
            return HttpResponse(data)
        


# GetPollingUnit handle getting of polling Unit and serialized it the data recieved
class GetPollingUnit(View):
    def post(self, request):
        if request.method == "POST":
            lga_id = request.POST['lga_id']
            get_queryset = PollingUnit.objects.filter(lga_id=lga_id)
            data = serializers.serialize('json', get_queryset)
            #print(data)
            return HttpResponse(data)
        

# GetPUResult handle getting of result for a particular polling unit base on user input
class GetPUResult(TemplateView):
    template_name = 'result.html'
    def post(self, request):
        if request.method == "POST":
            polling_unit_id = request.POST['pollingunit']
            results = AnnouncedPUResult.objects.filter(polling_unit=polling_unit_id)
            return render(request, self.template_name, {'results':results})
        
        


#GetResultByLGA handle getting of result base on Selected LGA        
class GetResultByLGA(TemplateView):
    template_name = 'pu_results.html'
    def post(self, request):
        if request.method == "POST":
            lga_id = request.POST['lgas']
            
            try:
                response = func.result_by_lga(lga_id)
            
                final_result = response[0]
                lga = response[1]
                state = response[2]
                sum_total = response[3]
                return render(request, self.template_name, {'party_scores':final_result, 
                                                        'lga':lga, 'sum_total':sum_total})
            except:
                data = "No Results Found"
                return render(request, self.template_name, {'polling_unit_name':data})



# AddResult is use to input result of a polling unit into the system
class AddResult(View):
    def post(self, request):
        if request.method == "POST":
            ip = get_client_ip(request)
            score = request.POST['score']
            party = request.POST['party']
            polling_unit_id = request.POST['pollingunitres']
            entered_user = request.POST['agentname']
            
            resp = func.add_result(polling_unit_id, party, score, entered_user, now, ip)
            if resp == True:
                messages.success(request, "Result Added")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Oops!! Something Went Wrong")
                return HttpResponseRedirect('/')
            