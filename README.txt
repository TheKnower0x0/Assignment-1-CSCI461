Project Structure
Load Data (load.py): Reads Mall_Customers.csv, ensuring data loads successfully.

Data Preprocessing (dpre.py):

Cleans data by dropping duplicates and filling missing values with the median for columns like Age, Annual Income (k$), and Spending Score (1-100).
Encodes categorical values, scales features, reduces dimensions with PCA, and categorizes income into levels.
Exploratory Data Analysis (EDA) (eda.py): Provides insights:

Average age, gender distribution, spending score range, average income, and customer count by income level.
Modeling (model.py): Clusters data into three groups using K-means, saving cluster counts.

Visualization (vis.py): Creates a bar chart of the average spending score by income level.

Docker Setup
Build Docker Image:

docker build -t assignment1 .
Run Docker Container:

docker run -it assignment1

Execute Pipelines:

Load: python3 /home/doc-bd-a1/load.py /home/doc-bd-a1/Mall_Customers.csv

Preprocess: python3 /home/doc-bd-a1/dpre.py /home/doc-bd-a1/Mall_Customers.csv

EDA: python3 /home/doc-bd-a1/eda.py /home/doc-bd-a1/Mall_Customers.csv

Model: python3 /home/doc-bd-a1/model.py /home/doc-bd-a1/Mall_Customers.csv

Visualization: python3 /home/doc-bd-a1/vis.py /home/doc-bd-a1/Mall_Customers.csv


Extract Results:

Run final.sh to transfer results from the container to C:\bd-a1\service-result\ on your local machine.

Bonus Task:

GitHub Link: https://github.com/TheKnower0x0/Assignment-1-CSCI461.git
Docker Hub Link: https://hub.docker.com/r/xahmedmomenx/bigdata_assg1