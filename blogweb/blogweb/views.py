from django.shortcuts import render
from blogger.models import post



def home(request):
    return render(request, "index.html")
def headers(request):
    return render(request, "header.html")


def blog(request, slug, status):
    postdata=post.objects.get(slug=slug)
    
    a=postdata
   

    
    data={  'title': a.title,
           'author': a.author,
           'publish': a.publish,
           'description' : a.description,
           'body': a.body
            }
    
        
    
    if status=='world':
        return render(request, "blogs/world.html", data)
    elif status=='india':
        return render(request, "blogs/india.html", data)
    elif status=='business':
        return render(request, "blogs/business.html", data)
    elif status=='politics':
        return render(request, "blogs/politics.html", data)
    elif status=='technology':
        return render(request, "blogs/technology.html", data)
    elif status=='travel':
        return render(request, "blogs/travel.html", data)
    elif status=='science':
        return render(request, "blogs/science.html", data)



def status(request, status):
    postdata=post.objects.filter(status=status)
    a=list(postdata)
    data=[]
    for x in a:
        temp={
            'title' : x.title,
            'body' : x.body,
            'slug' : x.slug,
            'description' : x.description,
            'status' : x.status
        }
        data.append(temp)
    return render(request, "base.html", {'data': data})

    
    # if status=='world':
    #     return render(request, "world.html", {'data': data})
    # elif status=='india':
    #     return render(request, "india.html", {'data': data})
    # elif status=='business':
    #     return render(request, "business.html", {'data': data})
    # elif status=='politics':
    #     return render(request, "politics.html", {'data': data})
    # elif status=='technology':
    #     return render(request, "technology.html", {'data': data})
    # elif status=='travel':
    #     return render(request, "travel.html", {'data': data})
    # elif status=='science':
    #     return render(request, "science.html", {'data': data})