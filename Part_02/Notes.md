1. When using Hugging Face library, it stores all the model corresponding data bydefault inside the `cache` folder of your system `HOME` directory. And this location inside the Hugging Face code is present in the `HF_HOME` variable. 

2. As can be seen from the image, that in our `HOME` directory we only have 2GiB space, and it won't be sufficient for large models, so we will change the default location in the variable `HF_HOME`  (More details about it can be seen from [here](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables)) and will store inside `/run` location as it has 100GiB of space available.
![alt text](/images/Storage_in_SaturnCloud.png)

3. As hugging face stores the file inside the cache folder inside HOME directory which in our case doesn't have mmuch storage, so changing the default storage of Hugging Face. `HF_HOME` is the variable which contains the location to store the Hugging Face data.
    ```python
    os.environ['HF_HOME'] = '/run/cache/'
    ```

4. 