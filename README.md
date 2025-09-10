# Sistema de Gestión de Empleados

Este es un programa sencillo en Python para gestionar empleados en una pequeña empresa. Permite registrar empleados, visualizar la lista de empleados, calcular el total de la nómina y eliminar empleados por su ID.

---

## Funcionalidades

- Registrar un nuevo empleado con datos como ID, nombre, correo, teléfono, valor por hora y cargo.
- Mostrar la lista de empleados registrados, incluyendo su salario mensual calculado automáticamente.
- Calcular el total de la nómina mensual (sumando todos los salarios).
- Eliminar un empleado a partir de su ID.
- Salir del programa.

---

## Cómo usar

1. Ejecuta el script en Python 3.
2. Aparecerá un menú con las opciones disponibles.
3. Ingresa el número correspondiente a la acción que deseas realizar.
4. Sigue las instrucciones para ingresar datos o ver resultados.

---

## Detalles técnicos

- El salario mensual se calcula con la fórmula:  
  `salario = valor_hora * 8 (horas diarias) * 22 (días laborales mensuales)`

- Si no se especifica un valor por hora al registrar un empleado, el programa asigna automáticamente un valor de 6500.

---

## Ejemplo de uso

