cmake_minimum_required(VERSION 3.4)
project(image_processor)

find_package(OpenCV REQUIRED)
find_package(pybind11 REQUIRED)

pybind11_add_module(image_processor image_processor.cpp)
target_link_libraries(image_processor PRIVATE ${OpenCV_LIBS})
