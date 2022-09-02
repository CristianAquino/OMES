import cv2
from setting import get

imagen = cv2.imread(get('img1'), 0)  # 1= color,0 = grises
cv2.imshow('POKEMON', imagen)  # para visualizar
cv2.imwrite('img/grises.jpg', imagen)  # crear y guardar una nueva imagen
cv2.waitKey(0)  # tiempo visualizacion
cv2.destroyAllWindows()  # cerrar todas las ventanas
