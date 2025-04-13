# import pandas as pd
# import json
# import requests
# import tagme
# import re
# # import wikipedia
# from tqdm import tqdm
# import pickle
# import sys

# input_file = sys.argv[1]
# output_file = sys.argv[2]

# informative_train_df = pd.read_csv(input_file, sep = '\t',encoding='utf-8')
# print(informative_train_df)


# def preprocess(text):
#     return re.sub(r"[:,\n\r;@#!]|http[s]?://\S+|\.\s*|[^\x00-\x7F]+", '', text)



# informative_train_df['tweet_text'] =  informative_train_df['tweet_text'].apply(lambda x: preprocess(x) )


# informative_train_df['final_text'] = informative_train_df['tweet_text']+ informative_train_df['event_name']

# final_text=[]
# for i,row in tqdm(informative_train_df.iterrows(), total= len(informative_train_df)):
#     final_text.append(row['final_text'])


# with open(output_file, 'w', encoding='utf-8') as f:  # Use 'w' mode for text
#     for text in final_text:
#         f.write(text + '\n')

import pandas as pd
import re
import sys
from tqdm import tqdm

# Get input and output file paths from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the input TSV file
informative_train_df = pd.read_csv(input_file, sep='\t', encoding='utf-8')

# Function to preprocess tweet text
def preprocess(text):
    return re.sub(r"[:,\n\r;@#!]|http[s]?://\S+|\.\s*|[^\x00-\x7F]+", '', str(text))

# Apply preprocessing to the 'tweet_text' column
informative_train_df['tweet_text'] = informative_train_df['tweet_text'].apply(preprocess)

# Create a new column 'final_text' by combining 'tweet_text' and 'event_name'
informative_train_df['final_text'] = informative_train_df['tweet_text'] + ' ' + informative_train_df['event_name']

# Save the modified DataFrame back to a TSV file
informative_train_df.to_csv(output_file, sep='\t', index=False, encoding='utf-8')

print(f"Successfully processed: {input_file} -> {output_file}")






