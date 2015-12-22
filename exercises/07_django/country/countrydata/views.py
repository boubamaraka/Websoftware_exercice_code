from django.http import Http404,HttpResponse,HttpResponseNotFound
from countrydata.models import Continent,Country
import json
from django.core import serializers

from .models import Continent, Country


def continent_json(request, continent_code):
    """ Write your answer in 7.2 here. """
    #continent=dict()
    #c=Continent.objects.filter(code__exact=continent_code)
    #print Continent.objects.get(code__exact=continent_code)
    if Continent.objects.filter(code__exact=continent_code):
        #print Country.objects.all(continent_code)
        continent= serializers.serialize('json', Continent.objects.filter(code__exact=continent_code))
        continent1=[]
        jfile={}
        jfile=json.loads(continent)
        #print jfile
        for i in jfile:
            continent1.append(i["fields"])
            c=i["pk"]
        data=Country.objects.filter(continent=c)
        cont={}
        for i in data:
            cont [i.code]=i.name
        cont=json.dumps(cont)
        callback=request.GET.get('callback')
        #if c==data.continent:
        #print c
        if callback:
            cont= '%s(%s)' % (callback, cont)
            return HttpResponse(cont,content_type="application/json")
        else:
            return HttpResponse(cont,content_type="application/json")
        #else:
            #return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


def country_json(request, continent_code, country_code):
        try:
            continent =Continent.objects.get(code=continent_code)
            country =Country.objects.get(code=country_code)
            if country.continent.code !=continent_code:
                return HttpResponseNotFound('<h1>Page not found</h1>')
            else:

                country= serializers.serialize('json', Country.objects.filter(code__exact=country_code))
                country1=[]

                jfile={}
                jfile=json.loads(country)
                #print jfile
                for i in jfile:
                    country1.append(i["fields"])
                    #c=i["pk"]
                    countryoriginal={}
                    for j in country1:
                        countryoriginal["area"]=j.get("area")
                        countryoriginal["population"]=j.get("population")
                        countryoriginal["capital"]=j.get("capital")
                    #print countryoriginal
                    countryoriginal=json.dumps(countryoriginal)
                    callback=request.GET.get('callback')

                    #if(Continet.objects.get(pk=c))
                    if callback:
                         countryoriginal= '%s(%s)' % (callback, countryoriginal)
                        #countryoriginal="{0}({1})".format(callback,countryoriginal)
                         return HttpResponse(countryoriginal,content_type="application/json")
                    else:

                        return HttpResponse(countryoriginal,content_type="application/json")

        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    #else:
        #return HttpResponseNotFound('<h1>Page not found</h1>')
