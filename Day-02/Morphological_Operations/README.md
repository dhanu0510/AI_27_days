### Erosion

- A pixel in the original image (either 255 or 0) will be considered 255 only
  if all the pixels under the kernel is 255, otherwise it is eroded (made to
  zero).
- Make image thinner

<img src = "./images/Erosion.png" width = "500" height = "250">

### Dilation

- Just Opposite of Erosion Here, a pixel element is '255'
  if atleast one pixel under the kernel is '255'.
- Make image thicker

<img src = "./images/Dilation.png" width = "500" height = "250">

### Opening

- Erosion followed by Dilation!
  Many times used in Noise Removal !

<img src = "./images/Opening.png" width = "500" height = "250">

### Closing

- Reverse of Opening (Dilation followed by Erosion)

<img src = "./images/Closing.png" width = "500" height = "250">

### Gradient (Edge)

- Dilated Image - Eroded image (thicker - thinner)
- To find outlines of Objects

<img src = "./images/Gradient.png" width = "500" height = "250">

### Top Hat

- Difference between Input Image and its opening
- Highlights minor details in image (only)

<img src = "./images/TopHat.png" width = "500" height = "250">

### Black Hat

-Closing Input Image

- To find bright objects on dark background

<img src = "./images/BlackHat.png" width = "500" height = "250">
