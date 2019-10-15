from django.shortcuts import render, redirect,HttpResponse
from app01 import models


# Create your views here.


def publisher_list(request):
    ret = models.Publisher.objects.all()
    return render(request,"publisher_list.html",{'publisher_list':ret})


def add_publisher(request):
    error_msg = ""
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name',None)
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect("/publisher_list/")
        else:
            error_msg = '出版社名字不能为空'
    return render(request,"add_publisher.html",{'error':error_msg})


def del_publisher(request):
    del_id = request.GET.get("id",None)
    if del_id:
        models.Publisher.objects.get(id=del_id).delete()
        return redirect("/publisher_list/")
    else:
        return HttpResponse("页面不存在")


def edit_publisher(request):
    if request.method == 'POST':
        # 从提交的请求中获取修改项的id和修改后的出版社名
        edit_id = request.POST.get("id")
        new_name = request.POST.get('publisher_name')
        # 根据ID值确定编辑的是哪一项，修改那一项的名字
        edit_publisher_obj = models.Publisher.objects.get(id=edit_id)
        edit_publisher_obj.name = new_name
        edit_publisher_obj.save()
        # 返回出版社列表查看修改是否成功
        return redirect("/publisher_list/")
    # 从GET请求中的URL取得id值
    edit_id = request.GET.get("id")
    if edit_id:
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {'publisher': publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在")


def start(request):
    ret = models.Publisher.objects.all()
    return render(request, "start.html", {'publisher_list': ret})
    # return render(request, "Start.html")


def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, "book_list.html", {'all_book': all_book})


def add_book(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        models.Book.objects.create(title=new_title,publisher_id=new_publisher_id)
        return redirect("/book_list/")

    ret = models.Publisher.objects.all()
    return render(request, "add_book.html", {"publisher_list":ret})


def del_book(request):
    del_id = request.GET.get("id")
    if del_id:
        models.Book.objects.get(id=del_id).delete()
        return redirect("/book_list/")
    else:
        return HttpResponse("页面不存在")


def edit_book(request):
    if request.method == 'POST':
        edit_id = request.POST.get("id")
        new_title = request.POST.get('book_title')
        new_publisher = request.POST.get('publisher')
        # 根据ID值确定编辑的是哪一项，修改那一项的名字
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title
        edit_book_obj.publisher_id = new_publisher #更新书籍关联的出版社
        edit_book_obj.save()
        # 返回出版社列表查看修改是否成功
        return redirect("/book_list/")
    # 从GET请求中的URL取得id值
    edit_id = request.GET.get("id")
    if edit_id:
        edit_book_obj = models.Book.objects.get(id=edit_id)
        publisher_obj = models.Publisher.objects.all()
        return render(request, "edit_book.html", {'book_obj': edit_book_obj,'publisher_list':publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在")


def author_list(request):
    ret = models.Author.objects.all()
    return render(request, "author_list.html", {'author_list': ret})


def add_author(request):
    error_msg = ""
    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        # post提交的数据是多个值时，用getlist接受
        books = request.POST.getlist('books')
        if new_author_name:
            new_author_obj = models.Author.objects.create(name=new_author_name)
            new_author_obj.book.set(books)
            return redirect("/author_list/")
        else:
            error_msg = '出版社名字不能为空'
    ret = models.Book.objects.all()
    return render(request, "add_author.html", {'book_list': ret}, {'error': error_msg})


def del_author(request):
    del_id = request.GET.get("id", None)
    if del_id:
        models.Author.objects.get(id=del_id).delete()
        return redirect("/author_list/")
    else:
        return HttpResponse("页面不存在")


def edit_author(request):
    if request.method == 'POST':
        # 从提交的请求中获取修改项的id和修改后的出版社名
        edit_author_id = request.POST.get("author_id") #根据id找到编辑的作者
        new_author_name = request.POST.get('author_name')
        new_books = request.POST.getlist('books')
        # 根据ID值确定编辑的是哪一项，修改那一项的名字
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        edit_author_obj.name = new_author_name
        edit_author_obj.book.set(new_books) #更新作者关联书的对应关系
        edit_author_obj.save()
        # 返回出版社列表查看修改是否成功
        return redirect("/author_list/")
    # 从GET请求中的URL取得id值
    edit_id = request.GET.get("id")
    if edit_id:
        edit_author_obj = models.Author.objects.get(id=edit_id)
        books = models.Book.objects.all()
        return render(request, "edit_author.html", {'book_list': books, 'author': edit_author_obj})
    else:
        return HttpResponse("编辑的出版社不存在")






