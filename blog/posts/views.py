from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
posts =[
    {
        'id': 1,
        'title': 'Chunghua Aluminium',
        'content': 'Chunghua Aluminium is located in Dhaka, Bangladesh. They specialize in the production of high-quality aluminium profiles, used for doors, windows, and various industrial applications. The company is known for its durable and reliable products in the construction sector.'
    },
    {
        'id': 2,
        'title': 'Dhaka Thai Aluminium',
        'content': 'Dhaka Thai Aluminium is one of the leading aluminium companies in Bangladesh, based in Gazipur. They manufacture a wide range of aluminium products including profiles for doors, windows, and curtain walls. The company is a key supplier to both domestic and international markets.'
    },
    {
        'id': 3,
        'title': 'Alco Aluminium',
        'content': 'Alco Aluminium is situated in Chittagong, Bangladesh. Their product line includes aluminium sheets, extrusions, and coils, which are used in the construction, automotive, and packaging industries. Alco is known for its innovative solutions and sustainable practices.'
    },
]

def home(request):

    return render(request,'posts/home.html',{'username': 'farzana'})


def blog(request):
    html=""
    for post in posts:
        html += f'''
            <div>
            
            <a href="/post/{post['id']}"> 
                <h1>{post['id']} - {post['title']}</h1></a>
                <p> {post['content']}</p>
            
            </div>
        
        '''
    return render(request,'posts/blog.html',{'posts': posts}) 


def post(request,id):
    print(type(id))
    return HttpResponse(f"{id}")

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] ==id:
            post_dict = post
            valid_id = True
            break
    if valid_id:   

        return render(request, "posts/post.html", {'post_dict': post_dict})
    else:
        #return  HttpResponseNotFound("<h1>Post not Available :)</h1>")
        raise Http404()
    
    
    
            
#HttpResponseRedirect class to access another url for price
def price(request):
    return HttpResponseRedirect('https://www.banglastall.com/filter/Construction/Thai-Aluminium/ALCO')

def google(request,id):
    #Using reverse function to dynamically generate the urls
    url = reverse("post",args=[id])
    return HttpResponseRedirect(url)
    # return HttpResponseRedirect(f'/posts/{id}/')
    
def about(request):
    return render(request, 'posts/about.html')

def contact(request):
    return render(request, 'posts/contact.html')  

#redirects users to login url if they are not logged in
@login_required(login_url='users:login')
def post_new(request):
    return render(request, 'posts/post_new.html')

