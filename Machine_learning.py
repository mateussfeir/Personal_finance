import pandas as pd
import string
from nltk.corpus import stopwords
import nltk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Step 1: Load the data
# Loading the csv file in a pandas data frame

df = pd.read_csv("bmo_jan23.csv", skiprows=[0], header=None, names=["card_number", "transaction_type", "date", "amount", "description"])
 
''' Let's break down the parameters used in the read_csv() function:

skiprows=[0] skips the first row of the CSV file, which contains the timestamp information.
header=None specifies that the CSV file does not have a header row.
names=["card_number", "transaction_type", "date", "amount", "description"] specifies the column names we want to use for the DataFrame.
With this code, you should be able to load the data from your CSV file into a pandas DataFrame called df.
'''

# Step 2: Data cleaning
# This code removes any duplicates and null values from the DataFrame and keeps only the columns we need for our analysis.

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df = df[["date", "description", "amount"]]

# Step 3: Data Preprocessing
# This code preprocesses the text data in the "description" column by removing punctuation, stop words,
# and converting all text to lowercase.

nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join([word for word in text.split() if word not in stopwords.words('english')])
    return text

df["preprocessed_description"] = df["description"].apply(preprocess_text)

# Step 4: Categorize Transactions
# This code categorizes transactions based on specific keywords in the preprocessed description column.

def categorize_transaction(description):
    if "interac etrnsfr" in description:
        return "Personal Transactions"
    elif "ib" in description:
        return "Cash deposit"
    elif "insurance" in description:
        return "Insurance Costs"
    elif "doordash" in description or "uber" in description:
        return "Delivery Income"
    elif "mobile cheque deposit" in description:
        return "Cheque deposit"
    elif "interactive brk" in description:
        return "TFSA deposit"
    elif "medallion" in description:
        return "Rent Costs"
    else:
        return "other"

df["category"] = df["preprocessed_description"].apply(categorize_transaction)

# Step 5: Feature Extraction
# This code extracts the relevant features by checking if the preprocessed text in the "description" column contains
# certain keywords that correspond to each category. We define a list of features that we want to extract, and then 
# loop through each feature to create a new column in the DataFrame with a Boolean value indicating whether the
# feature is present in the transaction description or not.

features = ["personal transactions", "insurance costs", "other"]
for feature in features:
    df[feature] = df["category"].apply(lambda x: 1 if x == feature else 0)

# Step 6: Training Data
# This code creates the training data set by selecting the features we extracted in Step 5 as inputs (X) and the corresponding
# category labels as outputs (y). We then split the data into training and testing sets using the train_test_split() function
# from scikit-learn.

X = df[features]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Model Training
# This code trains a logistic regression model on the training data using scikit-learn's LogisticRegression() function
# initialize the logistic regression model
model = LogisticRegression()

# fit the model on the training data
model.fit(X_train, y_train)

# make predictions on the test data
y_pred = model.predict(X_test)

# calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Step 8: Calculate total spending per category

category_totals = {}
total = float(0)

for category in df["category"].unique(): 
    try:
        total = df.loc[df["category"] == category, "amount"].astype(float).sum()
        category_totals[category] = total
    except ValueError:
        print(f"Error: could not convert amount to float for category {category}")
        continue

for category, total in category_totals.items():
    print(f"Total {category}: ${float(total):.2f}")
