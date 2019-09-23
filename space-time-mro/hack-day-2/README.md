
# Usage
- The notebooks currently aim to work on collab and locally but the steps to get them running will vary slightly. 
- For colab you will need to run a cell at the top of each notebook which installs the additional missing packages. 
- For working with these notebooks locally you will need to make sure you have Azcopy insalled. The steps for doing this can be found at https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10
- The pigeon tool for annotation currently only works in Jupyter notebooks not Jupyter labs ☹️
- You can find a conda environment 'maps-environment.yml' which *should* contain all the python packages you need. The pytorch package will automagically determine whether to install cpu or gpu version
- For any serious training of models it would be recommended to use a vm with GPU



