from models import cliente
from services import cliente_service
from repositories import cliente_repository
import json


service = cliente_service.ClienteService()

service.editar(cpf="12345678909", campo="email", novo_valor="papaicris@gmail.com.pt")

service.listar()