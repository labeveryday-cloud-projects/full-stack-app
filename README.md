# Quickstart Guide: Building and Running Your Application with Docker (Full-stack app)

Welcome to the Quickstart Guide for setting up your application using Docker containers! This guide is designed to help you swiftly build and run the frontend and backend parts of your application, ensuring a smooth and efficient development process. Whether you're new to Docker or looking for a refresher, this guide, inspired by insights from a helpful tutorial video, will walk you through the necessary steps to get your application up and running in no time.

![Front-end and backend](./images/architecture.png)

This repo is result from my learnings in this video: https://youtu.be/Jx39roFmTNg

Tools used:

- Backend: [fastAPI](https://fastapi.tiangolo.com)
- Frontend: [React](https://react.dev)
- Containerization: [Docker](https://www.docker.com/)

The notes in this README details how to build both the frontend and backend. 

If you would just like a detailed guide on how to build the application check the [AppBuildGuide](./quickstart.md)

## Getting Started with the Backend Container

The backend of your application is crucial for processing and managing data. Follow these steps to build and run your backend container:

**Build and run backend container**

1. CD to the backend directory.
2. Build the backend container.

```bash
docker build . -t backend
```

>NOTE: The `.` means use the Dockerfile in this directory and the `-t backend` means tag the build as backend.

3. Run the image enter `docker run --name backend --rm -p 8000:8000 backend`

>NOTE: This runs the image with the name backend exposing port 8000 from the host to 8000 within the container and using the image backend. Once its running you will see this:

![Running docker container](./images/backend-docker-running.png)

## Building and Running the Frontend

The frontend of your application provides the user interface. Here’s how to build and run the frontend container:

**Build and run the frontend**

1. CD to the frontend directory
2. In the terminal build the frontend image:

```bash
docker build . -t frontend
```

>Now we need to create a docker network for the frontend and backend to communicate.

## Configuring the Docker Network

A Docker network facilitates the connection between your frontend and backend containers. Follow these steps to set up the network:

**Configure the Docker Network**

1. Before we run the frontend container we need to create the network so the frontend and backend can communicate. Run:

```bash
docker network create frontend-backend-network
```

![docker network](./images/docker-network.png)

2. Verify the backed docker container ID:

```bash
docker ps
```

3. In order to configure the network we need to stop the docker container. 

```bash
docker stop CONTAINER ID
```

## Running the Backend and Frontend Containers

With the network configured, you can now run both containers on this network:

**Run the backend and frontend containers**

1. Restart the backend container but this time with the newly created docker network: 

```bash
docker run --name backend --rm --network frontend-backend-network -p 8000:8000 backend
```

>NOTE: The localhost can still access the docker container with `http://localhost:8000/api`

![Container running on network](./images/docker-build-network.png)

2. Run the frontend container:

```bash
docker run --rm --name frontend --network frontend-backend-network -p 3000:3000 frontend
```

![Successful deployment](./images/successful.png)

## Accessing Your Application

Congratulations! At this point, you can open your web browser and navigate to `http://localhost:3000/`. You should see your application's frontend, now successfully communicating with the backend through Docker containers.

___

### [Optional] Simplifying Deployment with Docker Compose

Rather than deploying each container manually you can deploy your containers with one command using [Docker Compose](https://docs.docker.com/compose/). Docker Compose enables you to define and run multi-container Docker applications with ease. Follow these steps to deploy your application using Docker Compose.

**Deploy Your Application** 

1. Navigate to this Project's Root Directory. Ensure you're in the directory containing your docker-compose.yml.
2. Deploy with Docker Compose: Run the following command:

```bash
docker-compose up --build
```

>NOTE: This builds (if necessary) and starts all the services defined in your Docker Compose file.

**Access Your Application**

1. With your containers running, you can access your application by navigating to http://localhost:3000/ in your web browser. You should see your frontend communicating seamlessly with the backend.

**Stopping Your Application**

1. To stop your application and remove the containers, networks, and volumes associated with it, run:

```bash
docker-compose down
```

This Quickstart Guide has walked you through building and running your application's backend and frontend in Docker. With your containers up and running, you're well on your way to developing and testing your application with ease. Happy coding!
