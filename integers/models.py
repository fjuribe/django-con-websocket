from django.db import models

# Create your models here.


# class Hobby(models.Model):
#     """ pasa tiempos """
#     hobby = models.CharField('Pasa tiempo',max_length = 150)
#     class Meta:
#         verbose_name='Hobby'
#         verbose_name_plural='hobbies'

#     def __str__(self):
#         return self.hobby


class Person(models.Model):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    # hobbies=models.ManyToManyField(Hobby)

    # class Meta:
    #     verbose_name = 'Persona'
    #     verbose_name_plural = 'Personas'
    
    # def __str__(self):
    #     return self.full_name


class Reunion(models.Model):
    """ modelo para reunion """
    persona = models.ForeignKey(Person, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField('Aunto de reunion',max_length = 100)

    class Meta:
        verbose_name='Reunion'
        verbose_name_plural='Reunion'
    
    def __str__(self):
        return self.asunto
    