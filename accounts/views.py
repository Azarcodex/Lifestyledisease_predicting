from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
#importing libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
#import xgboost as xgb
#from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
#import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.linear_model import LogisticRegression
# Create your views here.
def register(request):
       if request.method=='POST':
              first_name=request.POST['first_name']
              last_name=request.POST['last_name']
              username=request.POST['username']
              email=request.POST['email']
              password1=request.POST['password1']
              password2=request.POST['password2']
              if password1==password2:
                     if User.objects.filter(username=username).exists():
                            messages.info(request,"username already exists")
                            return redirect('register')
                     elif User.objects.filter(email=email).exists():
                            messages.info(request,"email already exists")
                            return redirect('register')
                     else:
                            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                            user.save();
                     return redirect('/')
              else:
                     messages.info(request,"password mismatched")
                     return redirect('register')
       else:
              return render(request,'register.html')
       
def login(request):
       if request.method=='POST':
              username=request.POST['username']
              password=request.POST['password']
              user=auth.authenticate(username=username,password=password)

              if user is not None:
                     auth.login(request,user)
                     return render(request,'operationsite.html')
              else:
                     messages.info(request,"invalid inputs")
                     return redirect('login')
       else:
              return render(request,'login.html')

#-------------------------------------------------------------------------------------"""
from django.shortcuts import render, redirect
import pandas as pd
import joblib

# Load model and label encoder once
model = joblib.load('models.pkl')
le_disease = joblib.load('le_disease.pkl')

# Define input maps
yes_no_map = {'yes': 1, 'no': 0}
gender_map = {'male': 1, 'female': 0}
bp_map = {'low': 0, 'normal': 1, 'high': 2}
cl_map = {'low': 0, 'normal': 1, 'high': 2}

def is_normal(x1,x2,x3,x4,x7,x8):
       return(
              x1==0 and
              x2==0 and
              x3==0 and
              x4==0 and
              x7==1 and
              x8==1
       )

def prediction(request):
    if request.method == 'POST':
        try:
            # Parse and preprocess input data
            val1 = float(yes_no_map.get(request.POST.get('Fever').lower(), 0))
            val2 = float(yes_no_map.get(request.POST.get('Cough').lower(), 0))
            val3 = float(yes_no_map.get(request.POST.get('Fatigue').lower(), 0))
            val4 = float(yes_no_map.get(request.POST.get('Difficulty Breathing').lower(), 0))
            val5 = float(request.POST.get('Age', 0))
            val6 = float(gender_map.get(request.POST.get('Gender').lower(), 0))
            val7 = float(bp_map.get(request.POST.get('Blood Pressure').lower(), 0))
            val8 = float(cl_map.get(request.POST.get('Cholesterol Level').lower(), 0))
            
            # Create input data frame
            if is_normal(val1,val2,val3,val4,val7,val8):
              message="Hey,You are completely normal,no disease detected."
            else:
              input_data = pd.DataFrame([[val1, val2, val3, val4, val5, val6, val7, val8]],
                                      columns=['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 
                                               'Age', 'Gender', 'Blood Pressure', 'Cholesterol Level'])
            
            # Predict disease
              prediction = model.predict(input_data)[0]
              result = le_disease.inverse_transform([prediction])[0]
              message=f"""You are at moderate risk for Lifestyle Disease {result} 
              Taking proactive steps now can help you lead a healthier and happier life"""

            return render(request, 'prediction.html', {"result": message})
        except Exception as e:
            return render(request, 'prediction.html', {"error": str(e)})
    else:
        return redirect('/')
