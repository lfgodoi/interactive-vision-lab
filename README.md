## Interactive Vision Lab (interactive-vision-lab)

A fullstack project that brings together image processing and analysis techniques through an interactive platform.

- Developer: _Leonardo Franco de Godói_
- GitHub profile: _https://github.com/lfgodoi_
- Contact: _eng.leonardogodoi@gmail.com_

### Running the app directly

It is usually common to need to run the app directly using Python for development and testing purposes, without the need to use Kubernetes, which will only be required for its automatic deployment.

_Navigate to the app directory._

    cd app

_Create a virtual environment._

    python3 -m venv venv

_Activate the virtual environment._

    source venv/bin/activate

_Update the Pip._

    pip install --upgrade pip

_Install the app dependencies._

    pip install -r requirements.txt

_Run the app._

    python main.py

### Accessing the app documentation

FastAPI provides the Swagger, which refers to the automatically generated interactive API documentation provided by the OpenAPI standard. Swagger UI is an interface that visualizes the API documentation in a user-friendly manner, allowing developers and users to explore and test the endpoints of a FastAPI application directly from a web browser.

_Open a browser and open the following URL: http://localhost:8000/docs._

_Find the endpoint you wish to test and click on 'Try it out'._

_Fill the request body parameters and click on 'Execute' to send the request._

_Check whether the response status code is 200 (success) and the content in response body._