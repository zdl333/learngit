from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text','people_start']
		labels = {'text':'内容','people_start':'申告人'}