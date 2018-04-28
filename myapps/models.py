from django.db import models

# Create your models here.

class Topic(models.Model):
	"""故障工单内容、申告时间、完成时间、申告人、完成人、状态（是否完成）"""
	text =  models.TextField()
	date_start = models.DateTimeField(auto_now_add=True)
	date_end = models.DateTimeField(null=True,blank=True)
	people_start = models.CharField(max_length=50)
	people_end = models.CharField(max_length=50,null=True,blank=True)
	state = models.CharField(max_length=10)

	def __str__(self):
		"""返回模型的字符串表示，前50个字符"""
		return self.text[:50]+"..."


class Distribute(models.Model):
	"""故障工单转派/反馈内容、时间、人"""
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	dis_type = models.CharField(max_length=10) #转派还是反馈
	distribute_time = models.DateTimeField(auto_now_add=True)
	distribute_people = models.CharField(max_length=50)

	def __str__(self):
		return self.text[:50]+"..."
