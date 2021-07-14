# apiPy

ApiPy was created for api testing with Python **pytest framework** which has also **requests**, **assertpy** and **pytest-html-reporter** libraries. With this framework you can create api tests to call http **GET**, **POST**, **UPDATE** and **DELETE** methods.

- **requests:** for calling http methods
- **asserpy:** for making assertions
- **pytest-html-reporter:** for creating html report

![](https://i.ibb.co/Vt9xXwq/pytest-html-reporter.png)

# Install
Pipenv is used to create a virtualenv. So just clone this project, go to the directory of the project and run below commands.

```sh
cd apiPy
pipenv shell 
pytest --html-report=./report
```

 **Note:** In order to run sample tests https://gorest.co.in/ endpoints was used. Before start to test don't forget to get an access token from gorest.co to be able to run these tests.