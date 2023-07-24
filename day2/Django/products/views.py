# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from .models import Author, Book


# class BookListView(ListView):
#     model = Book
#     template_name = "book_list.html"


# class BookDetailView(DetailView):
#     model = Book
#     template_name = "book_detail.html"

from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import Book, Author


def book_list(request):
    try:
        books = Book.objects.all()  # Book object를 다 가져온다.
        # data = {"books": list(books.values())}  # ORM
        # response = JsonResponse(data, safe=False, json_dumps_params={
        #                         'ensure_ascii': False})
        data = list(books.values())
        print('데이터', data)
        book_list = ''
        for i in data:
            book_list += f'<li><a href="/api/books/{i["id"]}">{i["name"]} ({i["price"]}원)</a></li>'
        print("북리스트", book_list)
        return HttpResponse(f'''
        <html>
        <body>
          <h2>책 목록</h2>
          <ol>
            {book_list}
          </ol>
        </body>
        </html>
        ''')
    except:
        return JsonResponse({'message': "ERROR OCCURED"})


def book_detail(requests, pk):
    try:
        book = Book.objects.get(pk=pk)
        data = {
            "book": {
                "author": book.author.name,
                "name": book.name,
                "description": book.description,
                "shipping_cost": book.shipping_cost,
                "quantity": book.quantity
            }}
        # response = JsonResponse(data, safe=False, json_dumps_params={
        #                         'ensure_ascii': False})
        # return response
        return HttpResponse(f'''
        <html>
        <body>
          <h2>{data['book']['name']}</h2>
          <ul>
            <li>작가: {data['book']['author']}</li>
            <li>내용: {data['book']['description']}</li>
            <li>배송비: {data['book']['shipping_cost']}</li>
            <li>남은 수량: {data['book']['quantity']}</li>
          </ul>
          <h5><a href="/api/books">책목록보기</a></h5>
        </body>
        </html>
        ''')
    except:
        return JsonResponse({'message': "ERROR OCCURED"})
