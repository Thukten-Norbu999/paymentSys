from django.db import models

# Create your models here.
from django.db import models
from useraccount.models import Account
from django.core.mail import send_mail, send_mass_mail
# Create your models here.
import uuid, random, string

def gen_journalNumber() -> str:
    al = [(random.choice(string.ascii_uppercase)) for i in range(3)]
    no = [random.choice(string.digits) for i in range(8)]
    return "".join(al)+"".join(no)




class Transactions(models.Model):
    #account = models.ForeignKey(Account)
    id = models.UUIDField(default=uuid.uuid4, verbose_name="ID", editable=False, primary_key=True)
    amount = models.FloatField(verbose_name="Amount")
    
    frm = models.CharField(max_length=9, verbose_name="From account")
    to = models.CharField(max_length=9, verbose_name="To account", )
    remarks = models.CharField(max_length=250, verbose_name="Remarks")

    date = models.DateTimeField(auto_now_add=True, verbose_name="Date-Time of Transaction")

    journalNo = models.CharField(unique=True, default=gen_journalNumber, verbose_name='Journal Number', max_length=12)

    class Meta:
        ordering = ['-date']
        constraints = [
            models.UniqueConstraint(fields=['id', 'journalNo'], name='unique_transaction')
        ]


    


    def mail(self, success:bool):
        subject = ''
        if success:
            subject='successful transaction '
        else:
            subject='Transactions failed'
        #TODO create the transaction msg with f'***{lastACCno}'
        
        


    def __str__(self):
        return self.journalNo
    


