from django.db import models
from localflavor.br.models import BRCPFField
from model_utils.models import TimeStampedModel


class Payment(TimeStampedModel):
    order = models.ForeignKey('main_app.Order', related_name="payments", on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(
        "Valor de transacción", max_digits=7, decimal_places=2
    )
    installments = models.IntegerField("Pago a meses")
    payment_method_id = models.CharField("Método de Pago", max_length=250, blank=True, null=True)
    card_holder = models.CharField("Titular de la tarjeta", max_length=250)
    email = models.EmailField()
    mercado_pago_id = models.CharField(max_length=250, blank=True, db_index=True)
    mercado_pago_status = models.CharField(max_length=250, blank=True)
    mercado_pago_status_detail = models.CharField(max_length=250, blank=True)

    # def save(self, *args, **kwargs):
    #     self.transaction_amount = round(self.transaction_amount, 2)
    #     super(Payment, self).save(*args, **kwargs)

    class Meta:
        ordering = ("-modified",)
        verbose_name="Pago"

    def __str__(self):
        return f"{self.mercado_pago_status} - M.Pago ID: {self.mercado_pago_id}"