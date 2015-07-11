from django.shortcuts import render
from votes.models import Vote, Answer, User
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse

# Create your views here.
def votes_view(request):
	context = {}
	votes = Vote.objects.all()
	for v in votes:
		total = 0
		for a in v.answer_set.all():
			total += a.votes_count
		v.total_votes = total
		if (v.user_set.filter(host=request.get_host())):
			v.is_loked=True
		else:
			v.is_loked=False
			
	context['votes'] = votes
	context['ip'] = request.get_host()

	return render(request,"votes.html", context)

def vote_view(request, vote_id):
	try:
		vote = Vote.objects.get(id=vote_id)
	except Exception as e:
		raise Http404

	return render(request,"vote.html",{"vote" : vote})

def vote_vote(request, answer_id):
	try:
		a = Answer.objects.get(id=answer_id)
		a.votes_count += 1
		a.save()
		user = User(host=request.get_host(),vote=a.vote)
		user.save()
	except Exception as err:
		raise Http404

	#return HttpResponseRedirect(reverse('vote', args=[a.vote.id]))
	return HttpResponseRedirect(reverse('votes'))