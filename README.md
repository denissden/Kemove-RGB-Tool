# Display images on your keyboard
This app helps you to convert images to Kemove files that are used for lighting up the keyboard

(insert images here)

### Usage
* run [main.py](../master/main.py)
* select your image
* export Kemove project file
* import project file in Kemove software 


### Technical information
The keyboard supports only 21 colors per project. To display the image on 61 keys colors need to be reduced.

Keys are numbered in rows from left to right. 

(insert image here)

The key map is stored in [map61key.json](../master/map61key.json) and can be generated using [generate_map61key.py](../master/generate_map61key.py)