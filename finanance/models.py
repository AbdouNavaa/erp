from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "User: "+self.username
    
    
class Client(models.Model):
    Name = models.CharField(max_length=40,null=False)
    # LastName = models.CharField(max_length=40)
    # profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40,)
    mobile = models.CharField(max_length=20,null=False)
    Type =models.ForeignKey("Type",on_delete=models.CASCADE)
   
    def __str__(self):
        return self.Name
    
class Type(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Fournisseur(models.Model):
    Name = models.CharField(max_length=40)
    # LastName = models.CharField(max_length=40)
    # profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    Type =models.ForeignKey(Type,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name

class FactureCl(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    journal = models.CharField(max_length = 100)
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    date_facturation = models.DateField()
    Taxe = models.FloatField()
    quantity = models.FloatField()
    
    @property
    def code(self):
        return "INV/"+str(self.date_facturation.year)+"/"+str(self.id)
    
    def __str__(self):
        return self.code
    @property
    def total(self):
        Total = ((self.quantity*self.produit.prix) * self.Taxe) + (self.quantity*self.produit.prix)
        return Total
    
    @property
    def HTaxe(self):
        hTaxe =self.quantity*self.produit.prix
        return hTaxe
    @property
    def TVA(self):
        tva =(self.quantity*self.produit.prix) * self.Taxe
        return tva
    
class FactureFr(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    journal = models.CharField(max_length = 100)
    date_facturation = models.DateField()
    Taxe = models.FloatField()
    quantity = models.FloatField()
    
    @property
    def code(self):
        return "BILL/"+str(self.date_facturation.year)+"/"+str(self.id)
    def __str__(self):
        return self.code
    @property
    def total(self):
        Total = -((self.quantity*self.produit.prix) * self.Taxe) - (self.quantity*self.produit.prix)
        return Total
    @property
    def total1(self):
        Total1 = 0
        Total = -((self.quantity*self.produit.prix) * self.Taxe) - (self.quantity*self.produit.prix)
        Total1 = Total1 - Total
        return Total1
    @property
    def HTaxe(self):
        HTaxe =self.quantity*self.produit.prix
        return HTaxe
    @property
    def TVA(self):
        tva =(self.quantity*self.produit.prix) * self.Taxe
        return tva
    
class Produit(models.Model):
    libelle = models.CharField(max_length = 100)
    prix = models.FloatField()
    

    def __str__(self):
        return self.libelle

class Journal(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name   
class JournalPaiement(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
class PieceCompt(models.Model):
    ref = models.FloatField()
    date_comptable = models.DateField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    partenaire = models.ForeignKey(Client, on_delete=models.CASCADE)
    deb = models.FloatField()
    cred = models.FloatField()
    @property
    def total(self):
        Total = self.deb-self.cred
        return Total
    def __str__(self):
        return self.journal.name
    
    
class Paiements(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Date = models.DateField()
    montant = models.FloatField()
    journal = models.ForeignKey(JournalPaiement, on_delete=models.CASCADE)
    Mode = models.CharField(max_length=100)
    Type_CHOICES = [
        ('E', 'Envoyer'),
        ('R', 'Recevoire'),
    ]
    Type = models.CharField(max_length=1, choices=Type_CHOICES)
    
    @property
    def Montant(self):
        Montant =0
        if self.Type in self.Type_CHOICES[0]:
            Montant -=self.montant
        else:
            Montant =self.montant
        return Montant
    
    @property
    def code(self):
        return "P"+str(self.journal)+str(self.Date.year)+"/"+str(self.id)
    def __str__(self):
        return self.code
    #  = models.BooleanField(choices=)
    # comptBank = models.FloatField()
    # @property
    # def total(self):
    #     Total = self.deb-self.cred
    #     return Total
    
    