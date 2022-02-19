# cypress-cucumber-auto-setup for behaviour-driven development
This is a tool written in python that automatically alters the json files and index.js such that a vue project created using vue CLI can use cypress and cucumber with cypress-cucumber-preprocessor without the user having to do it manually. I did this in my free time as I realized that such modifications are simple and should be automated instead of having to do it manually every time a new vue project is created.


# Requirements
This tool can only be used after the following requirements have been satisfied:

1. npm package has to be installed. (Windows users can use **nvm** to install npm)
2. vue cli has to be installed. (can be installed with : ` npm install -g @vue/cli`)

# Setup

1. launch the command line interface on windows or linux and navigate to where you want your vue 3 project to be.
2. write in the following command to create the vue project: ` vue create <your project's name>` (<b>*</b>)
3. copy and paste the python file from this repository inside the folder of your project. (<b>**</b>)
4. run the python script using the command "python main.py"

(<b>*</b>) the naming constraint on vue projects is that no capital letters are allowed.
(<b>**</b>) The Python scipt has to be on the same directory level as the folders "tests" and "src"


# Validation

You can check if you followed the steps correctly by running the following command in cmd inside the project's folder: `npm run test:e2e`
When that command runs successfully, you will see cypress UI with a single feature named "featureFileTest"


![cypressUI-1](https://user-images.githubusercontent.com/43525406/154819216-e041a64d-c478-4402-b070-3614144ec0ea.JPG)


If you click on it, the test should run and you should see the following:

![cypressUI-2](https://user-images.githubusercontent.com/43525406/154819219-095db26e-b006-49aa-9a0a-33674e406d8d.JPG)

Now you can start a new vue project with cypress and cypress-cucumber-preprocessor without all the hassle of setting up the dependencies! it's plug and play;)

