// Copyright 2021 The DaisyKit Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*
Implementation for class Base Model, the abstract class for all models.
All models should be inherited from this class to guarantee
the operation of loading model, predicting model and other basics.
*/

#include "daisykitsdk/models/ncnn_model.h"

// NCNN
#ifdef DAISYKIT_WITH_VULKAN
#include <gpu.h>
#endif

#include <iostream>
#include <string>

namespace daisykit {
namespace models {

/// Initialize a NCNN model.
NCNNModel::NCNNModel(bool use_gpu) {
#ifdef DAISYKIT_WITH_VULKAN
  if (ncnn::get_gpu_count() == 0) {
    std::cerr << "No GPU. Disabling GPU computation." << std::endl;
    use_gpu = false;
  }
  use_gpu_ = use_gpu;
#else
  use_gpu_ = false;
#endif
}

/// Initialize a NCNN from buffers.
NCNNModel::NCNNModel(const char* param_buffer,
                     const unsigned char* weight_buffer, bool use_gpu) {
#ifdef DAISYKIT_WITH_VULKAN
  use_gpu_ = use_gpu;
  if (ncnn::get_gpu_count() == 0) {
    std::cerr << "No GPU. Disabling GPU computation." << std::endl;
    use_gpu = false;
  }
#else
  use_gpu_ = false;
#endif
  // TODO (vietanhdev): Handle model loading result
  LoadModel(param_buffer, weight_buffer, use_gpu);
}

/// Initialize a NCNN model from files.
NCNNModel::NCNNModel(const std::string& param_file,
                     const std::string& weight_file, bool use_gpu) {
#ifdef DAISYKIT_WITH_VULKAN
  use_gpu_ = use_gpu;
  if (ncnn::get_gpu_count() == 0) {
    std::cerr << "No GPU. Disabling GPU computation." << std::endl;
    use_gpu = false;
  }
#else
  use_gpu_ = false;
#endif
  // TODO (vietanhdev): Handle model loading result
  LoadModel(param_file, weight_file, use_gpu);
}  // namespace models

int NCNNModel::LoadModel(const char* param_buffer,
                         const unsigned char* weight_buffer, bool use_gpu) {
  // https://github.com/VNOpenAI/daisykit/commit/89fbf2fcf34c75662c23d5f48abc3a538fae7e93#r56348806
  model_.clear();
  model_.opt.use_vulkan_compute = use_gpu;
  if (model_.load_param_mem(param_buffer) != 0) {
    std::cerr << "Failed to load model params from buffer." << std::endl;
    return -1;
  }
  if (model_.load_model(weight_buffer) != 0) {
    std::cerr << "Failed to load model params from buffer." << std::endl;
    return -2;
  }
  return 0;
}

int NCNNModel::LoadModel(const std::string& param_file,
                         const std::string& weight_file, bool use_gpu) {
  model_.clear();
  model_.opt.use_vulkan_compute = use_gpu;
  if (model_.load_param(param_file.c_str()) != 0) {
    std::cerr << "Failed to load model params from buffer." << std::endl;
    return -1;
  }
  if (model_.load_model(weight_file.c_str()) != 0) {
    std::cerr << "Failed to load model params from buffer." << std::endl;
    return -2;
  }
  return 0;
}

int NCNNModel::Infer(const ncnn::Mat& in, ncnn::Mat& out,
                     const std::string& input_name,
                     const std::string& output_name) {
  if (in.empty()) {
    return -1;
  }

  ncnn::MutexLockGuard g(model_mutex_);
  ncnn::Extractor ex = model_.create_extractor();
  ex.input(input_name.c_str(), in);
  ex.extract(output_name.c_str(), out);

  return 0;
}

int NCNNModel::Infer(const ncnn::Mat& in, std::map<std::string, ncnn::Mat>& out,
                     const std::string& input_name,
                     const std::vector<std::string>& output_names) {
  if (in.empty()) {
    return -1;
  }

  ncnn::MutexLockGuard g(model_mutex_);
  ncnn::Extractor ex = model_.create_extractor();
  ex.input(input_name.c_str(), in);

  // Extract outputs
  for (auto name : output_names) {
    // Prepare placeholders for outputs
    out.insert(std::make_pair(name, ncnn::Mat()));
    // Extract output
    ex.extract(name.c_str(), out[name]);
  }

  return 0;
}

int NCNNModel::Infer(const std::map<std::string, ncnn::Mat>& in,
                     std::map<std::string, ncnn::Mat>& out,
                     const std::vector<std::string>& output_names) {
  if (in.empty()) {
    return -1;
  }

  ncnn::MutexLockGuard g(model_mutex_);
  ncnn::Extractor ex = model_.create_extractor();
  for (auto const& input : in) {
    ex.input(input.first.c_str(), input.second);
  }

  // Extract outputs
  for (auto name : output_names) {
    // Prepare placeholders for outputs
    out.insert(std::make_pair(name, ncnn::Mat()));
    // Extract output
    ex.extract(name.c_str(), out[name]);
  }

  return 0;
}

int NCNNModel::Infer(const std::map<std::string, ncnn::Mat>& in, ncnn::Mat& out,
                     std::string& output_name) {
  if (in.empty()) {
    return -1;
  }

  ncnn::MutexLockGuard g(model_mutex_);
  ncnn::Extractor ex = model_.create_extractor();
  for (auto const& input : in) {
    ex.input(input.first.c_str(), input.second);
  }

  // Extract output
  ex.extract(output_name.c_str(), out);

  return 0;
}

}  // namespace models
}  // namespace daisykit
