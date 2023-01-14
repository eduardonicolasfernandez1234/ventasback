# VentasBack

Proyecto en Django

### Instalación y Ejecución

------

Una vez descargado/clonado el repositorio crearse un entorno virtual en la carpeta raíz del proyecto

```
$ python -m venv venv
```

**Iniciar el entorno virtual**

```
$ venv\Scripts\Activate
```

**Instalar dependencias**

```
$ pip install -r requirements.txt
```

**Ejecutar las migraciones**

```
$ pip install makemigrations
$ pip install migrate
```

**Crear un usuario administrador de Django**

```
$ python manage.py createsuperuser
```

**Ejecutar el proyecto**

```
$ python manage.py runserver
```

Ingresar al siguiente enlace para poder acceder a la interfaz de administración de Django, en la cual podrá realizar el CRUD de las aplicaciones. 

![image](https://user-images.githubusercontent.com/30891977/212450732-6054702a-aa50-4bff-bca4-cabbb7eb0969.png)

**Importar las colecciones de datos para realizar consultas por POSTMAN**

La colección de datos se encuentra en la carpeta raíz del proyecto, una vez clonado el entorno podrá importarlo.

**Nombre del fichero:** 

> Ventas Back.postman_collection.json

Una vez importada la colección **Ventas Back** podrá ver la documentación de la API clicando en la opción "View documentation" a través del botón  "view more options"

![image](https://user-images.githubusercontent.com/30891977/212450756-dad52601-7150-40cf-a8da-4a8865d4df91.png)

Todas las peticiones que se realicen de las carpetas **Ventas Back** cuentan con un script de autenticación, de tal modo que no sea necesario hacer login y cambiar el token de autorización.

En caso de querer actualizar el script actualizar los campos **username** y **password** en la sección Pre-request Script de la carpeta de la colección.

![image](https://user-images.githubusercontent.com/30891977/212450781-138a25d4-ceac-46c6-94a7-489b1db4f623.png)



### Inicio

1. **Criterios del proyecto**
   1. **Requisitos del proyecto**
   2. **Diagrama ER**
   3. **Colección de Datos API**
2. **Módulos del proyecto**
   1. **Módulo "Storage"**
      1. **Entidad "category"**
      2. **Entidad "provider"**
      3. **Entidad "product"**
      4. **Entidad "inventory"**
   2. **Módulo "Sales"**
      1. **Entidad "tax"**
      2. **Entidad "config_sales"**
      3. **Entidad "order"**
      4. **Entidad "sales"**
   3. **Módulo "Authentication"**
      1. **Entidad "User"**
3. **Seguridad del proyecto**
4. **Documentación**



### 1. Criterios del proyecto

#### 1.1 Requisitos del proyecto

Construir un servicio API REST para la gestión de productos de un almacén: 

* **Se deja a su criterio los atributos de este.** 

> Entidades y atributos del proyecto adjunto en el diagrama ER Ventas Back

* **Para la persistencia de datos está permitido el uso de una estructura de datos o una base de datos en cualquier motor.** 

> Motor base de datos SQLite, agregado en el proyecto.

* **El mismo debe permitir realizar las operaciones CRUD del objeto y gestionar el inventario de los productos.** 

> Las operaciones CRUD de las entidades se explicaran en la sección **2. Módulos del proyecto.**

* **Agregar también un endpoint para vender productos en función a cantidad y precio. Se debe aplicar un recargo por IVA que por el momento será del 13%**

> La configuración para aplicar el recargo a las ventas se explicará en la sección **2.2 Módulo "sales"** 



#### 1.2 Diagrama ER - VentasBack

Diagrama ER del proyecto separado por aplicaciones.

![image](https://user-images.githubusercontent.com/30891977/212450788-86e9080c-dd81-4de2-b310-f397b85a3057.png)


#### 1.3 Colección de Datos API

Se agrego al proyecto una colección de datos "Postman" para realizar consultas a la API RESTful.



### 2. Módulos del proyecto

#### 2.1 Módulo "Storage"

Módulo o aplicación "Storage" contiene los datos básicos donde se gestionara el registro de inventario de almacén y sus dependencias. 

##### 2.1.1 Entidad "category"

Es utilizado para agrupar productos.

Datos del formulario:

* **name:** Nombre del proveedor

Contiene operaciones CRUD del modelo.

Contiene un campo personalizado que permite guardar el nombre de la categoría con mayúsculas cada inicio de palabra.

##### 2.1.2 Entidad "provider"

Es utilizado para identificar los proveedores de diferentes productos registrados en el inventario.

Datos del formulario:

* **name:** Nombre del proveedor
* **nit:** Numero de identificación tributaria del producto
* **phone:** Numero de teléfono del proveedor

Contiene operaciones CRUD del modelo.

Contiene un campo personalizado que permite guardar el nombre del proveedor con mayúsculas cada inicio de palabra.

##### 2.1.3 Entidad "product"

Entidad que representa un producto digital, el cual tiene los atributos básicos.

Datos del formulario:

* **name:** Nombre del producto
* **description:** Descripción del producto
* **product_type:** Tipo de producto (pieza, paquete, bolsa, caja, etc.)
* **category_id:** Categoría perteneciente al respectivo producto.

Contiene operaciones CRUD del modelo.

##### 2.1.4 Entidad "Inventario"

Entidad que representa un almacén de productos disponibles para la venta final. 

Datos del formulario:

* **price:** Precio final a la venta del producto.
* **quantity:** Cantidad de productos registrados al momento de ingresar al inventario. (Unidades)
* **base_price:** Precio base con el que se registro al momento de ingresar el producto al inventario.
* **provider_id:** Referencia al proveedor del que proviene el producto.
* **product_id:** Referencia a la información básica del producto.

Datos generados:

* **stock:** Campo auto calculado que valida la cantidad disponible en el inventario de esa partida. 

#### 2.2 Módulo "Sales"

##### 2.2.1 Entidad "tax"

Entidad en la que se registra todos los importes o recargas que se agregan en la factura o venta al finalizar la compra. 

Datos del formulario:

* **name:** Nombre del importe.
* **percentage:** Valor decimal mayor a 1 y menor a 100 el cual representa el valor de la tasa.

##### 2.2.2 Entidad "config_sales"

Entidad en la que se guarda la configuración para las ventas con el motivo de realizar el importe automático.  Solamente puede haber 1 configuración activa en la aplicación, por lo que cada registro o actualización de esta entidad afecta a las demás configuraciones habilitadas para generar las ventas. 

Datos del formulario:

* **name:** Nombre para identificar cada configuración registrada en la aplicación.
* **tax_list:** Contiene una lista de tarifas o recargas en el caso que según normativa cambie o se adicionen nuevas reglas. 

Datos generados:

* **active:** Valor booleano por defecto falso que identifica si la configuración esta vigente para las ventas. (Solo 1 activa en la aplicación) 

##### 2.2.3 Entidad "order"

Entidad que representa los pedidos registrados por el cliente, sin la necesidad de estar comprometidos a la venta de ellos, pero con la reserva. Tiene 3 estados 

* Pendiente: Pedido confirmado antes de realizar por la venta y pago del producto
* Aprobado: Pedido pagado y generado una venta.
* Cancelado: Pedido cancelado por el usuario o por la aplicación, según sea el caso (Stock agotado, El producto ya no se encuentra, etc.)

Datos del formulario:

* **quantity:** Cantidad de productos que el usuario solicita para comprar.
* **client_id:** Referencia al cliente el cual solicita el pedido.
* **inventory_id:** Referencia al inventario en donde se almacena el producto.

Datos generados:

* **order_state:** Estados del producto.
* **total_price:** Campo calculado que representa el costo total del producto por la cantidad. 

##### 2.2.4 Entidad "sales"

Entidad que representa las ventas de productos, en el cual se almacenan datos del pedido del cliente y los importes respectivos según periodo.

Datos del formulario:

* **orders_list:** Contiene una lista de pedidos el cual se ha confirmado por el cliente para realizar la compra.

Datos generados:

* **sales_state:** Estado de la venta, puede ser vigente o cancelado.
* **subtotal_amount:** Campo calculado a través del importe total de todos los pedidos.
* **total_amount:** Campo calculado aplicando las tarifas de recargas en base al subtotal de la venta.
* **config_id:** Campo asignado automáticamente cuando se realiza una venta, en caso de no haber una configuración salta un mensaje indicando el problema.

#### 2.3 Módulo "Authentication"

##### 2.3.1 Entidad "user"

Entidad que representa los datos de los usuarios que puede interactuar con la aplicación, para ello tenemos los siguientes roles:

* Tipo de usuario cliente
* Tipo de usuario supervisor
* Tipo de usuario administrador

Todos comparten la información básica del usuario exceptuando el estado o rol. 

Solo los clientes pueden realizar pedidos en la aplicación.

### 3. Seguridad del proyecto

Un control de seguridad agregado en la aplicación es la autentificación o autorización de usuarios mediante JWT.

### 4. Documentación

Para mantener un código legible se utilizo el estilo de documentación: "Style Python Docstrings".

