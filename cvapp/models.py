from django.db import models
import datetime

class Userinfo(models.Model): 
    first_name=models.CharField(max_length=30,null=True, blank=True, verbose_name= "İsim")
    last_name=models.CharField(max_length=30,null=True, blank=True, verbose_name= "Soyisim")
    user_name=models.CharField(max_length=30, unique=True, verbose_name="Kullanıcı Adı")
    profession=models.CharField(max_length=30, null=True, blank=True, verbose_name= "Meslek")
    maritalstat = models.BooleanField(default=False, verbose_name="Evli")
    photos=models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Profil Fotoğrafı")    
    #Üniversite listesi eklenecek
    #Sürücü ehliyeti tipi

    class Meta:
        verbose_name= "Kullanıcı Bilgileri"
    
    def full_name(self):
        return " ".join([self.first_name,self.last_name])
    
    def __str__(self): 
        return self.full_name()
    

class Contactinfo(models.Model):
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.CharField(max_length=30,null=True, blank=True, verbose_name= "Telefon numarası")
    #Şehir bilgisi ayrı yazılabilir

    class Meta:
        verbose_name = "İletişim Bilgisi"
        verbose_name_plural= "İletişim Bilgileri"
    
    def __str__(self):
        return "İletişim"


class Education(models.Model):
    admission_date = models.DateField(null=True,blank=True, verbose_name="Giriş Tarihi")  
    graduation_date = models.DateField(null=True,blank=True,verbose_name="Mezuniyet Tarihi")
    school_name = models.CharField(max_length=100,null=True, blank=True,verbose_name="Okul Adı")
    faculty_name = models.CharField(max_length=100,null=True, blank=True,verbose_name="Fakülte")
    school_department = models.CharField(max_length=100,null=True, blank=True, verbose_name="Bölüm")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Kısa Açıklama")

    class Meta:
        verbose_name = "Eğitim Bilgileri"
    
    def __str__(self):
        return "Eğitim"


class Experience(models.Model):

    company_name=models.CharField(max_length=100, verbose_name="Şirket Adı")
    position=models.CharField(max_length=100,verbose_name="Pozisyon")
    employment_type= models.CharField(max_length=100,verbose_name="İstihdam Türü")
    #İstihdam türü şeçmeli liste olarak açılmalı 
    job_admission_date= models.DateField(null=True,blank=True, verbose_name="İşe Giriş Tarihi")
    leave_date= models.DateField(null=True, blank=True, verbose_name="İşten Ayrılma Tarihi")
    short_description= models.TextField(max_length=500,null=True, blank=True,verbose_name="Kısa Açıklama")

    class Meta:
        verbose_name = "Tecrübe"
        verbose_name_plural = "Tecrübeler"
    
    def __str__(self):
        return "Tecrübe"


class Project(models.Model):

    project_name = models.CharField(max_length=255,verbose_name="Proje Adı")
    start_date = models.DateField(null=True, blank=True,verbose_name="Proje Başlangıç Tarihi")
    end_date = models.DateField(null=True, blank=True, verbose_name="Proje Bitiş Tarihi")
    project_url = models.URLField(null=True, blank=True, verbose_name="Proje Linki")
    related_institution=models.CharField(max_length=255, null=True, blank=True, verbose_name="İlgili Kuruluş Adı")
    description=models.TextField(null=True, blank=True, verbose_name="Proje Bilgileri")
    #Buraya hala devam ediyor check box yerleştirilebilir booleanField ile
    
    class Meta:
        verbose_name = "Projeler"
    
    def __str__(self):
        return "Projeler"


class Activity(models.Model):

    organization_name = models.CharField(max_length=200,null=True, blank=True,verbose_name="Organizasyon Adı")
    role=models.CharField(max_length=100,null =True, blank=True,verbose_name="Organizasyondaki Pozisyonu")
    related_institution=models.CharField(max_length=255, null=True, blank=True, verbose_name="İlgili Kuruluş Adı")
    start_date = models.DateField(null=True, blank=True,verbose_name="Başlangıç Tarihi")
    end_date = models.DateField(null=True, blank=True, verbose_name="Bitiş Tarihi")
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    #Hala devam ediyor check box 

    class Meta:
        verbose_name = "Sosyal Aktiviteler"
    
    def __str__(self):
        return "Sosyal Aktiviteler"


class Certificate(models.Model):

    certificate_name = models.CharField(max_length=200,null =True, blank=True,verbose_name="Sertifika ya da Lisans Adı")
    related_institution = models.CharField(max_length=255, null=True, blank=True, verbose_name="İlgili Kuruluş Adı")
    certificate_stat = models.BooleanField(default=False, verbose_name="Bu sertifikanın geçerliliği sona ermez")
    start_date = models.DateField(null=True, blank=True, verbose_name="Alınma Tarihi")
    end_date = models.DateField(null=True, blank=True, verbose_name="Sona Erme Tarihi")
    certificate_url = models.URLField(null=True, blank=True, verbose_name="Sertifika Linki")
    certificate_id = models.CharField(max_length=255,null=True, blank=True,verbose_name="Sertifika Kimliği")
    Description = models.TextField(null=True, verbose_name="Kısa Açıklama")

    class Meta:
        verbose_name = "Sertifika Bilgileri"
    
    def __str__(self):
        return "Sertifika Bilgileri"


class Skills(models.Model):
    skill_name = models.CharField(max_length=100,null =True, blank=True,verbose_name="Yetkinlik Adı")
    knowledge=models.CharField(max_length=50,null =True, blank=True,verbose_name="Yetkinlik Düzeyi")
    
    class Meta:
        verbose_name = "Yetkinlikler"
    
    def __str__(self):
        return "Yetkinlikler"

class Computer_Skills(Skills):
    com_program= models.CharField(max_length=50,null =True, blank=True,verbose_name="Program Adı")

    def __str__(self):
        return "Bilgisayar Becerileri"

class Language_Skills(Skills):
    language = models.CharField(max_length=50,null =True, blank=True,verbose_name="Yabancı Dil")
    reading_level=models.CharField(max_length=30,null =True, blank=True,verbose_name="Okuma Yetkinliği")
    writing_level=models.CharField(max_length=30,null =True, blank=True,verbose_name="Yazma Yetkinliği")
    speaking_level=models.CharField(max_length=30,null =True, blank=True,verbose_name="Konuşma Yetkinliği")
    #başlangıç orta ileri ve profesyonel seviye olmak üzere 4 seçenek yazılmalı 
    def __str__(self):
        return "Yabancı Dil Becerileri"

class Interests(models.Model):
    interest_list = models.TextField(max_length=500,null=True, blank=True, verbose_name="İlgi Alanları")
    
    class Meta:
        verbose_name = "İlgi Alanları"
    
    def __str__(self):
        return "İlgi Alanları"
class Deneme(models.Model):
    interest_list = models.TextField(max_length=500,null=True, blank=True, verbose_name="İlgi Alanları")
