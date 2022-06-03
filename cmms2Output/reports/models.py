from django.db import models

class Student(models.Model):
	std_id = models.BigAutoField(primary_key=True)
	std_email = models.CharField(max_length=50,null=True,unique=True) 

	def __str__(self):
		return str(self.std_email)

class Block(models.Model):
	bl_id = models.BigAutoField(primary_key=True)
	bl_name = models.CharField(max_length=2,null=True,unique=True) 

	def __str__(self):
		return self.bl_name

class Lab(models.Model):
	l_id = models.BigAutoField(primary_key=True)
	l_no = models.IntegerField(null=True,unique=False)
	block_n=models.ForeignKey(Block,on_delete=models.CASCADE) 

	def __str__(self):
		return str(self.l_no)

class Computer(models.Model):
	c_id = models.BigAutoField(primary_key=True)
	comp_no = models.IntegerField(null=True,unique=False)
	c_status = models.IntegerField(null=True,unique=False)

	lab_n=models.ForeignKey(Lab,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.c_id) 

class Report(models.Model):
	r_id = models.BigAutoField(primary_key=True)

	comp_id=models.ForeignKey(Computer,on_delete=models.CASCADE)

	r_mouse = models.IntegerField(null=True,unique=False)
	r_keyboard = models.IntegerField(null=True,unique=False)
	r_monitor = models.IntegerField(null=True,unique=False)
	r_OS = models.IntegerField(null=True,unique=False)
	r_internet = models.IntegerField(null=True,unique=False)
	r_other = models.CharField(max_length=200,null=True,unique=True) 
	date_created = models.DateTimeField(auto_now_add=True,null=True) 

	std_mail=models.ForeignKey(Student,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.r_id) 




