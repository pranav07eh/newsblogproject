from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    data = {
        'blogsData':Blog.objects.all()
    }
    return render(request, 'index.html', data)
 
def about(request):
    return render(request, 'about.html')

def addnews(request):
    if request.method=="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = ''
        if request.FILES:
            image = request.FILES['image']
        Blog.objects.create(title=title,desc=description,image=image)
        return redirect('index')
    else:
        return render(request, 'addnews.html')
    
def newsdetails(request,id):
    data={
        'blog':Blog.objects.get(id=id)
    }    
    return render(request,'newsdetails.html',data)

def contact(request):
    return render(request, 'contact.html')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'desc', 'image'] 
    template_name = 'update_blog.html' 
    context_object_name = 'blog' 

    def form_valid(self, form):
        print(f"Form is valid, updating blog: {form.instance.title}")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('newsdetails', kwargs={'id': self.object.id})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('index')
    


