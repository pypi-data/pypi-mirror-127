## json txt

With the help of json txt you can use your txt file as a json file in a very simple way

## Dependencies 
- re
- filemod `pip install filemod` 
- colored `pip install colored`

### Installation and Usage

1. use `pip install json_txt`
2. Make sure that your `pip` version is updated `pip install --upgrade pip`. 
3. Import the package: ``import json_txt``

# Updates

1. Complete changed algorithm to find keys and values and 
its faster than ever.
2. Strings are also supported in the module.
3. New compiler is designed it will be used when if you use
load_txt() method if all test gets passed it will reaturn the file text
4. Now you can use integer values in variable due to new algorithm

### Functions in the module 

1)First load the data of the file using load_txt method you need to load 
data every time you make changes to it as it is using txt as its main source
`json_txt.load_txt(filename)`

2)extract_keys method helps you extract all the keys from the txt file , and returns them all in the list
`json_txt.extract_keys(data).`

3)extract_values method helps you extract all the values from the specific keys in sequence from the txt file , and returns them in the list.
`json_txt.extract_keys(data).`

4)extract_data method helps you extract all the key value pairs from the txt file to dict
`json_txt.extract_data(filename)`

5)edit_data method helps you edit key's value pair , it takes filename ,key, and a value to change.
`jason_txt.edit_data(filename,key,value_to_change)` 

6)Helps you detect weather the var is int or not returs bool
`json_txt.number_detect(letter)`




## Run Locally

Clone the project

```bash
  git clone https://github.com/kshitij1235/Json_txt/tree/main/dist
```

Install

```bash
  pip install json_txt
```

## List of Functions

| functions | processs| args|
| ----------|---------|-----|
|load_txt|loads the txt data|filename|
|extract_keys|extract key from data|data|
|extract_values|extract values from data|data|
|extract_data|Extracts key value pair|filename|
|edit_data|Edit certain key values|filename,key,value_to_change|
|add_data|Help add data to the txt| filename,new key , new value|

## Usage/Examples

### way to write your txt

```txt
{ 
settings:"active"
x:4
truck:32
}

Rules : 
1) Dont make any sub tree to write your data do it under one tree/{}
4)strictly use : when assigning values
```

### code

```python
import json_txt

###printing basic dictornary 
file=json_txt.load_txt("main.txt") #load the txt file
print(json_txt.extract_data(file)) #printing key value pairs

###adding and editing values 

add_data('main.txt',"sleep","disable") #adding keys and values
file=json_txt.load_txt("main.txt") #load the txt file
print(json_txt.extract_data(file)) #printing key value pairs

edit_data('main.txt',"sleep","active") #adding keys and values
# file=json_txt.load_txt("main.txt") #load the txt file
print(json_txt.extract_data(file)) #printing key value pairs

####extracting keys and values separately
print(json_txt.extract_keys(file)) #printing the updated key values
print(json_txt.extract_values(file)) #printing the updated values values
```


### Output

```python
✓ Test 1 pass
✓ Test 2 pass
✓ Test 3 pass
All Test Passed
{'setting': 'active', 'work': '9', 'lol': '8', 'sleep': 'disable'}
✓ Test 1 pass
✓ Test 2 pass
✓ Test 3 pass
All Test Passed
{'setting': 'active', 'work': '9', 'lol': '8', 'sleep': 'active'}
['setting', 'work', 'lol', 'sleep']
['active', '9', '8', 'active']
```

## Badges


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/kshitij1235/Json_txt/blob/main/LICENSE)

  
## Authors

- [@kshitij1235](https://github.com/kshitij1235)

  
