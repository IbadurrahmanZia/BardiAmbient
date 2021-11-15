from PIL import ImageGrab,Image
import tinytuya
import getip


device_id = ##get id from tinytuya.scan()

ip_address = getip.ip(device_id)


locale_key = ##get locale key from tuya website


device = tinytuya.BulbDevice(dev_id = device_id, address= ip_address, local_key= locale_key)
device.set_version(3.3)


def setColor(color):
    device.set_colour(color[0],color[1],color[2])

def get_colors(image_file, numcolors=1, resize=150):
    # Resize image to speed up processing
    img = Image.open(image_file)
    img = img.copy()
    img.thumbnail((resize, resize))

    # Reduce to palette
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=numcolors)

    # Find dominant colors
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    colors = list()
    for i in range(numcolors):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        colors.append(tuple(dominant_color))
    return colors[0]

while True:
    image = ImageGrab.grab()
    image.save('screenshot.png')
    setColor(get_colors('screenshot.png'))




