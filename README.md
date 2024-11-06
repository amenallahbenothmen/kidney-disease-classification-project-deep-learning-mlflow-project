

## Project Overview

The **MLOps-Driven Deep Learning Web App for Disease Classification** is a comprehensive application designed to classify kidney diseases using medical data. By implementing state-of-the-art deep learning models and leveraging MLOps methodologies, the project aims to provide accurate disease classification and streamline the deployment process for continuous integration and delivery.

## Features

- **Medical Data Analysis**:Processes and analyzes medical datasets for model training and evaluation.
- **Deep Learning Models**:Utilizes advanced neural networks for accurate disease classification.
- **Containerization**: Employs Docker for easy deployment and scalability.
- **Experiment Tracking**: Integrates MLflow for tracking model performance and experiments.
- **Data Version Control**: Uses DVC for efficient data management and reproducibility.



## Prerequisites

- **Python 3.9** 
- **Docker**
- **DVC**
- **MLflow**
- **TensorFlow**
- **Flask**

## Setup and Installation

Follow the steps below to set up and run the application:

### 1. Clone the Repository

```bash
git clone https://github.com/amenallahbenothmen/kidney-disease-classification-project-deep-learning-mlflow-project
cd kidney-disease-classification-project-deep-learning-mlflow-project
```

### 2.Create a Virtual Environment

```bash
conda create -n kidney-disease-classification python=3.9
conda activate kidney-disease-classification
```


### 3.Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```
