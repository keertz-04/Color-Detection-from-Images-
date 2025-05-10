import cv2
import webcolors
import sys

def get_color_name(R, G, B):
    try:
        return webcolors.rgb_to_name((R, G, B))
    except ValueError:
        closest_color = min(webcolors.CSS3_HEX_TO_NAMES,
                            key=lambda k: sum((v - c) ** 2 for v, c in zip(webcolors.hex_to_rgb(k), (R, G, B))))
        return webcolors.CSS3_HEX_TO_NAMES[closest_color]

def show_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        color_name = get_color_name(r, g, b)
        text = f'{color_name} (RGB: {r}, {g}, {b})'
        img_copy = img.copy()
        cv2.rectangle(img_copy, (10, 10), (350, 50), (b, g, r), -1)
        cv2.putText(img_copy, text, (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255-b, 255-g, 255-r), 2)
        cv2.imshow('Color Picker', img_copy)

if __name__ == '__main__':
    image_path = sys.argv[1] if len(sys.argv) > 1 else 'sample_image.png'
    img = cv2.imread(image_path)
    if img is None:
        print(f'Failed to load image: {image_path}')
        sys.exit(1)
    cv2.imshow('Color Picker', img)
    cv2.setMouseCallback('Color Picker', show_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
