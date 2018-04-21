from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from myapps.models import Topic
from myapps.forms import TopicForm

# Create your views here.

def view(request):
	"""显示工单的视频页"""
	limit = 5	#每页显示的记录数
	topics = Topic.objects.order_by('-date_start')	#按时间顺序取记录
	paginator = Paginator(topics,limit)	#实例化一个分页对象
	page =  request.GET.get('page')	#获取页码

	try:
		topics = paginator.page(page)	#获取页码对应的记录
	except PageNotAnInteger:	#如果页码不是整数
		topics = paginator.page(1)	#取第一页记录
	except EmptyPage:	#如果页码太大，没有相应的记录
		topics = paginator.page(paginator.num_pages)	#取最后一页的记录

	return render(request,'myapps/view.html',{'topics':topics})



def information(request,topic_id):
	"""显示单个工单及其详细转派内容"""
	topic = Topic.objects.get(id=topic_id)
	distributes = topic.distribute_set.order_by('-distribute_time')
	context = {'topic':topic,'distributes':distributes}
	return render(request,'myapps/information.html',context)


def new_topic(request):
	"""添加新工单"""
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myapps:view'))

	context = {'form':form}
	return render(request,'myapps/new_topic.html',context)


def edit_topic(request,topic_id):
	"""修改工单"""
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		form = TopicForm(instance=topic)
	else:
		form = TopicForm(instance=topic,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myapps:view'))

	context = {'topic':topic,'form':form}
	return render(request,'myapps/edit_topic.html',context)