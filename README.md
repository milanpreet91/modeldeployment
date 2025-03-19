# modeldeployment

1. Create a new repo on GITHUB 
2. Open codepace on github repo 
3. Anaconda : Python distribution, eases package management (to manage environment for an app). Using anaconda (which has a server), one can create and move around the environment file needed for an app
Environment: folder containing packages and dependencies for a specific application so dependencies of diff apps do not interfere with each other 
4. conda --version
5. Create a conda environment: conda create -n env_name python=version
6. conda init and open new bash
7. conda activate env_name python=version
8. pip install flask gunicorn pickle-mixin scikit-learn
9. Start creating flask basic app server
10. app.py & home_page.html
11. Import flask: from flask import Flask, request, 
12. Create instance of flask class
13. Register a route
14. Run flask app
15. Modify flask server to render an html template 
-----1. create html file in Templates directory, modify flask app to render html template, create a simple form with style tags that handles POST request (to server)
16. ML models (tokenizer and classifier) available as pickle files downloaded and saved in models folder
17. load the models and use them to predict if email is spam by predict function at predict route
18. Specify the action=/predict in HTML files form section to call predict function
19. home_page.html file will show the webpage which will be loaded at home and after the response received from predict function.
20. Deploy the app on cloud. For this you create the container out of the app by saving the packages and dependencies set by the environment into a requirements file