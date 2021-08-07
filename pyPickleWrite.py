import pickle

vaccine_details = {
    "Karnataka": {"Covishield": 5, "Covaxin": 2, "Sputnik": 1, "users": ["18", "45"]},
    "Delhi": {"Covishield": 15, "Covaxin": 12, "Sputnik": 0, "users": ["45"]},
    "Maharashtra": {"Covishield": 10, "Covaxin": 5, "Sputnik": 3},
}

# Binary mode for Write Operations
fh = open("vdStates", "wb") # wb => write + Binary mode

pickle.dump(vaccine_details, fh)

fh.close()