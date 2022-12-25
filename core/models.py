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


class TagHeader(TimestampModel):
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE, verbose_name='Zone')
    code_nfc = models.CharField(max_length=255, verbose_name='code NFC')
    designation = models.CharField(max_length=255, verbose_name='Nom du TAG')
    order = models.PositiveIntegerField(verbose_name='Ordre', blank=True, null=True)
    observation = models.CharField(max_length=255, verbose_name='Observation')

    class Meta:
        verbose_name = 'Tag'

    def __str__(self):
        return self.designation


class TagDetail(TimestampModel):
    tag_header = models.ForeignKey(TagHeader,on_delete=models.CASCADE, verbose_name='Tag')
    memo_path = models.CharField( max_length=255, verbose_name='Lien de la memo',blank=True, null=True)
    image_path = models.ImageField(null=True, blank=True, upload_to="images/")
    description_anomaly = models.TextField(verbose_name='Anomalie', blank=True, null=True)
    is_checked = models.BooleanField(verbose_name='tag visité',default=False)

    class Meta:
        verbose_name = 'Tag détail'

    def __str__(self):
        return self.tag_header.designation