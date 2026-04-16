from PIL import Image
import json

face = Image.open("python_util/face2.png")

with open('python_util/circles.json', 'r') as file:
    circles = json.load(file)

circle_colors = []
circle_count = 1

for circle in circles:
    circle_color = [0, 0, 0]
    pixel_count = 0

    for y in range(face.height):
        for x in range(face.width):
            if (x - circle['x'])**2 + (y - circle['y'] + 100)**2 <= circle['radius']**2:
                pixel = face.getpixel((x, y))
                if pixel[3] > 0:
                    pixel_count += 1
                    circle_color[0] += pixel[0]
                    circle_color[1] += pixel[1]
                    circle_color[2] += pixel[2]
    
    if pixel_count <= 60:
        circle_color = [58, 64, 61]
    else:
        circle_color[0] = round(circle_color[0] / pixel_count)
        circle_color[1] = round(circle_color[1] / pixel_count)
        circle_color[2] = round(circle_color[2] / pixel_count)

    circle_colors.append(circle_color)

    print(str(circle_count) + " circles done")
    circle_count += 1


print(circle_colors)