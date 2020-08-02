

# importing the shiny new class
from mrivis import Collage

# creating a collage is super easy - with default layout
collage = Collage()

# displaying an MR image with default layout is as simple as attaching it
collage.attach(scaled_img_one)

# and then we can simply show it
plt.show(collage.fig) 


