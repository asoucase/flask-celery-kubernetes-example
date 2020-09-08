# Flask + Celery + RabbitMQ in Kubernetes
This repository contains the code of a demo app developed with Flask that calculates the [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) in the most non-optimised way possible. 

The application provides the user with a simple form to type in the n-th term of the sequence. Every time a new calculation is submitted, a job gets created and a [celery](https://github.com/celery/celery) worker, using [rabbitmq](https://www.rabbitmq.com) as message broker,  will pick up the job to perform the calculation. 

A list of all jobs created is also presented below the form. 

An instance of [flower](https://github.com/mher/flower) is also included to monitor celery. 

Node Ports: 

- flask app: `30081`
- flower: `30082`



## Screenshots

![](resources/images/screenshot_01.png)

![](resources/images/screenshot_02.png)



## Usage

```bash
$ kubectl apply -f manifests/
```