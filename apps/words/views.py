from django.shortcuts import render,redirect, HttpResponse
from time import gmtime, strftime

def index(request):
	try:  #need this so I will not get an error when i reset and cannot append anything to words
		request.session['words']
	except:
		request.session['words'] = []
	return render(request,'words/index.html')

def process(request):
	if request.POST.get("font") == "font": #post.get used instead of try and except.. as a way to bypass a key error.. will just print none instead of error
		fontsize = "big"
	else:
		fontsize = "regular"

	context = {
	"word": request.POST.get('word'), #if if dont post anything on word or pick a color, it will not send me to an error page with post.get
	'color': request.POST.get('color'),
	"font": fontsize,
	"time": strftime("%I:%M %p, %B %d %Y ", gmtime())
	}

	request.session["words"].append(context) #adding the dictionary of context to my words session..
	request.session.modified = True  #allows to append information
	return redirect('/')

def clear(request):
	del request.session['words']
	return redirect('/')
