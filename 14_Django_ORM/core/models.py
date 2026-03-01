from django.db import models

# Create your models here.
class Profile(models.Model):
    #1. Create a database table in the database that you are using for your Django project.
    name =models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    # 2. Create a skills field that is a list of strings.
    skills = models.TextField()

    # 3. Funtion to return a string representation of the object.
   

    def get_skills_list(self):
        
        if self.skills:
            return [skill.strip() for skill in self.skills.split(',')]
        else:
            return []

    def __str__(self):
        return self.name        