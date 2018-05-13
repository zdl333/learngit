from django import forms

from .models import Topic,Distribute

class TopicForm(forms.ModelForm):
	"""新增工单表单"""
	class Meta:
		model = Topic
		fields = ['text','people_start']
		labels = {'text':'内容','people_start':'申告人'}


class ForwardForm(forms.ModelForm):
	"""转派表单"""
	class Meta:
		model = Distribute
		fields = ['text','dis_type','distribute_people']
		labels = {'text':'备注','dis_type':'类型','distribute_people':'转派人'}


class ForwardForm1(forms.ModelForm):
	"""反馈表单"""
	class Meta:
		model = Distribute
		fields = ['text','distribute_people']
		labels = {'text':'备注','distribute_people':'反馈人'}