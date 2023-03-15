from django import forms

from main_app.models import UserProfile
from localflavor.mx.forms import MXZipCodeField
from django.utils.safestring import mark_safe
# from django.core.validators import RegexValidator

PAYMENT_OPTIONS = (
    ('C', mark_safe("<i class='fas fa-credit-card'></i> Carjeta de Crédito")),
    ('B', mark_safe("- Não Implementado abaixo -<br><i class='fas fa-barcode'></i> Efectivo")),
    ('P', mark_safe("<i class='fa-brands fa-pix'></i> Otros")),
    # ('C', mark_safe("<img src=/static/img/teste.jpg> Cartão de Crédito")), # Another option is to use an image instead of an icon
    # ('C', mark_safe('<img src="https://images.kabum.com.br/produtos/fotos/112990/processador-intel-core-i5-10400-cache-12mb-2-9ghz-lga-1200-bx8070110400_1589200167_p.jpg"/> Cartão de Crédito')),
)
# PAYMENT_OPTIONS = (
#     ('C', 'Cartão de Crédito'),
# )


# alphanumeric = RegexValidator(r'^[0-9\w ]*$', 'Somente alfanúmericos são permitidos.')
# #https://stackoverflow.com/questions/11757013/regular-expressions-for-city-name
# cities = RegexValidator(r'^([a-zA-Z\u0080-\u024F]+(?:. |-| |\'))*[a-zA-Z\u0080-\u024F]*$', 'Somente letras são permitidas.')


class NewAddressForm(forms.Form):
    zipcode = MXZipCodeField(label='Código Postal', widget=forms.TextInput(attrs={'id': 'id_postal_code', 'data-mask': '00000', 'placeholder': 'Formato: XXXXX', 'onkeyup': 'getAddress()'}))
    address = forms.CharField(label='Dirección', max_length=250, widget=forms.TextInput(attrs={'id': 'id_address'}))
    number = forms.IntegerField(label='Número (00 ppara indicar sin numero)', widget=forms.TextInput(attrs={'data-mask': '00000'}))
    district = forms.CharField(label="Colonia", max_length=250, widget=forms.TextInput(attrs={'id': 'id_district'}))
    # state = BRStateChoiceField(label='Estado', widget=forms.Select(attrs={'id': 'id_state'}))
    city = forms.CharField(label="Cuidad", max_length=250, widget=forms.TextInput(attrs={'id': 'id_city'}))
    state = forms.CharField(label='Estado', max_length=250, widget=forms.TextInput(attrs={'id': 'id_state'}))
    complement = forms.CharField(required=False, label="Complemento", max_length=250, widget=forms.TextInput(attrs={'id': 'id_complement', 'placeholder': 'Exemplo: Ao lado da loja...'}))
    default = forms.BooleanField(required=False, label='Hacer dirección preferida', initial=True)


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        widgets = {'cell_number': forms.TextInput(attrs={'data-mask':"(00) 000000000", 'placeholder': '(XX)-XXXXXXXXX'}),
                   }
    email = forms.EmailField()


class PaymentOptionForm(forms.Form):
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style': 'position: relative;'}), # position just to center radio button
                                        choices=PAYMENT_OPTIONS,
                                        label='Opciones de pago')


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Cupon',
        'class': 'form-control',
        'aria-label': "Recipient's username",
        'aria-describedby': "basic-addon2"}))


class RefundForm(forms.Form):
    ref_code = forms.CharField(label="Código de Pedido")
    reason = forms.CharField(label="Razón de Devolución", widget=forms.Textarea(attrs={'rows': 4}))
    email = forms.EmailField()
        