# Flask + Celery + RabbitMQ in Kubernetes
This repository contains the code of a demo app developed with Flask that calculates the [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) in the most non-optimised way possible. 

The application provides the user with a simple form to type in the n-th term of the sequence. Every time a new calculation is submitted, a job gets created and a [celery](https://github.com/celery/celery) worker, using [rabbitmq](https://www.rabbitmq.com) as message broker,  will pick up the job to perform the calculation. 

A list of all jobs created is also presented below the form. 

An instance of [flower](https://github.com/mher/flower) is also included to monitor celery. 

Node Ports: 

- flask app: `30081`
- flower: `30082`



## Screenshots

![](https://github.com/asoucase/flask-celery-kubernetes-example/blob/master/.github/images/screenshot_01.png?raw=true)

![](https://github.com/asoucase/flask-celery-kubernetes-example/blob/master/.github/images/screenshot_01.png?raw=true)


## Usage

### Docker Compose

Just as simple as running:

```bash
$ docker-compose up --build
```



### Kubernetes

In order to deploy the demo app stack on a kubernetes cluster, you must build and push the images into a container registry. In this repository, we will make use of [docker hub](https://hub.docker.com).

Please login into docker hub with the command:

```bash
$ docker login
```



Steps:

1. Set docker hub username in `.env` file

    ```
    DOCKERHUB_USERNAME=arturosoucase
    ```

2. Build images

      ```bash
    $ docker-compose build
      ```

3. Push images into Docker Hub

      ```bash
    $ docker-compose push
      ```

4. Apply kubernetes manifest files:

    ```bash
    $ kubectl apply -f manifests/
    ```
   
### Diagram

![](https://github.com/asoucase/flask-celery-kubernetes-example/blob/master/.github/images/k8s-diagram.svg?raw=true)
