from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from .models import Book
#批量添加数据
def add(request):
    #只有Y一个insert语句,性能更好
    booklist =[]
    for i in range(1,100):
        book = Book(title="book"+str(i),price=i*2)
        booklist.append(book)
    Book.objects.bulk_create(booklist)
    return HttpResponse("<h3>添加成功<h3>")
#让数据可以分页
def page(request):
    page_num = int(request.GET.get('page'))
    pag = Paginator(Book.objects.all(),8)#每一页有多少个数据
    book_num = pag.page(page_num)
    page_count = pag.page_range

    return render(request,'page.html',{'book_num':book_num,'page_num':page_num,'page_count':page_count,'pag':pag})
def page2(request):
     visit_page = int(request.GET.get('page'))
     pag = Paginator(Book.objects.all(), 2)
     page_visit = pag.page(visit_page)
     if visit_page == 1:
         on_page = range(1,4)
     elif visit_page == pag.num_pages:
         on_page = range(pag.num_pages -2,pag.num_pages +1)
     else:
         on_page = [visit_page -1,visit_page,visit_page +1]
     return render(request,'page2.html',{'on_page':on_page,'pag':pag,'visit_page':visit_page,"page_visit":page_visit})