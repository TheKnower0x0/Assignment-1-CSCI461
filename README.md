Steps Performed

1. Dockerfile Setup

Base Image: Used ubuntu:latest.

Environment: Installed Python 3 and dependencies (pandas, numpy, seaborn, matplotlib, scikit-learn, scipy) in a virtual environment.

Files: Copied dataset (Mall_Customers.csv) and Python scripts (load.py, dpre.py, eda.py, vis.py, model.py) to the container.

2. Data Preprocessing (dpre.py)

Data Cleaning & Transformation: Filled missing values, encoded Genre, scaled features, and performed PCA.

Income Level Binning: Added Income_Level by binning Annual Income (k$).

Output: Saved as res_dpre.csv.

3. Exploratory Data Analysis (eda.py)

Insights: Generated insights like average age, gender distribution, and spending score.

Output: Saved insights to .txt files.

4. Visualization (vis.py)

Chart: Created a bar chart of average spending score by income level.

Output: Saved as vis.png.

5. Clustering (model.py)

K-means Clustering: Clustered customers and saved cluster info to k.txt.

6. Bash Script (final.sh)

Script Actions: Managed container, copied output files to /result, and transferred results to local machine (C:\bd-a1\service-result).

Bonus Task:

GitHub Link: https://github.com/TheKnower0x0/Assignment-1-CSCI461.git
Docker Hub: 
