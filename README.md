
# Zoe Depth Estimation

ZoeDepth is a deep learning model for metric depth estimation from a single image by [Intelligent Systems Lab Org](https://github.com/isl-org). This project demonstrates the creation of a comprehensive end-to-end pipeline, incorporating FastAPI and Docker by using [ZoeDepth](https://github.com/isl-org/ZoeDepth) model

## Usage/Examples


### CLI Usage
```bash
usage: cli.py [-h] input_image output_image

Depth estimation using ZoeDepth

positional arguments:
  input_image   Path to input image.
  output_image  Path to ouput depth map.

options:
  -h, --help    show this help message and exit
```
### API Usage
```
http://127.0.0.1:8000/predict
```

## Installation

Install depth estimator with poetry

```bash
pip install poetry #If poetry is not installed
poetry install
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`IMAGE_API_KEY`


## Deployment

To deploy this project run

```bash
  docker build -t depth_estimation .
  docker run -d -p 8041:8041 depth_estimation
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

