from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse, response
from .forms import *
import json
import pandas as pd
from django.db.models import Max, Min, Sum
import csv
import static
# Create your views here.



class HomePageView(TemplateView):
    def get(self, request):
        return render(request, 'Home.html')

def dataset(request):
    myquery = Document.objects.values('description','uploaded_at')
    if request.method == 'POST':
        
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            our_form = form.save(commit=False)
            
            files = request.FILES['document']
            our_form.description = files
            
            our_form.save()
            return redirect('/app/dataset/')
    else:   
        form = DocumentForm()
        return render(request, 'Upload.html', {
        'form': form,'myquery':myquery
    })


def save_data(request):
    mydata = request.POST.get("valuedict")
    mydict = json.loads(mydata)
    # print(mydict,"===============",type(mydict))
    if mydict['op']== "Max":
        obj = Document.objects.get(description=mydict['file'])
        file =open("media/{}".format(obj.document))
        df = int((pd.read_csv(file, usecols = [mydict['col']])).max())
        json_data = json.dumps(str(df))
        file.close()
        return JsonResponse({'json_data':json_data},safe=False)
    if mydict['op']== "Min":
        obj = Document.objects.get(description=mydict['file'])
        file =open("media/{}".format(obj.document))
        df = int((pd.read_csv(file, usecols = [mydict['col']])).min())
        json_data = json.dumps(str(df))
        file.close()
        return JsonResponse({'json_data':json_data},safe=False)
    if mydict['op']== "Sum":
        obj = Document.objects.get(description=mydict['file'])
        file =open("media/{}".format(obj.document))
        df = int((pd.read_csv(file, usecols = [mydict['col']])).sum())
        json_data = json.dumps(str(df))
        file.close()
        return JsonResponse({'json_data':json_data},safe=False)
import ast 
def plot_data(request):
    mydata = request.POST.get("valuedict")
    mydict = json.loads(mydata)
    new_dict = {}
    obj = Document.objects.get(description=mydict['file'])
    file =open("media/{}".format(obj.document))
    df1 = pd.read_csv(file, usecols = [mydict['col1'],mydict['col2']])
    new_dict['list1'] = df1["Col1"].tolist()
    new_dict['list2'] = df1["Col2"].tolist()
    json_data = json.dumps(new_dict)
    return JsonResponse({'json_data1':json_data},safe=False)
  


class plot_and_commute(TemplateView):
    def get(self, request):
        myquery =Document.objects.values('description')
        return render(request, 'Data_V.html',{'myquery':myquery})

    def post(self, request):
        myquery =Document.objects.values('description')
        return render(request, 'Data_V.html',{'myquery':myquery})