import face_recognition

# Load an image of the person you want to recognize
known_image = face_recognition.load_image_file("person1.jpg")

# Encode the person's face into a vector
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Create an array of known face encodings and their names
known_face_encodings = [known_face_encoding]
known_face_names = ["Person 1"]

# Load an image where you want to identify faces
unknown_image = face_recognition.load_image_file("unknown.jpg")

# Find all face locations and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # If a match is found, use the name of the known face
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Print the location and name of the recognized face
    print(f"Found {name} at top:{top}, right:{right}, bottom:{bottom}, left:{left}")