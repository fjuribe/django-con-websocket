from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save,post_delete,post_init,pre_save,m2m_changed,pre_init,post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
# Create your models here.
import channels
import json
# from model_utils import FieldTracker

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

    full_name = models.CharField('Nombres',max_length=50)
    job = models.CharField('Trabajo',max_length=30,blank=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField('telefono',max_length=15,blank=True)


###revisado###
@receiver(post_delete,sender=Person)
def detalle_fac_guardar2(sender,instance,**kwargs):
    print("Hubo una eliminar")
    message = {
            'full_name': instance.full_name,
            "job":instance.job,
            "email":instance.email,
            "phone":instance.phone
    }
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "group_name", {"type": "send_message", "data": message}
    )


@receiver(post_save,sender=Person)
def detalle_fac_guardar(sender,instance,created,**kwargs):
    print("-->",instance.full_name)
    print("-->",created)

    print("Se creo uno nuevo")
    message = {
            'full_name': instance.full_name,
            "job":instance.job,
            "email":instance.email,
            "phone":instance.phone
    }
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "group_name", {"type": "send_message", "data": message}
    )

########################################
# @receiver(post_init,sender=Person)
# def detalle_fac_guardar(sender,instance,**kwargs):
#     print("--->",sender.__dict__)
#     print("-->",instance.full_name)


#     print("Hubo una actualizar")
#     message = {
#             'full_name': instance.full_name,
#             "job":instance.job,
#             "email":instance.email,
#             "phone":instance.phone
#     }
#     channel_layer = channels.layers.get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         "group_name", {"type": "send_message", "data": message}
#     )

############################################
# @receiver(,sender=Person)
# def detalle_fac_guardar(sender,instance,**kwargs):

#     print(instance.id)
    # person=Person.objects.all().order_by('-id').first()
    # print(person.full_name)
    # print("Hubo un cambio")
    # message = {
	# 		'full_name': person.full_name,
    #         "job":person.job,
    #         "email":person.email,
    #         "phone":person.phone
    # }
    # channel_layer = channels.layers.get_channel_layer()
    # async_to_sync(channel_layer.group_send)(
    #     "group_name", {"type": "send_message", "data": message}
    # )


# @receiver(m2m_changed,sender=Person)
# def detalle_fac_guardar(sender,instance,action,**kwargs):
#     print(action)
#     person=Person.objects.all().order_by('-id').first()
#     print(person.full_name)
#     print("Hubo un cambio")
#     message = {
#             'full_name': person.full_name,
#             "job":person.job,
#             "email":person.email,
#             "phone":person.phone
#     }
#     channel_layer = channels.layers.get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         "group_name", {"type": "send_message", "data": message}
#     )



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
    


# @receiver(post_save,sender=Person)
# def detalle_fac_guardar(sender,instance,**kwargs):
    #print("Hubo un cambio")


@receiver([post_save, post_delete], sender=Person)
def emitiendo(sender, instance, **kwargs):
    layer = channels.layers.get_channel_layer()
    print("Hubo un cambio")
    async_to_sync(layer.send)("timer_observers",{
            'type': 'send_message',
            'text': "holaa"
    })
    # message = {
    # 	'status': "se ejecuto",

    # }

#     async_to_sync(get_channel_layer().send)( 'timer_observers',
#             {"type": "timer.changed"}
#         )