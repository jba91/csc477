# CSC477 

Our dataset came from data.gov:

https://catalog.data.gov/dataset/crime-data-from-2010-to-present

This dataset contains crimes that occurred in the City of Los Angeles dating back to 2010.
Our goal was to predict the location (AreaID) of crimes based on this data.

The dataset has 26 fields but we only wanted to use (5) fields as we were interested in
crimes that had a human victim. We did not want to consider crimes involving property etc.

The fields we were interested were:

AreaID : CrimeID : Age : Gender : Race

AreadID is an integer from 1 to 21 representing the 21 police departments located in Los Angeles, CA.
CrimeID is a code used to indicate the type of crime committed - integer.
Age refers to the age of the victim of the crime - integer.
Gender: a character - M (Male) or F (Female)
Race: a character code - W for white, etc

We wrote `make_data_file.py` to parse the original csv file from data.gov and select only the fields we were interested in. We also converted all 5 fields to floating point values (see the code).

