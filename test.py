# from pagseguro.api import PagSeguroAuthorizationApp
# pagseguro = PagSeguroAuthorizationApp(
#     permissions=("CREATE_CHECKOUTS", "RECEIVE_TRANSACTION_NOTIFICATIONS"),
#     redirectURL="http://seusite.com.br/redirect",
# )
# response=pagseguro.get_authorizations()

# from pagseguro.api import PagSeguroApiTransparent
# pagseguro_api = PagSeguroApiTransparent()
#
# # pegando a session id
# data = pagseguro_api.get_session_id()
#
# # o método get_session_id retorna um dicionário que contém uma id válida que será utilizada no Browser para iniciar
# # uma sessão de chekout transparent.
# session_id = data['session_id']
#
# from pagseguro.api import PagSeguroApiTransparent, PagSeguroItem
# api = PagSeguroApiTransparent()
# item1 = PagSeguroItem(id='0001', description='Notebook Prata', amount='24300.00', quantity=1)
# api.add_item(item1)
# sender = {'name': 'Jose Comprador', 'area_code': 11, 'phone': 56273440, 'email': 'c46879763398023446825@sandbox.pagseguro.com.br', 'cpf': '22111944785',}
# api.set_sender(**sender)
# shipping = {'street': "Av. Brigadeiro Faria Lima", 'number': 1384, 'complement': '5o andar', 'district': 'Jardim Paulistano', 'postal_code': '01452002', 'city': 'Sao Paulo', 'state': 'SP', 'country': 'BRA',}
# api.set_shipping(**shipping)
# api.set_payment_method('creditcard')
# data = {'quantity': 1, 'value': '24300.00', 'name': 'Jose Comprador', 'birth_date': '27/10/1987', 'cpf': '22111944785', 'area_code': 11, 'phone': 56273440, 'no_interest_quantity': 5}
# api.set_creditcard_data(**data)
# billing_address = {'street': 'Av. Brig. Faria Lima', 'number': 1384, 'district': 'Jardim Paulistano', 'postal_code': '01452002', 'city': 'Sao Paulo', 'state': 'SP', 'country': 'BRA',}
# api.set_creditcard_billing_address(**billing_address)
# api.set_creditcard_token('e94f235ca3c643208c71ad9c29e2134d')
# api.set_sender_hash('daaab447501b4d97bc814f390657877c69dbb6b5afbd0d6938779a6eb215f63e')
# data = api.checkout()
# print(data)


"""
<script type="text/javascript" src=
    "https://stc.sandbox.pagseguro.uol.com.br/pagseguro/api/v2/checkout/pagseguro.directpayment.js">
</script>

<script type="text/javascript">
    PagSeguroDirectPayment.setSessionId('ID_DA_SESSÃO');
</script>
"""
