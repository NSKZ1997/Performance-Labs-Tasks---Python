#Задание #2 (task #2)
#Ключевой пункт: если два треугольника пободные, их углы одинаковые
import math

def get_vector(point1, point2): #Вектор из 2-х точик
    if len(point1) != len(point2):
        print("Заданные пункты должны быть в одинаковом прострастве")
        return None
    vector = []
    for i in range(len(point1)):
        vector.append(point2[i] - point1[i])
    return vector

def dot_product(vector1, vector2): #Скалярное производное
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result

def vector_length(vector): #Длина вектора
    length = 0
    for i in vector:
        length += i**2
    length = length ** 0.5
    return length

def get_angle(vector1, vector2): #Угл ммежду двумя векторами
    dotted = dot_product(vector1, vector2)
    angle = math.cos(dotted/(vector_length(vector1) * vector_length(vector2)) * math.pi/2)
    return angle * 90

#Очень важный момент: в ходе вычисление этой задачи, компютер совершает ошибки округление. По этому неодходимо
#обозначить диапазон ошибки, и проверять если данное число находится в его границах.
rounding_error = 10**-12

#Создаем пустой класс, куда далее будем добавлять треугольники
class Triangles:
    def check_if_similar(self, triangle1, triangle2):
        angles1 = list(triangle1.angles)
        angles2 = list(triangle2.angles)
        #Не нужно проверять первый элемент. Мы проверяем есть ли нужное нам расстояние в любом из элементов,
        #и удаляем уже использованные элементы
        while angles1:
            similar = False
            for i in range(len(angles1)):
                if angles1[0] + rounding_error > angles2[i] and angles1[0] - rounding_error < angles2[i]:
                    similar = True; break   
            angles1.remove(angles1[0])
        return similar

#Данные о треугольники и расстояние между его точек вычисляеться и находиться в этом классе.
class Triangle:
    def __init__(self, vertices):
        self.vertices = vertices
        self.angles = self.get_angles(vertices)
    
    def get_angles(self, vertices):
        angles = []
        vertices += vertices
        for i in range(len(vertices[:3])):
            vector1 = get_vector(vertices[i], vertices[i + 1])
            vector2 = get_vector(vertices[i], vertices[i + 2])
            angles.append(get_angle(vector1, vector2))
        return angles
        
triangles = Triangles()

#Читаем файл и извлекаем из него нужныю информацию.
with open('triangles_file.txt', 'r') as f:
    triangle_vertices = eval(f.read())
    
#Добавляем эту информацию в класс "triangles".    
counter = 0
for key, value in triangle_vertices.items():
    counter += 1
    new_list = []
    for key, value in value.items():
        new_list.append(value)
    setattr(triangles, 'triangle' + str(counter), Triangle(new_list))

#Проверяем, подобные ли треугольники   
similar = triangles.check_if_similar(triangles.triangle1, triangles.triangle2)

if similar: print("Данные треугольники подобные")
else: print("Данные треугольники не подобные")