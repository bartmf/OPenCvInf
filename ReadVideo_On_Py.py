#add OpenCv Lib
import cv2

#creat object from VideoCapture, argument - is path to video file
#создаём объект класса VideoCapture, фргумент - это путь к видеофайлу(или просто название если он лежит в том же каталоге, что и скрипт)
cap = cv2.VideoCapture('video.mp4')

#cycle for if video not end, function isOpen() - boolean, when video is over, isOpen() return - false, and cycle is over
#цикл пока не закончится видео, функция isOpen() - булевая, когда кончится видео, isOpen() вернет - ложь
while(cap.isOpened()):

#function read() return two values, 1 - bool for errors (we place in "ret"), 2 - read fream ( We place in "frame")
#функция read() возвращает два значения, 1 - булевая для ошибок (false - если они есть), 2 - прочтённый кадр
 ret, frame = cap.read()

#its optional... cvtColor() is filter, 1 arg - is frame (logic =)), 2 arg - preset (in  "cvtColor presets.txt")
#это опционально... cvtColor() возвращает объект в цветовом представлении. 1 аргумент - это объект кадра, 2 - само цветовое представление (поместил в cvtColor presets.txt)
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#here we using imshow(), is function for show, 1 arg - name winndow, 2 arg - object
#функция для показа объекта в окне, 1 аргумент - название окна, объект для передачи в окно
 cv2.imshow('frame',gray)

#condition if you press button "q" to quit in cycle
#УЛовия досрочного выхода при нажатии 'q', кстати если задать для waitKey - 0, то кадр будет ждать пока мы что либо нажмём (если q то выход, если другую, сл. кадр)
 if cv2.waitKey(1) & 0xFF == ord('q'):
    break

#clear memory
#чистим память, точнее сожержимое cap
cap.release()

#lol destroy all windows XD
#Как не странно уничтожаем все окна
cv2.destroyAllWindows()
