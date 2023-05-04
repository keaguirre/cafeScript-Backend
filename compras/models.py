from django.db import models
from django.utils import timezone
from productos.models import preparacion
from local.models import Totem

#comando salvador: python manage.py migrate --run-syncdb
# Modelos de bloque Compras
# bloque productos = Compra, Item compra

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Compra')
    tipo_servicio_compra = models.CharField(max_length=32,null=False, blank=False, default='Para servir', verbose_name='Para servir o llevar')
    fecha_compra = models.DateTimeField(auto_now_add=True)
    estado_compra = models.CharField(max_length=32,null=False, blank=False, default='esperando', verbose_name='Estado compra')
    total_compra = models.IntegerField(verbose_name='Total de la compra', default=0)
    #nboleta_compra = models.AutoField(verbose_name='N boleta servicios de pago', default=0)
    procesador_pago_compra = models.CharField(max_length=15,null=False, blank=False, default='transbank', verbose_name='Tipo de pago')
    #campos medios de pago-------
    id_transaccion_compra = models.CharField(max_length=30, null=True, blank=False, default='0', verbose_name='ID Transaccion')
    cod_comercio_compra = models.CharField(max_length=15,null=True, blank=False, default='0', verbose_name='Cod comercio')
    respuesta_tb_compra = models.CharField(max_length=15,null=True, blank=False, default='0', verbose_name='Cod comercio')
    respuesta_mp_compra = models.CharField(max_length=15,null=True, blank=False, default='0', verbose_name='Cod comercio')
    totem_compra = models.ForeignKey(Totem, on_delete=models.CASCADE, default='null', related_name='id_totem_compra')

    class Meta:
        verbose_name='Compra'
        verbose_name_plural='Compras'

    def __int__(self):
        return self.id_compra

class Item_compra(models.Model):
    id_prep = models.ForeignKey(preparacion, on_delete=models.CASCADE, default='null', related_name='id_prep_itemcompra')
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, default='null', related_name='id_compra_itemcompra')
    cantidad_item = models.IntegerField(verbose_name='Cantidad del item', default=999)
    precio_unitario_item = models.IntegerField(verbose_name='Precio unitario item', default=999)
    total_item = models.IntegerField(verbose_name='Precio unitario item', default=0)

    class Meta:
        verbose_name='Item_compra'
        verbose_name_plural='Items_compra'
        ordering=['id_prep']

    def __int__(self):
        return self.id_prep