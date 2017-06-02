# pyimagingdock

Image processing methods from Python and SimpleITK exposed through Docker.  Based off of the pysciencedock
design here: http://github.com/Kitware/pysciencedock


## Local usage

List methods available with JSON descriptions of inputs and outputs:
```
python -m pyimagingdock
```

Print help information for a method:
```
python -m pyimagingdock <method> --help
```

Run one of the methods:
```
python -m pyimagingdock <method> <arg1> ...
```

## Usage through Docker

List the methods available through Docker:
```
docker run pyimagingdock
```

Run a method through Docker:
```
docker run <docker_options> pyimagingdock <method> <arg1> ...
```

In order to send data files to Docker, mount a volume and use the mounted
volume prefix for the input and output paths. For example, if `myinput.csv`
is in your current directory, the following will produce `myoutput.csv` in
the current directory:
```
docker run -v $PWD:/data pyimagingdock ImagePassThroughFilter --image=/data/myinput.png --output=/data/myoutput.png
```

Build the Docker image:
```
git clone https://github.com/curtislisle/pyimagingdock.git
cd pyimagingdock
docker build -t pyimagingdock .
```

## Usage through Girder

* Install Girder.
* Enable the "Item tasks" plugin.
* Start a `girder_worker` Celery worker and point it and the Worker plugin settings to use the same task queue.
* From any folder you have write access to (you must be admin), select
  "Add tasks" from the actions menu.
* Enter "kitware/pyimagingdock" as the image name and click Run.
* When that task completes, navigate to a created task item and select
  "Run task" from the actions menu.
* Fill in the task parameters and click Run.

## Testing

To run the unit tests:

```
python -m unittest tests
```
