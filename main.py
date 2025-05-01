import cv2
import numpy as np
from matplotlib import pyplot as plt


def q1():
    # QUESTION 1
    image = cv2.imread("data\dental_xray.tif", cv2.IMREAD_COLOR)

    # part a
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to separate the bottle from the background
    _, thresh = cv2.threshold(gray, 167, 255, cv2.THRESH_BINARY)

    cv2.imshow("image", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # part b
    row, col = np.where(image[:, :, 0] >= 230)

    # Set those pixels to red color
    image[row, col] = [0, 0, 255]  # BGR color format, set red to [0, 0, 255]

    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # part c
    rows, cols, x = image.shape

    total_size = rows * cols

    # Create a binary mask where the pixels with the specified color are white
    mask = cv2.inRange(image, (0, 0, 255), (0, 0, 255))

    # Count the number of white pixels in the mask
    affected = cv2.countNonZero(mask)

    percentage_affected = (affected / total_size) * 100
    print(f"Filled percentage: {percentage_affected:.2f}%")


def q2():
    # QUESTION 2
    img = cv2.imread("data/brain.tif", cv2.IMREAD_GRAYSCALE)

    low_threshold = 200
    high_threshold = 255

    binary_img = np.zeros_like(img)
    binary_img[(img > low_threshold) & (img <= high_threshold)] = 1

    fig, axs = plt.subplots(1, 2)
    fig.suptitle('Intensity Slicing Result')

    axs[0].imshow(img, cmap='gray')
    axs[0].set_title('Original Image')

    axs[1].imshow(binary_img, cmap='gray')
    axs[1].set_title('Binary Image')

    plt.show()

    rows, cols = binary_img.shape
    white_in_row = []
    white_in_col = []

    # part b
    count = 0
    for i in range(0, rows):
        count = 0
        for j in range(0, cols):
            if binary_img[i, j] == 255:
                count = count + 1
        white_in_row.append(count)
    print(white_in_row)

    # part c
    for i in range(0, cols):
        count = 0
        for j in range(0, rows):
            if binary_img[j, i] == 255:
                count = count + 1
        white_in_col.append(count)
    print(white_in_col)


def logTransformations(img, gamma):
    # Apply gamma transformation
    c = 4
    # c = 1
    gamma_transformed = c * (img ** gamma)

    # Normalize the transformed image to 0-255 range
    gamma_transformed = np.uint8(gamma_transformed / np.max(gamma_transformed) * 255)

    # Display the transformed image
    cv2.imshow(str(gamma), gamma_transformed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def q3():
    # QUESTION 3
    img = cv2.imread("data/4.grain.tif", cv2.IMREAD_GRAYSCALE)

    # Define gamma value
    gamma = 0.7

    logTransformations(img, gamma)


def q4():
    # QUESTION 4
    # part a
    img = cv2.imread("data/4.grain.tif", cv2.IMREAD_GRAYSCALE)
    rows, cols = img.shape

    pixels = {}

    for i in range(0, rows):
        for j in range(0, cols):
            if img[i][j] in pixels:
                pixels[img[i][j]] = pixels[img[i][j]] + 1
            else:
                pixels[img[i][j]] = 1

    keys = list(pixels.keys())
    values = list(pixels.values())

    plt.bar(keys, values)
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.show()

    # part b
    # define the two box filters
    box_filter_3 = np.ones((3, 3), dtype=np.float32) / 9
    box_filter_7 = np.ones((7, 7), dtype=np.float32) / 49

    # apply the filters to the input image
    O3 = cv2.filter2D(img, -1, box_filter_3)
    O7 = cv2.filter2D(img, -1, box_filter_7)

    # calculate the final output image
    diff = cv2.absdiff(O7, O3)
    final_output = cv2.subtract(img, diff)

    # display the resulting image
    cv2.imshow('Final Output', final_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def checkBottleFill(image_path, threshold):
    # Load the image and convert it to grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    area_bottle = cv2.countNonZero(gray)

    # Create a binary mask where the pixels are between 1 and 254
    mask = cv2.inRange(gray, 1, 253)

    # Count the number of white pixels in the mask
    area_drink = cv2.countNonZero(mask)

    filled_percentage = (area_drink / area_bottle) * 100

    # Print the filled percentage and a message
    print(f"Filled percentage: {filled_percentage:.2f}%")
    if filled_percentage < threshold:
        print("Bottle is not properly filled")
    else:
        print("Bottle is properly filled")


def q5():
    # QUESTION 5
    checkBottleFill("data/bottle1.jpg", 85)
    checkBottleFill("data/bottle2.jpg", 70)


q1()
# q2()
# q3()
# q4()
# q5()
