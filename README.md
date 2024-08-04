# FactIT: Empowering Tech Users with Reliable Information

Welcome to CropLossAnalyzer, a cutting-edge platform revolutionizing crop damage estimation through the power of Deep Learning Transformers.
Our platform utilizes state-of-the-art technology and pre-trained models to predict change maps by analyzing two input images—providing accurate insights into crop damage assessment.

At CropLossAnalyzer, we harness the capabilities of Deep Learning Transformers, leveraging their advanced algorithms and neural networks to process imagery data. By inputting before-and-after images, our platform generates precise change maps, highlighting areas of crop damage, disease, or changes in vegetation cover.



Whether you're a farmer seeking to assess crop health or an agricultural expert monitoring vast fields, CropLossAnalyzer provides a reliable solution for understanding and managing crop damage.
Join us in revolutionizing the agricultural landscape with innovative Deep Learning technologies.

Empower your agricultural decisions with accurate crop damage estimation. Explore CropLossAnalyzer and experience the transformative potential of Deep Learning-based change map predictions today!

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



---
## How the Project Works

### 1. Entering News

![Entering News](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/image_1.png?raw=true)

Users can enter the news they want to verify. FactIT processes the entered news and provides an assessment of its authenticity, enriching the quality of the dataset.

### 2. Entry Point

![Entry Point](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/image_2.png?raw=true)

The entry point allows users to input news articles into the system.

### 3. Verifying News Authenticity

![Verifying News](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/image_3.png?raw=true)

FactIT evaluates the entered news, indicating whether it is true or false. It also provides information and credibility details, enhancing user trust in the information.

### 4. News Feed

![News Feed](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/image_4.png?raw=true)

Users can access a curated news feed enriched with verified information for their study purposes.

### 5. Date and Region Filtering

![Filtering Options](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/image_5.png?raw=true)

FactIT provides options to filter the news feed based on date and region, tailoring the information to specific user requirements.

## What Makes This Project Special

### Interactive Interface

![Interactive Features](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/ss7.jpg?raw=true)

FactIT comes with several distinctive features that set it apart from other education hubs and resources.

### Chat Bot Assistance

![Chat Bot](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/ss8.jpg?raw=true)

The project includes an interactive chatbot designed to assist users in understanding the application. If a user is confused, the chatbot provides guidance, enhancing the overall user experience.

### Auto-Populating Feature

![Auto-Populating Feature](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/ss9.jpg?raw=true)

FactIT introduces an auto-populating feature using Selenium. It alerts students if they are reading misleading or incorrect news, fostering a more informed educational experience.

### Focus on Natural Language Processing (NLP)

![NLP](https://github.com/vempatisaivishal/GlobalTruthHub/blob/main/images/ss10.jpg?raw=true)

The entire project is centered around Natural Language Processing (NLP), leveraging cutting-edge technologies to enhance the quality of news verification. The images below illustrate the NLP process.

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

Pulijala Sai Rahul
Vempati Sai Vishal
Mamilla Thanish kumar
Gorenkala Praneeth Sai
Gangadari Mouneesh

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
