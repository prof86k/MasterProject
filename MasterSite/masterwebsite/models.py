from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# =============================== programming codes models ==============================
class ProgrammingLanguage(models.Model):
    """ programming languages whose questions are solved"""
    language_name = models.CharField("Language Name",max_length=25,null=False,blank=False)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.language_name


class Question(models.Model):
    """question to be answered """
    programming_language = models.ForeignKey(ProgrammingLanguage,on_delete=models.CASCADE)
    question_text = models.TextField(verbose_name="Question",blank=False,null=False)


    def __str__(self):
        """ to be modified to question by username"""
        return self.question_text[:50]


class ProgramSolutions(models.Model):
    """ program solution to a question asked """
    # a question can have many solution from different users
    # user model as a foreignkey
    # language name as a foreignkey
    # language_name = models.ForeignKey(ProgrammingLanguage,on_delete=models.CASCADE)
    program_question = models.ForeignKey(Question,on_delete=models.CASCADE)
    solution_code = RichTextUploadingField(blank=False,null=False,config_name='special')

    class Meta:
        verbose_name_plural = "Programm Solutions"

    def __str__(self):
        """ to be modified to question_text+user_name"""
        return "Solution To "+self.program_question.question_text

class Comment(models.Model):
    """ comments of the solution to the question """
    # program solution as a foreign key
    program_solution = models.ForeignKey(ProgramSolutions,on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text[:20]
    
# =============================================== programming code models ends here ================\