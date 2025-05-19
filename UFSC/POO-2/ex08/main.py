from controladorPessoas import ControladorPessoas

controlador = ControladorPessoas()
controlador.inclui_cliente(1234, "Lucas")
print(controlador.clientes)
controlador.inclui_cliente(1234, "Lucas")