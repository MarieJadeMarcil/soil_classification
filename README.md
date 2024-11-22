# ARTIFICIAL VISION - FINAL PROJECT

**Author**: Marie-Jade Marcil
<br>
**Student ID**: 186239
<br>
**Date**: November 26, 2024
<br>

## RURAL COMMUNITIES: SOIL CLASSIFICATION FOR CROP RECOMMENDATIONS

### **Context**

This application and repertory was created to offer an web application to the agricultural rural communities. This application aims to help farmer reduce their resources to determine what soil type their dealing with and what crops they should prioratiize.

### **Model**

The Densely Connected Model DenseNet-121 was trained with the [Soil Type Dataset](https://www.kaggle.com/datasets/jayaprakashpondy/soil-image-dataset) and successfully predicted soil types and crop recommendations.

### **Installation**

**Clone the Repository**:

```sh
git clone https://github.com/yourusername/soil-classification-app.git
cd soil-classification-app

```

### **To Launch the Web App**

#### **Linux/Mac Users**:

1. **Make the Script Executable**:

   - Run the following command to give executable permissions to the script:
     ```sh
     chmod +x launch_app.sh
     ```

2. **Run the Script**:
   - To install dependencies and launch the web application, execute the script:
     ```sh
     ./launch_app.sh
     ```

This will automatically install all required dependencies and start the web application.

#### **Windows Users**:

- Simply double-click on `launch_app.bat` or run it via the command prompt:
  ```sh
  launch_app.bat
  ```

### **How it works **

1. **Upload a Soil Image**: The user uploads an image of the soil sample using the web interface.

2. **Soil Classification**: The trained DenseNet-121 model analyzes the uploaded image and predicts the soil type.

3. **Crop Recommendations**: The app then provides a list of crops suitable for the identified soil type.
   <br>

**Supported Soil Types:**

- Alluvial Soil
- Black Soil
- Clay Soil
- Red Soil

### **Acknowledgments**

- **Dataset**: This project uses the [Soil Image Dataset](https://www.kaggle.com/datasets/jayaprakashpondy/soil-image-dataset) made publicly available on Kaggle by Jayaprakash Pondy.

- **Inspiration**: Inspired by the need for accessible tools to assist rural communities in agriculture by utilizing AI to enhance decision-making for farmers.

* **Dataset Name**: Soil Image Dataset
* **Last Updated**: a years ago (Version 1)
* **Dataset URL**: [Soil Type Image Classification](https://www.kaggle.com/code/arjupaudel/soil-crop-recomendation/)

#### **About this Dataset**

This dataset is the cleaned up version of the [Soil Image Dataset](https://www.kaggle.com/datasets/jayaprakashpondy/soil-image-dataset), which had lots of corrupted images. The dataset contains 1555 images divided into two subsets (train and test set) of 4 classes each.
