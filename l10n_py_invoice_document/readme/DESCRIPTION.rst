**Tipos de documentos usados en la contabilidad paraguaya**

- Definicion de los tipos de documentos en la localizacion
- Gestion de timbrados
- Agregado de datos necesarios a los formularios como ser Facturas, Contactos, Diarios, etc.

**Tipos de Cliente/Proveedor**

En Contabilidad / Tipos de socios de negocio se definen los tipos de Cliente/Proveedor, por ejemplo:

+-------------------------+-------------+---------------+-------------+---------------+
| Aplica | Tipo           | Oblig indiv | Oblig empresa | Consolidado | Cuenta predet |
+--------+----------------+-------------+---------------+-------------+---------------+
| Venta  | Cliente Local  |          NO |     SI        | 44444401-7  | 10.25.33.120  |
+--------+----------------+-------------+---------------+-------------+---------------+
| .....  | .....          |          .. |     ..        |   	.....       | .....   |
+----------+--------------+-------------+---------------+-------------+---------------+

Luego en el partner se define el tipo de cliente o de proveedor, y se utilizan
las reglas para determinar si el ruc es requerido o no dependiendo si es un
individuo o una empresa.
Si el ruc esta en blanco y la regla lo permite se usa el ruc consolidado para
la factura y el libro de iva

Ademas se definen cuentas contables predeterminadas, para las compras y las
ventas segun el caso.

**Cuenta separada para devoluciones**

Se define una cuenta adicional para las notas de credito en ventas.

Por ejemplo:
Un producto tiene *Cuenta de Ingresos* y una *Cuenta de Gastos*. Se le agrega otra
cuenta llamada *Cuenta de Ingresos (devolución)* para las notas de crédito.

Esta cuenta esta en la pestaña *Contabilidad* de la ficha del producto y en el
formulario de *Categoria de producto*.
