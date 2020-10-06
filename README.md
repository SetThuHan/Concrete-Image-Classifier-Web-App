# Concrete-Image-Classifier-Web-App

## This Repo can be used for hosting Github to Heroku and also running on local machine. 
### Deployed to Heroku by hosting Github : https://cracked-uncracked.herokuapp.com/ . 

First you need to open this link in your web browser, then push that browser to Background or Switch to another Web URL, after that, wait for few seconds, and then you can see the Web App is loaded : "concrete .Streamlit" on your browser. After all, you can enjoy it. Maximum size for uploading JPG image : 100 KB. 

If you upload something like 1MB image size, it will cause Overloads or Index to be out of bounds and try to reconnect Docker Container Framework. Please view sample image dataset here: https://github.com/SetThuHan/AI-Capstone-Final-Assignment/tree/master/concrete_data_week4. These datasets were used to fit the model with Pre-traind VGG16 model.

#### Since Deep Learning Libs use more Slug-size, I used Github hosting method. But there is still "Connection Timed Out" Issue because of large dataset. I tried all solutions found in Google. Better waiting re-connecting to the Web-App.

## Below setup is to run in local machine
## Prerequisites

You'll need the following:

* [Git]
* [Python-3 latest version]
* [Heroku]
* [Tensorflow-2.2.0] Since VGG16 Pre-trained model was fitted in Tensorflow-2.2.0. For training, validating & testing, here is a git-repo that contains image datas: https://github.com/SetThuHan/AI-Capstone-Final-Assignment/tree/master/concrete_data_week4
* [Keras latest version]
* [Streamlit]

## 1. Clone the sample app

Now you're ready to start working with the app. Clone the repo and change to the directory where the sample app is located.
  ```
git clone https://github.com/SetThuHan/Concrete-Image-Classifier-Web-App.git
cd Concrete-Image-Classifier-Web-App
  ```
## 2. Run the app locally
Install the dependencies listed in the [requirements.txt]
  ```
pip install -r requirements.txt
  ```
Or you can install all requirements manually using [pip]
Run the app.
  ```
streamlit run concrete.py
  ```
If streamlit command not found, you need to set its path to be executed manually using [chmod +x (your-dir-path/bin/streamlit)].
When streamlit's run-time Syntax error found even after setting above method, you need to update [dateutils].
```
Now your web app will be automatically generated and open in browser.
```
## 3. Deploy the app to Heroku
```
First, you need to create an app in your new Heroku account, then follow the instructions shown below "Deploy" Tab in your new app dashboard.
```
