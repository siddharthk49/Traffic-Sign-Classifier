This project implements a Convolutional Neural Network (CNN) for automatic traffic sign recognition. The system aims to classify various traffic signs from images, contributing to the development of advanced driver-assistance systems (ADAS) and autonomous vehicles.

Key Features:
    Data Loading and Preprocessing:
    Loads traffic sign images from a pickle file.
    Normalizes the pixel values of the images.
    Converts RGB images to grayscale.
    Model Architecture:
    Implements a sequential CNN model with multiple layers.
    Uses Conv2D layers with ReLU activation for feature extraction.
    Employs AveragePooling2D for downsampling.
    Includes Dense layers with ReLU and softmax activations for classification.
    Training:
    Compiles the model with sparse categorical cross-entropy loss and Adam optimizer.
    Trains the model on preprocessed training data.
    Evaluates performance using validation data.
    Evaluation:
    Calculates test accuracy.
    Plots training/validation accuracy and loss curves.
    Generates confusion matrix for visualizing classification errors.
    Visualization:
    Displays sample images with predicted classes.
    Creates heatmaps of confusion matrices for better visualization.
This project demonstrates a comprehensive approach to traffic sign recognition using deep learning techniques. It showcases data preprocessing, model architecture design, training, evaluation, and visualization methods for image classification tasks. The system can be further extended or integrated into larger ADAS systems for real-world applications.