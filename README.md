# Movie booking API 


## Project topic: Movie Mood

### Brief details about the project:

This is a server-side web service built using Python's Django and Django REST Framework.

It has the following CRUD functionalities:

<ul>
<li><b>User</b> - creating/deleting/updating/retrieving users and authenticating and authorizing using the credentials of the users. Supports the both Basic Email/Password and Token authentication.</li>
<li><b>Movie</b> - creating/deleting/updating/retrieving movies. You can get more details about the fields in API Documentation documented using Swagger.</li>
<li><b>Events</b> - creating/deleting/updating/retrieving movie events. You can create an event for a speicific movie. You can assign venue and the date and time of the event. You can also specify the price of the ticket. You can get more details about this Event model in API Documentation documented using Swagger.</li>
<li><b>Bookings</b> - creating/deleting/updating/retrieving bookings. You can make a booking for an event by specifying the number of tickets and you will get all of the details about the booking once you create the booking. You can also edit your bookings. You can get more details about this Event model in API Documentation documented using Swagger.</li>
<li><b>Reviews</b> - creating/deleting/updating/retrieving reviews. You can leave a review for a specific movie by writing your review and a rate of the movie. You can get more details about this Event model in API Documentation documented using Swagger.</li>
</ul>

You can explore all of the models in the API Documentation on the following url once you run the project:
```localhost:8000/swagger/```


### Brief details about the docker containers included in the project:
You can explore the ```docker-compose.yml``` to get the broader image of a project setup.

It basically contains 2 containers:
<ul>
<li><b>web</b> - this is the service for the API</li>
<li><b>db</b> - this is the Postgres database service of the API.</li>
</ul>  

## Students worked on the project:
<ul>
<li>Javokhirbek Khaydaraliev - Student NR: <b>40797</b></li>
<li>Shakhzod Yuldoshov - Student NR: <b>41821</b></li>
</ul>

## Requirements to run the project
<ul>
<li>Docker</li>
</ul>

## Steps to run the project
1. Make sure you have the <i>Docker</i> installed in your PC and start the <i>Docker</i>.

2. Once you have the <i>Docker</i> running, execute the following command in the terminal of your choice:
    ```bash
    $ docker-compose up --build
    ```
    Make sure to include the ```--build``` flag since it will reflect the changes you made to the project.

3. Once you execute the above command, the docker services will start to build in separate containers. Once the containers are build, the app will start on port ```8000```.

4. Once you have the project running, you can access the project at the following url:
```localhost:8000/swagger```.

5. Once you access the ```localhost:8000/swagger```, you will be redirected to the interactive documentation of API using Swagger. 
You should see the following page:

<img src="https://i.imgur.com/kMk8Z8O.png">


## Interactive in-build Django REST Client

You can also use more interactive API Client for interacting with the API using Django REST Framework's UI.

## Usage
Simply vising the API Endpoints on the localhost:

#### Example usage for Users functionality:
```localhost:8000/api/users/create/```
<br>

Once you visit the above URL, you will get the following view:
<img src="https://i.imgur.com/FexZiTE.png">

You can directly interact with the API.

Once you navigate to ```localhost:8000```
you will get the following view:
<img src="https://i.imgur.com/pFdLcZp.png">

More details about the api endpoints:

```localhost:8000/admin/``` - you can authenticate the use using this url <br>
```localhost:8000/api/users/``` - endpoint for users funcitionality <br>
```localhost:8000/api/movies/``` - endpoint for movies functionality <br>
```localhost:8000/api/bookings/``` - endpoint for bookings functionality <br>
```localhost:8000/api/events/``` - endpoint for events functionality <br>
```localhost:8000/swagger/``` - endpoint for swagger documentation
```localhost:8000/redoc/``` - endpoint for redocly documentation

