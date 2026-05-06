# Basic Deployment (Using HTML)
## We’ll create:
- Own HTML page
- Run it using Docker + httpd
- Open it in browser
---

## FULL STEP-BY-STEP PROJECT
### Step 1: Open Docker Desktop
Start Docker Desktop
Make sure it shows Running
---

### Step 2: Create HTML file
notepad index.html

Paste:
<h1>My First Page</h1>

Save and close.
---

### Step 3: Check file exists
dir

 You must see:

index.html
---
### Step 4: Pull Apache image
docker pull httpd
<img width="1338" height="468" alt="image" src="https://github.com/user-attachments/assets/14cc3b06-9cce-487e-a234-6a4ecdcc7353" />

---
### Step 5: Run container with your HTML
docker run -d -p 8090:80 -v ${PWD}:/usr/local/apache2/htdocs httpd
<img width="1359" height="472" alt="image" src="https://github.com/user-attachments/assets/c349a6c8-7d20-417c-85ef-e84e4215705d" />

---
### Step 6: Open browser
http://localhost:8090
### Final Output

You will see:
My First Page
<img width="1174" height="200" alt="image" src="https://github.com/user-attachments/assets/c72498b8-6369-4908-972f-9a7514634b76" />

---
### What we did
Created HTML page
Pulled image from Docker Hub
Ran container
Used volume mapping
Hosted website locally
