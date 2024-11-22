import cv2
import gradio as gr
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# DenseNet121 with Fine-Tuning on Soil Dataset
model = load_model('./models/soil_classificator_3.keras')


def classify_image(image):
    # Preprocess the image
    preprocessed_image = preprocessing_pipeline(image)
    preprocessed_image = np.expand_dims(preprocessed_image, axis=0)  # Add batch dimension

    # Predict using the model
    predictions = model.predict(preprocessed_image)
    index = np.argmax(predictions, axis=1)[0]  # Get the class index
    probabilities = predictions[0]  # Probabilities for all classes

    # Define soil types and their associated crops
    soil = {
        "Alluvial soil": "Rice, SugarCane, Maize, Cotton, Soyabean, Jute",
        "Black Soil": "Wheat, Virginia, Jowar, Millets, Linseed, Castor, Sunflower",
        "Clay soil": "Rice, Lettuce, Chard, Broccoli, Cabbage, Snap Beans",
        "Red soil": "Cotton, Pulses, Millets, Oilseeds, Potatoes",
    }
    labels = list(soil.keys())

    # Get predicted soil type and recommended crops
    predicted_soil = labels[index]
    recommended_crops = soil.get(predicted_soil, "No crop recommendations available.")

    # Format probabilities for display
    probabilities_str = "\n".join(
        [f"{label}: {prob:.2f}" for label, prob in zip(labels, probabilities)]
    )

    return f"{predicted_soil}", f"{recommended_crops}", f"{probabilities_str}"



def preprocessing_pipeline(input_image):
    """
    Preprocess the input image: Contrast enhancement, noise reduction, resizing, normalization.
    """
    target_size = (224, 224)

    # Enhance Contrast
    #input_image = equalize_this(image_file=input_image, with_plot=False)

    # Convert input to a NumPy array if it's a PIL image
    if isinstance(input_image, Image.Image):
        image = np.array(input_image)
    elif isinstance(input_image, np.ndarray):
        image = input_image  # If it's already a NumPy array
    else:
        raise ValueError("Input must be a PIL image or NumPy array")

    # Ensure the image is in RGB format
    if len(image.shape) == 3 and image.shape[-1] != 3:
        raise ValueError("Input image must have 3 channels (RGB)")

    # Apply Noise Reduction
    image = cv2.bilateralFilter(image, 9, 75, 75)

    # Resize image to 224x224
    image = cv2.resize(image, target_size)

    # Normalize pixel values to range [0, 1]
    image = image / 255.0

    return image


demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=[
        gr.Textbox(label="Soil Type"),           # First output: Soil type
        gr.Textbox(label="Recommended Crops"),   # Second output: Recommended crops
        gr.Textbox(label="Class Probabilities"), # Third output: Probabilities
    ],
    title="Soil Type Classification and Crop Recommendation",
    description="Upload a soil image, and this app will classify the soil type, recommend suitable crops, and show prediction probabilities.",
)


if __name__ == "__main__":
    demo.launch(share=False, debug=True)

