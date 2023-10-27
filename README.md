# HISTORY / SECOND

This is my final project for _CSCA 5028 Applications of Software Architecture for Big Data at CU Boulder_. You can view
it on any web-enabled device at https://gz-hps-01b3926752ea.herokuapp.com The aim of the project is to showcase the vast
collection of historical artifacts at NYC's Metropolitan Museum of Art. It accomplishes this by displaying a new photo
of a random item from the museum's collection (roughly) every second.

All of this is accomplished by 3 isolated microservices (Docker images), hosted on Heroku and communicating via RabbitMQ
(CloudAMQP):
* Collector service accesses the museum's public API. It retrieves information about an item in the museum's collection.
It then publishes this information via RabbitMQ. This process is repeated every minute.
* Transformer service uses RabbitMQ to receive the data that Collector publishes. It analyzes this data: if the relevant
museum item is determined to be in public domain and has a valid photo hosted online by the museum (links are checked
and some end up being broken), said photo's URL is published using RabbitMQ (in a separate channel).
* Renderer service has 2 separate running processes:
* * The first process uses RabbitMQ to receive analyzed (transformed) data, published by the Transformer. It stores said
data in a MongoDB database.
* * The second process is a Flask app that retrieves a random piece of data (museum item's photo's URL) from the
database every second and displays it for the user on a simple web page using Ajax Polling.

For clarity, please refer to the Whiteboard Diagram in the project repo: "WHITEBOARD_DIAGRAM.jpg"

#### Tech Stack (Python)
* Flask
* MongoDB (via PyMongo)
* RabbitMQ (via CloudAMQP & Pika)
* Docker
* Heroku

Choosing an appropriate tech stack for the project was not easy. Since the project was small and rather simple, Python
became the language of choice. For something larger and with more contributors, Java might have been preferred. Flask
was chosen as the web framework over the alternatives (like Django). This was because the project was (again) smaller
scale but also because the bare-bones, modular structure of Flask lends itself well to the microservices architecture.
A document-based NoSQL database, MongoDB, was chosen for storage. This was dictated by the project data (simple
key-value pairs) and the operations performed on it (simple put/get). RabbitMQ was chosen for inter-process
communications as its asynchronous nature makes it a good choice for microservices. CloudAMQP was chosen due to its
Heroku integration and low cost, as well as ease of use. For local development, as well as to promote proper service
isolation, Docker was used. Each service was built as a distinct Docker image from the start and was run on a local
Docker network during development, alongside Docker images for Mongo and RabbitMQ. Said images were then easily pushed
to Heroku's container registry and hosted as separate processes in a single Heroku app. Each process has its dedicated
Dyno and can function regardless of the others' status while being independently scalable based on load. Heroku also
allows for continues delivery/deployment, as well as process monitoring with its included dashboards. Grafana add-ons
provide more flexibility when needed. CloudAMQP and MongoDB similarly have their respective monitoring tools built-in
as a web dashboard. All of the above are easily testable and can be switched out for better alternatives as the project
evolves.
