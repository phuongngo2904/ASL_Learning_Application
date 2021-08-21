import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
import tensorflow as tf
datagen = ImageDataGenerator(rescale=1/255.,
                                  samplewise_center=True,
                                  samplewise_std_normalization=True,
                                  brightness_range=[0.8, 1.0],
                                  zoom_range=[1.0, 1.2]
)
### LOADING MODEL
model = tf.keras.models.load_model('gesture_regconition_model.h5')
labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z','del','nothing','space']
cap = cv2.VideoCapture(0)

IMAGE_SIZE = 64
CROP_SIZE = 200
while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    # Target area where the hand gestures should be.
    cv2.rectangle(frame, (5, 5), (CROP_SIZE, CROP_SIZE), (0, 255, 0), 3)

    # Preprocessing the frame before input to the model.
    cropped_image = frame[0:CROP_SIZE, 0:CROP_SIZE]
    resized_frame = cv2.resize(cropped_image, (IMAGE_SIZE, IMAGE_SIZE))
    reshaped_frame = (np.array(resized_frame)).reshape((1, IMAGE_SIZE, IMAGE_SIZE, 3))
    frame_for_model = datagen.standardize(np.float64(reshaped_frame))

    # Predicting the frame.
    prediction = np.array(model.predict(frame_for_model))
    predicted_class = labels[prediction.argmax()]  # Selecting the max confidence index.

    # Preparing output based on the model's confidence.
    prediction_probability = prediction[0, prediction.argmax()]
    if prediction_probability > 0.5:
        # High confidence.
        cv2.putText(frame, '{} - {:.2f}%'.format(predicted_class, prediction_probability * 100),
                    (10, 450), 1, 2, (255, 255, 0), 2, cv2.LINE_AA)
    elif prediction_probability > 0.2 and prediction_probability <= 0.5:
        # Low confidence.
        cv2.putText(frame, 'Maybe {}... - {:.2f}%'.format(predicted_class, prediction_probability * 100),
                    (10, 450), 1, 2, (0, 255, 255), 2, cv2.LINE_AA)
    else:
        # No confidence.
        cv2.putText(frame, labels[-2], (10, 450), 1, 2, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    """
    # Got this from collect-data.py
    # Coordinates of the ROI
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]

    # Resizing the ROI so it can be fed to the model for prediction
    roi = cv2.resize(roi, (64,64))
    #roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    #_, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    #cv2.imshow("test", test_image)

    # Batch of 1
    img = image.img_to_array(roi)
    pred = model.predict(tf.expand_dims(img, axis=0))
    # Sorting based on top prediction
    pred_class = labels[pred.argmax()]
    print(pred_class)
    # Displaying the predictions
    cv2.putText(frame, pred_class, (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)


    cv2.imshow("Frame", frame)
    """
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # esc key
        break
cap.release()
cv2.destroyAllWindows()



