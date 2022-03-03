# Black-Duck-API

Making use of https://github.com/blackducksoftware/hub-rest-api-python

1. Install the library first by running:
   ```pip3 install blackduck```

2. Setup the environment variable "blackduck_token"

3. Modify the "base_url" to point to your Black Duck instance at line 19

4. Run the script with python 3 to output "licenses.csv" to get the licenses in use and license terms

API License Inventory 

Sample output:
```
[2022-02-23 12:12:07,549] {Client:51} INFO - Using a session with a 15.0 second timeout and up to 3 retries per request
Processing licenses...
[2022-02-23 12:12:07,550] {Authentication:56} WARNING - ssl verification disabled, connection insecure. do NOT use verify=False in production!
[2022-02-23 12:12:07,641] {Authentication:70} INFO - success: auth granted until 2022-02-23 14:12:07.639347+08:00
Detected 16 licenses...
All Done, exported 16 licenses
```
CSV output:
```
License,Component Count,License Terms
MIT License,828,"['Commercial Use=PERMITTED', 'Disclose Source=PERMITTED',...
ISC License,137,"['Commercial Use=PERMITTED', 'Disclose Source=PERMITTED', ...
Apache License 2.0,36,"['Commercial Use=PERMITTED', 'Compensate Damages=REQUIRED', ...
```

API License Inventory by Project

Sample output:
```
[2022-03-03 16:56:48,408] {Client:51} INFO - Using a session with a 15.0 second timeout and up to 3 retries per request
[2022-03-03 16:56:48,409] {Authentication:56} WARNING - ssl verification disabled, connection insecure. do NOT use verify=False in production!
[2022-03-03 16:56:49,617] {Authentication:70} INFO - success: auth granted until 2022-03-03 18:56:49.615094+08:00
Processing Project: chanp_insecure_bank
Processing Version: 1.0
Processing Version: 1.1
Processing Project: chanp_JavaSecCode
Processing Version: 1.0
Processing Version: 1.1
```

CSV output:
```
License,License Terms,count
Apache License 2.0,Commercial Use=PERMITTED Compensate Damages=REQUIRED ...,769
"BSD 3-clause ""New"" or ""Revised"" License",Commercial Use=PERMITTED...,59
MIT License,Commercial Use=PERMITTED Disclose Source=PERMITTED Distribute=PERMITTED ...,56
```
