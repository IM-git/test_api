Docker+Pytest+Allure
====================

Description: Perform the test and save the allure report in the specified location.
Docker image is being created. After running is created an allure report in the docker container. Report is copied to the specified destination.

Execution Steps:
+ docker build -t <name_docker_image> .
+ docker run --name <name_container> -it <name_docker_image>
+ docker cp <name_container>:<path_in_docker_image> <destination_path>
+ allure serve <destination_path>

Additions:
* <name_docker_image> - come up your own **name docker image**.
* <name_container> - come up your own **name docker container**.
* <path_in_docker_image> - the path to the source in the docker container.
* <destination_path> - the destination path to save of the source files.
* if you don't need to use this container anymore, 
  don't forget to perform: **docker stop <name_container>**.


    *I was performing this in Windows System.*