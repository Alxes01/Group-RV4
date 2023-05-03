# Integrating all programs into one
from capture import capture
from correction import correction
from match import match
from recognitiona import recognititiona
from order import order

# Defined path for images
path = "C:\\Users\\Peeta\\Desktop\\Robot\\RV1\\Results"
path_csv = "C:\\Users\\Peeta\\Desktop\\Robot\\RV1"

# Capturing the image with defined path for images
#capture(path)

# Undistortion of the captured image using values from calibration
correction(path)

# Aligning the picture with the reference picture
match(path)

# Recognition of lego bricks and location of their coordinates from captured image
pard = recognititiona(path)

# Array which contains how many of each figure is desired to be made
# [Marge, Lisa, Maggie, Homer, Bart]
figures = [1, 1, 1, 1, 1]

# Assembly of the figures
order(pard, figures, path_csv)

