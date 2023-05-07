To create a Docker image, we can use a Dockerfile, which is a simple text file that contains a set of instructions that Docker can use to build an image. Here are the basic steps to create a Docker image:

1. Create a new directory for the Docker image and navigate to it:

```
mkdir myimage
cd myimage
```

2. Create a new file called `Dockerfile` in the directory:

```
touch Dockerfile
```

3. Open the `Dockerfile` in a text editor and add the following lines:

```
FROM base_image
# Replace 'base_image' with the name of the image you want to use as the base.

RUN command1
RUN command2
# Add any additional commands needed to configure the image.
```

The `FROM` instruction specifies the base image that we want to use for our image. For example, if we want to create an image for a Node.js app, we can use the official Node.js image as the base:

```
FROM node:latest
```

The `RUN` instructions are used to execute commands in the container during the build process. For example, we can install dependencies for our app:

```
RUN npm install express
```

4. Save the `Dockerfile` and build the image using the `docker build` command:

```
docker build -t myimage .
```

The `-t` option specifies a name and optional tag for the image, and the `.` at the end specifies the build context (i.e., the directory containing the `Dockerfile`).

5. After the build is complete, we can verify that the image was created by running the `docker images` command:

```
docker images
```

This will show a list of all the Docker images on our system, including the new image we just created.

Overall, creating a Docker image using a Dockerfile provides a simple and repeatable way to package an application and its dependencies, making it easy to distribute and run across different environments.