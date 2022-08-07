# practise for NFT creation
# Date  : 17/7/2022
# author : gaurav

from PIL import Image,ImageDraw,ImageChops
import random
import colorsys

def random_color():
    # return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    h = random.random()
    s = 1
    v = 1

    float_color = colorsys.hsv_to_rgb(h,s,v)
    rgb = [int(x*255) for x in float_color]
    return tuple(rgb)

def interpolate(start_color,end_color,factor : float):
     reciprocal = 1- factor
     return(
            int(start_color[0] * reciprocal + end_color[0]*factor),
            int(start_color[1] * reciprocal + end_color[1]*factor),
            int(start_color[2] * reciprocal + end_color[2]*factor)
           )
def Generator(path : str):
    print("Generation started!")
    image_size_px = 256 
    padding = 12
    image_color = (0,0,0)
    start_color = random_color()
    end_color  = random_color()
    image = Image.new("RGB", size=(image_size_px,image_size_px), color=(image_color))
    #draw lined
    draw = ImageDraw.Draw(image)
    points_1 = []
    
    #creating points 
    for _ in range (15):   
        random_val_1 = (
            (random.randint(padding ,(image_size_px - padding))),
            (random.randint(padding,(image_size_px - padding))
            ))
        points_1.append(random_val_1)
    
    # draw bounding box

    #minimum of x and y
    min_x  = min([p[0] for p in points_1])
    min_y  = min([p[1] for p in points_1])
    #maximun of x and y
    max_x  = max([p[0] for p in points_1])
    max_y  = max([p[1] for p in points_1])
    #draw.rectangle((min_x  ,min_y  ,max_x,max_y),outline = ("red"))

    #cenre the image
    delta_x = min_x - (image_size_px - max_x)
    delta_y = min_y - (image_size_px - max_y)
    for i,point in enumerate(points_1):
        points_1[i] = (point[0] - delta_x //2 , point[1]- delta_y)

    
    # min_x  = min([p[0] for p in points_1])
    # min_y  = min([p[1] for p in points_1])
    # #maximun of x and y
    # max_x  = max([p[0] for p in points_1])
    # max_y  = max([p[1] for p in points_1])
    # draw.rectangle((min_x  ,min_y  ,max_x,max_y),outline = ("black"))

    #draw points
    thickness = 0
    n_points = len(points_1) - 1
    for i,point in enumerate(points_1):
        
        image_overlay = Image.new("RGB", size=(image_size_px,image_size_px), color=(image_color))
        image_draw = ImageDraw.Draw(image_overlay)

        point_1 = point
        if i == n_points:
            point_2 = points_1[0]
        else:
            point_2 = points_1[i+1] 
        line_xy = (point_1,point_2)
        #ellipse_xyz = (point_1,point_2) #used for concentric circles.
        thickness += 1 
        factor = i /  n_points
        color_black = interpolate(start_color , end_color , factor)
        image_draw.line(line_xy, fill=color_black,width=thickness)
        #image_draw.ellipse(ellipse_xyz , fill=color_black , outline= 1,width=1) # circle idea 
        image = ImageChops.add(image , image_overlay)
    
    image = image.resize((image_size_px,image_size_px) ,Image.ANTIALIAS)
    image.save(path)
    print("Generation completed!")


if __name__ == "__main__":
    for i in range(10):
        Generator(f"output{i}.png")