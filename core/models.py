from django.db import models


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Créé')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modifié')

    class Meta:
        abstract = True


class Enterprise(TimestampModel):
    designation = models.CharField(max_length=255, verbose_name='Nom de l\'entreprise')

    class Meta:
        verbose_name = 'Entreprise'

    def __str__(self):
        return self.designation


class Site(TimestampModel):
    designation = models.CharField(max_length=255, verbose_name='Nom du site')
    enterprise = models.ForeignKey(Enterprise,on_delete=models.CASCADE)


    def __str__(self):
        return self.designation + f" ({self.enterprise.designation})"


class Zone(TimestampModel):
    designation = models.CharField(max_length=255, verbose_name='Nom de la zone')
    site = models.ForeignKey(Site,on_delete=models.CASCADE, verbose_name='Site')

    def __str__(self):
        return self.designation + f" ({self.site.designation} - {self.site.enterprise.designation})"



class Employee(TimestampModel):
    designation = models.CharField(max_length=255, verbose_name='Nom de l\'employée')
    site = models.ForeignKey(Site,on_delete=models.CASCADE)
   
    class Meta:
        verbose_name = 'Employée'

    def __str__(self):
        return self.designation


class Tag(TimestampModel):
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE, verbose_name='Zone')
    code_nfc = models.CharField(max_length=255, verbose_name='code NFC')
    designation = models.CharField(max_length=255, verbose_name='Nom du TAG')
    order = models.PositiveIntegerField(verbose_name='Ordre', blank=True, null=True)
    observation = models.CharField(max_length=255, verbose_name='Observation')

    class Meta:
        verbose_name = 'Tag'

    def __str__(self):
        return self.designation


class PatrolLog(TimestampModel):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE, verbose_name='Tag')
    audio_path = models.CharField( max_length=255, verbose_name='Lien de la memo-vocale',blank=True, null=True)
    image_path = models.ImageField(null=True, blank=True, upload_to="images/")
    description_anomaly = models.TextField(verbose_name='Anomalie', blank=True, null=True)
    is_checked = models.BooleanField(verbose_name='tag visité',default=False)

    class Meta:
        verbose_name = 'Journal des tournées'

    def __str__(self):
        return self.tag.designation


class Planning(TimestampModel):
    name_day=(
        ('1','Samedi'),
        ('2','Dimanche'),
        ('3','Lundi'),
        ('4','Mardi'),
        ('5','Mercredi'),
        ('6','Jeudi'),
        ('7','Vendredi'),
        ('8','Jour férié'),
    )
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE, verbose_name='Zone')
    selected_day_index = models.CharField(max_length=10,null=True,blank=True,choices=name_day)
    patrol_start_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Heure de début de la tournée')
    tolerated_time = models.DurationField(verbose_name='Temps toléré')
    observation = models.TextField(verbose_name='Observation', blank=True, null=True)
    
    def __str__(self):
        return  f"(planning de la zone : {self.zone}"