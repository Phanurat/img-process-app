#include <pybind11/pybind11.h>
#include <opencv2/opencv.hpp>

namespace py = pybind11;

cv::Mat apply_gray_scale(const cv::Mat& input) {
    cv::Mat gray;
    cv::cvtColor(input, gray, cv::COLOR_BGR2GRAY);
    return gray;
}

PYBIND11_MODULE(image_processor, m) {
    m.def("apply_gray_scale", &apply_gray_scale, "Apply grayscale filter to an image");
}
