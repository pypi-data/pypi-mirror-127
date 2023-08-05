## To build docker container locally 
```angular2html
docker buildx build --platform=linux/amd64 -t spotml-batch-job:latest .
```

## To tag the docker container with ECR repo url
```angular2html
docker tag spotml-batch-job:latest 625539840132.dkr.ecr.us-east-1.amazonaws.com/spotml-batch-job:latest
```

## If you are logged out of aws cli ECR, you can login with this
```angular2html
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 625539840132.dkr.ecr.us-east-1.amazonaws.com
```

## To push the docker container to the ECR
```angular2html
docker push 625539840132.dkr.ecr.us-east-1.amazonaws.com/spotml-batch-job:latest
```

## To run the docker container locally
```angular2html
docker run -it spotml-batch-job:latest
```

If you want to test the cli with localhost:3000 api then, add the below line to your ~/.zshrc or ~/.bashrc file.   
```
export SPOTML_ENV="LOCAL"
```
## To publish the package to pypi

To package the source code into dist folder.
1. Delete the `build` and `dist` folders in your root directory(if exists)
2. Generate the dist folder.
3. Check all is well
4. Push the package to Pypi repo
```angular2html
rm -fR build && rm -fR dist && python setup.py sdist bdist_wheel && twine check dist/* && twine upload dist/*
```
