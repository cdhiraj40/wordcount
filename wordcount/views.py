

from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def loginpage(request):
    return HttpResponse('PLease Enter Your Username'
                        'AND Choose your password')

def aboutpage(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    word_dict={}
    for word in wordlist:
        if word in word_dict:
            #increase
            word_dict[word]+=1
        else:
            #add to dict
            word_dict[word] = 1
    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)


    return render(request,'count.html',{'fulltext':fulltext ,'count':len(wordlist),'word_dict':sorted_words})