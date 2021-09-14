from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
class gesture_regcognize():
    def __init__(self):
        self.x1, self.y1 = 5, 5
        self.x2, self.y2 = 330, 330
        self.IMAGE_SIZE = 64
        self.CROP_SIZE = 330
        self.timer = 0
        self.previous_text = ""
        self.predicted_string = ""
        self.key_pressed = False

    def preprocess_data(self):
        self.datagen = ImageDataGenerator(rescale=1 / 255.,
                                          samplewise_center=True,
                                          samplewise_std_normalization=True,
                                          brightness_range=[0.8, 2.5],
                                          zoom_range=[0.8, 1.5])

    def create_labels(self):
        self.labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del', 'nothing', 'space']

    def predict_function(self,model):
        # Predicting the frame.
        prediction = np.array(model.predict(self.frame_for_model))
        predicted_class = self.labels[prediction.argmax()]  # Selecting the max confidence index.
        # Preparing output based on the model's confidence.
        prediction_probability = prediction[0, prediction.argmax()]
        return predicted_class,prediction_probability

    def run_function(self,model):
        ####
        self.preprocess_data()
        self.create_labels()
        cap = cv2.VideoCapture(0)
        while True:
            """
            x1,y1---------------
            |                   |
            |                   |
            |                   |
            |_________________x2,y2
            """
            _, frame = cap.read()
            # Simulating mirror image
            frame = cv2.flip(frame, 2)
            # Target area where the hand gestures should be.
            cv2.rectangle(frame, (self.x1, self.y1), (self.x2, self.y2), (255, 6, 6), 1)

            # Preprocessing the frame before input to the model.
            cropped_image = frame[5:self.CROP_SIZE, 5:self.CROP_SIZE]
            resized_frame = cv2.resize(cropped_image, (self.IMAGE_SIZE, self.IMAGE_SIZE))
            reshaped_frame = (np.array(resized_frame)).reshape((1, self.IMAGE_SIZE, self.IMAGE_SIZE, 3))
            self.frame_for_model = self.datagen.standardize(np.float64(reshaped_frame))

            cv2.putText(frame, "Place your left hand here",
                        (5, 400), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2, cv2.FILLED)

            # Create a blackboard to display predited text
            blackboard = np.zeros(frame.shape, dtype=np.uint8)
            cv2.putText(blackboard, "Hand Gestures to Text", (30, 40), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))
            # Predicting the frame.
            self.predicted_text, self.predicted_prob = self.predict_function(model)

            if self.predicted_prob > 0.5:
                # High pred prob.
                cv2.putText(blackboard, '{} - {:.2f}%'.format(self.predicted_text, self.predicted_prob * 100),
                            (30, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))
            elif self.predicted_prob > 0.2 and self.predicted_prob <= 0.5:
                # Low pred prob.
                cv2.putText(blackboard, 'Maybe {}... - {:.2f}%'.format(self.predicted_text, self.predicted_prob * 100),
                            (30, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

            res = np.hstack((frame, blackboard))
            cv2.imshow("Camera", res)

            interrupt = cv2.waitKey(1)
            if interrupt & 0xFF == 27:  # esc key
                break
            #if interrupt == ord('c'): key_pressed = True
        cap.release()
        cv2.destroyAllWindows()