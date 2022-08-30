# ProyectoCoderHouse
Proyecto de fin de curso

## Descripcion

Esta es una web de una ferreteria que tiene login, registro, edicion de perfil con imagen, cambiar contraseña, con un carrito de compra, donde se pueden agregar productos.

## Getting Started

### Instalando el proyecto

Pasos: 

* git clone https://github.com/fvck12/ProyectoCoderHouse.git

* Pre-Requisitos para ejecutar la web.

* pip install Django
* pip install Pillow
* pip install django-cripsy-forms
* pip install django-import-export
* echo "from Accounts.models import User; User.objects.create_superuser('hwstoreadmin', 'hwstoreadmin@gmail.com', 'Homero123')" | python manage.py shell

### Ejecutar el servidor

* python manage.py runserver

### Uso de la web

* admin/ administracion
* ""/ 'Pagina inicial'
* HWStockApp/CrearProducto/ 'Formulario de alta de producto'
* HWStockApp/ListarProductos/ 'Formulario de lista de productos en formato tabla'
* HWStoreApp/ComprarProductos/ 'Lista paginada de los productos con carro de compras'
* HRApp/CrearEmpleados/ 'Formulario de alta de empleado'
* HRApp/ListaEmpleados/ 'Formulario de lista de empleado en formato tabla'

* HRApp/CrearClientes/ 'Formulario de alta de cliente'
* HRApp/ListaClientes/ 'Formulario de lista de cliente en formato tabla'

## Developers

Nicolas Sandoval
[@DrSandwell](https://github.com/DrSandwell)

Omar Rivera
[@omaration22](https://github.com/omaration22)

Nicolas Martinez
[@fvck12](https://github.com/fvck12)

## Version History

* 0.1
    * Version Inicial
* 52
    * Version final
