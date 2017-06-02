FROM python:2-onbuild
#RUN pip install SimpleITK
ENTRYPOINT ["python", "-m", "pyimagingdock"]
