# Concrete-Image-Classifier-Web-App
## Deployed to Heroku by hosting Github
https://cracked-uncracked.herokuapp.com/
### Since Deep Learning Libs use more Slug-size, I used Github hosting method.

## Below setup is to run in local machine
## Prerequisites

You'll need the following:

* [Git]
* [Python-3 latest version]
* [Heroku]
* [Tensorflow-2.2.0] Since VGG16 model was trained in Tensorflow-2.2.0.
* [Keras latest version]
* [Streamlit]

## 1. Clone the sample app

Now you're ready to start working with the app. Clone the repo and change to the directory where the sample app is located.
  ```
git clone https://github.com/SetThuHan/Concrete-Image-Classifier-Web-App.git
cd get-started-python
  ```
## 2. Run the app locally
```
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

Now view your app at: http://localhost:8501
```
## 3. Deploy the app to Heroku
```
First, you need to create an app in your new Heroku account, then follow the instructions shown below "Deploy" Tab in your new app dashboard.
```
