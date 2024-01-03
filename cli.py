import argparse

from predictor import DepthEstimationModel


def main():
    parser = argparse.ArgumentParser(description="Depth estimation using ZoeDepth")
    parser.add_argument("input_image", help="Path to input image.")
    parser.add_argument("output_image", help="Path to ouput depth map.")
    args = parser.parse_args()

    model = DepthEstimationModel()
    result = model.calculate_depth_map(args.input_image, args.output_image)
    print(result)


if __name__ == "__main__":
    main()
