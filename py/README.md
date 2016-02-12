#Build a Face Recognition System

These files demonstrate what it will be achieved at the end of the tutorial. But in the notebok and with better use of classes.

### Adding a new face to the dataset
To add add new faces to the dataset execute:

<code>
  $ python build_dataset.py NAME_OF_PERSON
</code>

This will try to find your face one time per second, if a face is detected a green rectangle is shown, 
together with the normalized face that is going to be saved to use later to train nthe algorithm.
Try to collect around 20 pictures. And make them differently!! even you look silly :).

Once the dataset has 2 or more people, execute:

<code>
  $ python recognition.py
</code>
