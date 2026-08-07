
student_data = {
    "id1": {
        "name": "Sara",
        "class": "V",
        "subject_integration": "english, math, science"
    },
    "id2": {
        "name": "David",
        "class": "V",
        "subject_integration": "english, math, science"
    },
    "id3": {
        "name": "Sara",
        "class": "V",
        "subject_integration": "english, math, science"
    },  
    "id4": {
        "name": "Surya",
        "class": "V",
        "subject_integration": "english, math, science"
    }
}

result = {}
seen_keys = []  

for student_id, details in student_data.items():
    unique_key = (
        details["name"],
        details["class"],
        details["subject_integration"]
    )

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)


# Initialize dictionary
test_dict = {
    'Codingal': 2,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
K = 2

# Using loop
# Selective key values in dictionary
res = 0

for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

# printing result
print("Frequency of K is : " + str(res))