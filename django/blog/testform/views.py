from django.shortcuts import render
from testform.forms import MessageForm
from django.conf import settings

# Create your views here.
def form_view(request):
	context = {}
	if request.method == "POST":
		context["postreport"] = repr(request.POST)
		context["uploadfile"] = repr(request.FILES)
		form = MessageForm(request.POST, request.FILES)
		if form.is_valid():
			context["message"] = [form.cleaned_data]
			'''
			or
			author = form.cleaned_data["author"]
			msg = form.cleaned_data["message"]
			context["messages"] = []
			context["messages"].append({
				"author": author,
				"message": msg,
				"is_public": form.cleaned_data["is_public"],
				})

			'''
			#UploadedFile
			tempFile = request.FILES["image"]
			outFile = open(settings.BASE_DIR + "/static/upload/" + tempFile.name,"wb")
			
			for chunk in tempFile.chunks():
				outFile.write(chunk)
			outFile.close()
			form = MessageForm()
	else:
		form = MessageForm()

	context["form"] = form
	return render(request,"forms.html",context)