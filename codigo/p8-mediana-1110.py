#Mario Yañez NC 1110
import cv2

# Cargar la imagen
imagen = cv2.imread("imagenes/gorrion.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(imagen, 7)

# Mostrar imágenes
cv2.imshow("gorrion original 1110", imagen)
cv2.imshow("Imagen con filtro de mediana 1110", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "resultados/gorrion.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("resultados/gorrion.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Mario Yañez NC 1110")