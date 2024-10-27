from django.shortcuts import render

# Create your views here.
def context(request):
    context = {
        'text':"This is the sample text",
        'pageno':5,
        'items' : ['item1','item2','item3']
    }

    return render(request,'index.html',context)