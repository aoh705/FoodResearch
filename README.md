# FoodResearch

### Team Members:
- **Aimee Oh** (UNI: ao2686)
- **Steven Huang** (UNI: sh4013)

### This iteration of our project contains:
-  Instructions to run and test our product. (Found Below)
-  Code (All of the code is located in this Github repository).

### What our code produces:
-  loading of data from .csv files (in the 'data' file)
-  exploring a few columns from datasets
-  cleaning and pre-processing of data
    -  Using NTLK module for eliminating stopwords and reducing words to their simplest form
    -  Calculating sentiment of review text provided in the dataset
    -  Fitting review text to Tf-Idf and SVM model
-  statistical analysis of sentiment using Wilcoxon rank-sum test in the .Rmd file
-  creation of a new .csv file for each cleaned dataset (in 'altdata' file)

# Setting Up Your Environment:
## Python Notebooks
1. After setting up this repository locally, create a virtual environment with Python.
2. After creating a virtual environment, in your command line, type: `pip install -r requirements.txt`
This should install all the needed modules and packages to execute this code.
3. You are ready to execute the code in this repository. Good luck!

## R Markdown
1. For the `all_data.Rmd` file, it is ideal to open this Markdown file with Rstudio to run.
2. Once you open RStudio, please open this file.
3. Run the entire file to conduct all tests.
