# Welcome to CropLossAnalyzer, a cutting-edge platform revolutionizing crop damage estimation through the power of Deep Learning Transformers.

Our platform utilizes state-of-the-art technology and pre-trained models to predict change maps by analyzing two input images—providing accurate insights into crop damage assessment.

At CropLossAnalyzer, we harness the capabilities of Deep Learning Transformers, leveraging their advanced algorithms and neural networks to process imagery data. By inputting before-and-after images, our platform generates precise change maps, highlighting areas of crop damage, disease, or changes in vegetation cover.



Whether you're a farmer seeking to assess crop health or an agricultural expert monitoring vast fields, CropLossAnalyzer provides a reliable solution for understanding and managing crop damage.
Join us in revolutionizing the agricultural landscape with innovative Deep Learning technologies.

Empower your agricultural decisions with accurate crop damage estimation. Explore CropLossAnalyzer and experience the transformative potential of Deep Learning-based change map predictions today!

## Live Demo of Application
[click for demo](https://cute-gingersnap-6b7322.netlify.app/)

## Problem Statement

Many farmers are availing the crop insurance and benifited in case of 
crop damage due to natural calamaties such as floods. The challange 
for both insurance agancies and farmers is timely compansation and 
accurate estimation of damage. Manual process have many known 
bottlenecks and need reliable solution.

## Project Features

### Deep Learning Technology: 
Our platform integrates powerful Deep Learning Transformers, trained on vast datasets, to ensure robust and accurate predictions.

### Change Map Generation: 
Upload two images captured at different times, and our system swiftly processes them to create a detailed change map, highlighting alterations in the agricultural landscape.

### Precise Analysis: 
Gain actionable insights into the extent and nature of crop damage, facilitating prompt decision-making for farmers, agricultural experts, and stakeholders.

### User-Friendly Interface: 
A user-friendly interface allows seamless image upload, quick processing, and easy visualization of the predicted change maps.


## Tools Used

- Generative AI
- Machine Learning
- Deep Learning
- Flask
- Transformers
- Encoder - Decoder
- React
- HTML
- CSS
- Bootstrap

## Cropland-CD

The pytorch implementation for **MSCANet** in paper "[A CNN-transformer Network with Multi-scale Context Aggregation for Fine-grained Cropland Change Detection](https://ieeexplore.ieee.org/document/9780164)" on [IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing](https://www.grss-ieee.org/publications/journal-of-selected-topics-in-applied-earth-observations-and-remote-sensing/).  


## Datasets
### CropLand Change Dection (CLCD) Dataset
The CLCD dataset consists of 600 pairs image of cropland change samples, with 360 pairs for training, 120 pairs for validation and 120 pairs for testing.
The bi-temporal images in CLCD were collected by Gaofen-2 in Guangdong Province, China, in 2017 and 2019, respectively, with spatial resolution ranged from 0.5 to 2 m. Each group of samples is composed of two images of 512 × 512 and a corresponding binary label of cropland change.

- Download the CLCD Dataset: [OneDrive](https://mail2sysueducn-my.sharepoint.com/:f:/g/personal/liumx23_mail2_sysu_edu_cn/Ejm7aufQREdIhYf5yxSZDIkBr68p2AUQf_7BAEq4vmV0pg?e=ZWI3oy) | [Baidu](https://pan.baidu.com/s/1Un-bVxUm1N9IHiDOXLLHlg?pwd=miu2)
- Download the [HRSCD Dataset](https://ieee-dataport.org/open-access/hrscd-high-resolution-semantic-change-detection-dataset)



## Requirements
- Python 3.6
- Pytorch 1.7.0
  
## Models Used

An MSCANet with CNN-transformer hybrid architecture
is proposed for cropland CD, in which aMSCA is designed
to encode multiscale context information, and an MBPH
is utilized to improve deep feature learning.

![Entering News](https://github.com/PulijalaSaiRahul/Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model/blob/main/images/Screenshot%202024-08-05%20014454.png)

---
## How the Project Works

### 1. Landing Page of website

![Entering News](https://github.com/PulijalaSaiRahul/Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model/blob/main/images/Screenshot%202024-08-05%20012953.png)

Users can find the landing page built using React, it can be used with ease.

### 2. Uploading Before the change and After the change images for detection of damage

![Entry Point](https://github.com/PulijalaSaiRahul/Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model/blob/main/images/Screenshot%202024-08-05%20013011.png)

The users neeed to provide with the temporal images of the site where damage need to be predicted.

### 3. Sample Images 

#### Before Image
![Verifying News](https://github.com/PulijalaSaiRahul/Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model/blob/main/repeatfolder/time1/image1.png)

#### After Image
![Verifying News](https://github.com/PulijalaSaiRahul/Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model/blob/main/repeatfolder/time2/image1.png)

### 4. Output image predicted by the MSCANet model

![News Feed](https://github.com/PulijalaSaiRahul/Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model/blob/main/Output_images1/result1.png)

### 5. User must be Registered in the website and have an account to avail all services of CropAnalyzer

![Filtering Options](https://github.com/PulijalaSaiRahul/Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model/blob/main/images/Screenshot%202024-08-05%20013116.png)


## Installation

1. Clone the repository:

   ```bash
      git clone https://github.com/PulijalaSaiRahul/Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model.git
   ```

2. Install dependencies:

   ```bash
   cd Crop-Damage-Estimation-Using-Satellite-Image-and-Transformer-model
   pip install -r requirements.txt
   ```


## Usage

1. Run the application:

   ```bash
    npm start
   ```

   ```bash
    run the flash app for backend
   ```

2. Open your web browser and navigate to the provided local URL.

3. You can give input as image form where we will take the input image and using OCR we will extract the info from image
4.Please give images which has before and after timeline change.

## Configuration

Users can customize the project by modifying the Bard / Open API key. In case users encounter issues, they can replace the key in the configuration file.

## Future Enhancements

- **Database Integration:** Future plans include connecting the project to a database for data storage and retrieval.
- **Power BI Integration:** Explore options for enhancing interactivity by integrating the project with Power BI.


## Credits

- Generative AI
- Google Bard

## Contributions
- Pulijala Sai Rahul
- Vempati Sai Vishal
- Adoni Venkata Giri Vardhan
- Mamilla Thanish kumar
- Gorenkala Praneeth Sai
- Gangadhari Mouneesh

---


## Citation

```
@ARTICLE{9780164,
  author={Liu, Mengxi and Chai, Zhuoqun and Deng, Haojun and Liu, Rong},
  journal={IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing}, 
  title={A CNN-Transformer Network With Multiscale Context Aggregation for Fine-Grained Cropland Change Detection}, 
  year={2022},
  volume={15},
  number={},
  pages={4297-4306},
  doi={10.1109/JSTARS.2022.3177235}}
```
