def calc_images(rects, width, height):
    images = {}
    for name in rects.keys():
        image = load_image("images/{}.jpg".format(name))
        size = image.get_size()
        sc = list(size)
        if name == "crocs":
            sc[1] = int(width/(size[0]/size[1])/1.2)
            sc[0] = int(width/1.2)
        elif size[0] > size[1]:
            sc[1] = int(width/(size[0]/size[1]))
            sc[0] = width
        else:
            sc[0] = int(height/(size[1]/size[0]))
            sc[1] = height
        image = scale(image, tuple(sc))
        images[name] = image
    return images
