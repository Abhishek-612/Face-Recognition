import os
import face_recognition
import camera,time



dataset=os.listdir('images')

count=0

current_image=camera.main()
print("Image obtained...")
print()
#print(current_image)
#current_image=face_recognition.load_image_file('images/'+dataset[7])
encoded_current_image=face_recognition.face_encodings(current_image)
#print(encoded_current_image)
print("Authenticating...")

for image in dataset:
    check_image=face_recognition.load_image_file('images/'+image)
    faces=face_recognition.face_encodings(check_image)

    for face in faces:
        encoded_check_image=face
        #print(encoded_check_image)

        result=face_recognition.compare_faces(encoded_current_image,encoded_check_image)
        #print(result)

        if len(result)==0:
            continue
        elif result[0]==True:
            count+=1
            
        encoded_check_image=[]


print()

if(count<len(dataset)/2):
    print("Not Matched")
    print(count)
else:
    print("Matched")
    print(count)
    print('\nAuthentication Successful!!')
