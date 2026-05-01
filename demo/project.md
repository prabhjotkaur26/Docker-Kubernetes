# Basic Docker Container Deployment
## Step-by-step procedure:
Pull image → Run → Open in browser
### Step 1: Make sure Docker is running
Open Docker Desktop
Make sure it shows Running
----
### Step 2: Pull image from Docker Hub

We’ll use Nginx (simple web server)

Run:

docker pull nginx

What happens:

Docker downloads nginx image from Docker Hub
----
###  Step 3: Check image downloaded
docker images

You should see:

nginx
----
### Step 4: Run container from image
docker run -d -p 8080:80 nginx

Meaning:

-d → run in background
-p 8080:80 → map port
8080 (your PC) → 80 (container)
----
### Step 5: Check running container
docker ps

You should see nginx container running
----
### Step 6: Open in browser

Open:

http://localhost:8080
----
### Output

You will see:

- Welcome to nginx!

This is the default page from Nginx

### What you just did
1. Pulled image from Docker Hub
2. Created container from image
3. Exposed port
4. Accessed app in browser
