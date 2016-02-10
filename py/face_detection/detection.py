import cv2

# paths to the trained models by opencv to detect faces and eyes
path = 'face detection/cascades/haarcascades/'
frontal = path + 'haarcascade_frontalface_alt.xml'
side = path + 'haarcascade_profileface.xml'
eye = path + 'haarcascade_eye.xml'

# Create classifier objects
face_class = cv2.CascadeClassifier(frontal)
side_class = cv2.CascadeClassifier(side)
eye_class = cv2.CascadeClassifier(eye)

# Draw the rectangle on the detected face
def draw_faces(frame,faces):
    for (x,y,w,h) in faces:
        # Green rectangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    return frame

def detect_frontal_face(frame_gray):
    # Change to True if we want to detect only one face
    biggest_only = False
    ''' The algorithm checks for faces of different sizes, 
    the scale_factor is how much difference is between each size
    that you want to check. 
    A bigger scale_factor means bigger jumps so it will perform
    faster but less accuratelly, it is recommended 1.2 or 1.3 '''
    scale_factor = 1.2
    '''Treshold to detect a face, it needs a minimum of min_neighbors
    neighbor pixels to return a detected a face  on that pixel'''
    min_neighbors = 10
    # Sets the min_size of the face we want to detect
    # Default is 20x20
    min_size = (120,120)
    # Defines how we want the algorithm to run
    flags = cv2.CASCADE_FIND_BIGGEST_OBJECT | \
            cv2.CASCADE_DO_ROUGH_SEARCH if biggest_only else \
            cv2.CASCADE_SCALE_IMAGE
            
    faces = face_class.detectMultiScale(frame_gray,
                                        scale_factor,
                                        min_neighbors,
                                        flags,
                                        min_size)
    return faces

def cut_faces(frame,faces):
    people_faces = []
    for (x,y,w,h) in faces:
        people_faces.append(frame[y: y + h, x: x + w])
    return people_faces

def normalize_faces(faces, color=False, size=(100,100)):
    for i, face in enumerate(faces):
        #print 'Normalizing image: ' + str(i+1) + '/' + str(len(faces))
        if color:
            face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        if face.shape < size:
            face_norm = cv2.resize(face,size,
                                    interpolation = cv2.INTER_AREA)
        else:
            face_norm = cv2.resize(face,size,
                                    interpolation = cv2.INTER_CUBIC)
        faces[i] = cv2.equalizeHist(face_norm)
    return faces

    

##### FUNCTIONS TO DETECT ROTATED/TILTED FACES #####

def detect_side_face(frame_gray):
    # Change to True if we want to detect only one face
    biggest_only = False
    ''' The algorithm checks for faces of different sizes, 
    the scale_factor is how much difference is between each size
    that you want to check. 
    A bigger scale_factor means bigger jumps so it will perform
    faster but less accuratelly, it is recommended 1.2 or 1.3 '''
    scale_factor = 1.2
    '''Treshold to detect a face, it needs a minimum of min_neighbors
    neighbor pixels to return a detected a face  on that pixel'''
    min_neighbors = 10
    # Sets the min_size of the face we want to detect
    # Default is 20x20
    min_size = (120,120)
    # Defines how we want the algorithm to run
    flags = cv2.CASCADE_FIND_BIGGEST_OBJECT | \
            cv2.CASCADE_DO_ROUGH_SEARCH if biggest_only else \
            cv2.CASCADE_SCALE_IMAGE
            
    faces = side_class.detectMultiScale(frame_gray,
                                            scale_factor,
                                            min_neighbors,
                                            flags,
                                            min_size)  
    return faces 

# This function rotates the frame
def rotate_frame(img,rotation_matrix):
    rows,cols = img.shape
    img_rotated = cv2.warpAffine(img,rotation_matrix,(cols,rows))
    return img_rotated

def detect_rotated_face(frame_gray):
    '''The idea was to perform rotations to the frame and detect the 
    face in this rotated frame, then based on the rotation matrix
    transform the rectangle to the original frame orientation '''
    # Rotation angle set to 45 for testing clockwise
    angle = 45
    rows,cols = frame_gray.shape
    # Perform rotation
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    img = rotate_frame(frame_gray,M)
    faces = detect_frontal_face(img)
    # Extract coordinates for then rotate the rectangle back
    if len(faces) != 0:
        x = faces[0][0]
        y = faces[0][1]
        # Rotation matrix from linear algebra check wikipedia for info
        M_la = M[:,:2] 
        # Rotate back the coordinates
        ''' Transformation back not working properly because apparently
        opencv returns a rotation matrix different from the known 
        rotation matrix in linear algebra, i think it is returning the off
        diagonal term of the matrix with a negative sign M_la '''
        faces[0][0],faces[0][1] =  np.dot(np.linalg.inv(M_la),[x,y])

    return faces, img
