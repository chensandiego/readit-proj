from django.shortcuts import render
from django.views.generic import DetailView,View
from .models import Book,Author
from django.db.models import Count

# Create your views here.
def list_books(request):
	"""
	list the books that have reviews
	"""

	books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')
	context = {
		'books':books,
	}


	return render(request,"list.html",context)



class AuthorList(View):
	def get(self,request):
		authors = Author.objects.annotate(published_books=Count('books')
			).filter(
				published_books__gt=0
			)

		context={
			'authors':authors,
		}
		return render(request,'authors.html',context)


class BookDetail(DetailView):
	model =Book
	template_name = 'book.html'


class AuthorDetail(DetailView):
	model = Author
	template_name = 'author.html'